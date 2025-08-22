
import os
import pytest
import requests

from constants import API_BASE, CINESCOPE_AUTH_BASE_URL, HEADERS
from api.movies_api import MoviesAPI
from utils.data_generator import DataGenerator

AUTH_URL = f"{CINESCOPE_AUTH_BASE_URL}/login" # Собираем полный URL авторизации: база + /login


# Фикстуры авторизации и клиента

@pytest.fixture(scope="session")
def admin_token() -> str:
    """
    Получаем accessToken пользователя-админа.
    Берём из переменных окружения, чтобы не хардкодить; если их нет — используем дефолт.
    """
    email = os.getenv("ADMIN_EMAIL", "api1@gmail.com") # Берём логин/пароль из переменных окружения
    password = os.getenv("ADMIN_PASSWORD", "asdqwe123Q") # Если их нет — используем дефолтные значения

    r = requests.post( # Делаем POST на /login
        AUTH_URL,
        json={"email": email, "password": password}, # Передаём тело запроса как JSON (email+password)
        headers=HEADERS,
        verify=False,  # отключаем проверку SSL
        timeout=30, # на случай подвисаний
    )
    assert r.status_code == 200, f"Login failed: {r.status_code} {r.text}" # Гарантируем, что логин успешен (иначе тесты дальше не имеют смысла)
    token = r.json().get("accessToken") # Достаём JWT-токен из ответа (это ключ к API) Сервер доверяет только тем, кто показывает этот билет в заголовке
    assert token, f"No accessToken in response: {r.text}" # Проверяем что он не пустой
    return token


@pytest.fixture(scope="session") # Получает session (из твоего conftest.py) и admin_token (что выше)
def movies_api(session, admin_token) -> MoviesAPI: # Возвращаем готовый клиент
    """
    Клиент MoviesAPI на общей session из conftest, с подставленным Bearer-токеном
    """
    headers = {**HEADERS, "Authorization": f"Bearer {admin_token}"} # Склеиваем заголовки
    return MoviesAPI(session=session, base_url=API_BASE, headers=headers) # Создаем экземпляр


# Вспомогательные фикстуры

@pytest.fixture
def movie_payload():
    """
    Генерируем валидный payload для создания фильма
    (см. методы в DataGenerator внизу)
    """
    return DataGenerator.generate_movie_payload() # Отдаёт свежий валидный JSON для создания фильма — чтобы не хардкодить


@pytest.fixture
def created_movie(movies_api, movie_payload):
    """
    Создаём фильм до теста и удаляем после
    Удобно для тестов чтения/обновления/негатива
    """
    resp = movies_api.create_movie(movie_payload, expected_status=201)
    body = resp.json()
    # ID может называться по-разному, подстрахуемся
    movie_id = body.get("id") or body.get("uuid") or body.get("_id")
    assert movie_id, f"No id in create response: {body}"

    yield {"id": movie_id, "body": body, "payload": movie_payload}

    # Teardown: чисто на всякий случай удалим (если ещё не удалили в тесте)
    try:
        movies_api.delete_movie(movie_id, expected_status=204)
    except AssertionError:
        # Если уже удалён (404) — ок
        pass


# ПОЗИТИВНЫЙ CRUD-ТЕСТ

class TestMoviesCRUD:

    def test_create_get_update_delete_movie(self, movies_api, movie_payload):
        # CREATE
        r_create = movies_api.create_movie(movie_payload, expected_status=201)
        created = r_create.json()
        movie_id = created.get("id") or created.get("uuid") or created.get("_id")
        assert movie_id, f"No id in response: {created}"

        # GET
        r_get = movies_api.get_movie(movie_id, expected_status=200)
        got = r_get.json()
        # В Swagger у объекта поле name (не title)
        assert got.get("name") == movie_payload["name"]

        # PATCH — поменяем, например, description
        patch_payload = DataGenerator.movie_patch_payload()
        r_patch = movies_api.patch_movie(movie_id, patch_payload, expected_status=200)
        patched = r_patch.json()
        assert patched.get("description") == patch_payload["description"]

        # DELETE
        movies_api.delete_movie(movie_id, expected_status=204)

        # GET после удаления — ожидаем 404
        movies_api.get_movie(movie_id, expected_status=404)


# НЕГАТИВНЫЕ ТЕСТЫ

class TestMoviesNegative:

    def test_get_not_found(self, movies_api):
        movies_api.get_movie("non-existent-id-123", expected_status=404)

    def test_create_invalid_payload(self, movies_api):
        bad_payload = DataGenerator.movie_invalid_payload()
        movies_api.create_movie(bad_payload, expected_status=400)

    def test_patch_invalid_payload(self, movies_api, created_movie):
        movie_id = created_movie["id"]
        bad = {"year": "abc"}  # нарушаем тип явно
        movies_api.patch_movie(movie_id, bad, expected_status=400)

    def test_unauthorized_access(session):
        """
        Проверяем, что без Authorization токена API не пускает
        """
        raw_client = MoviesAPI(
            session=session,
            base_url=API_BASE,
            headers={"Accept": "application/json"}  # без Bearer
        )
        raw_client.list_movies(expected_status=401)


# ФИЛЬТРЫ / ПАГИНАЦИЯ

class TestMoviesList:

    @pytest.mark.parametrize(
        "params",
        [
            {"genre": "Drama"},          # фильтр по жанру (имя зависит от контракта)
            {"published": True},         # фильтр по публикации
            {"sort": "rating,desc"},   # сортировка
            {"page": 1, "pageSize": 10},  # пагинация
        ]
    )
    def test_list_with_filters(self, movies_api, params):
        r = movies_api.list_movies(params=params, expected_status=200)
        body = r.json()

        # По контракту листинг возвращает объект:
        # {
        #   "movies": [...],
        #   "count": 13,
        #   "page": 1,
        #   "pageSize": 10,
        #   "pageCount": 2
        # }
        assert isinstance(body, dict), f"Unexpected response: {body}"
        assert "movies" in body, f"No 'movies' in list response: {body}"
        assert isinstance(body["movies"], list), f"'movies' is not a list: {type(body['movies'])}"

        # Доп.проверки пагинации, если есть в ответе
        if "page" in body and "pageSize" in body:
            assert body["page"] >= 1
            assert body["pageSize"] > 0