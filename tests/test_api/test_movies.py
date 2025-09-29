import pytest
from faker import Faker
from uuid import uuid4

fake = Faker()

# Параметры из Swagger для /movies (оставили только то, что реально задокументировано)
MOVIES_PARAM_PAGE = "page"
MOVIES_PARAM_LIMIT = "pageSize"


# Хелперы
def _extract_items_or_fail(resp_json):
    if isinstance(resp_json, dict) and isinstance(resp_json.get("movies"), list):
        return resp_json["movies"]
    raise AssertionError(
        f"Нарушен контракт списка: ожидали dict с movies:list, получили {type(resp_json)}; "
        f"keys={list(resp_json.keys()) if isinstance(resp_json, dict) else None}"
    )


def _create_movies(admin_api, base_payload, count, anchor, extra=None):
    """
    CHANGED: добавлен параметр extra (ADDED), чтобы можно было задавать
    изолирующие поля (например, уникальный location) и не зависеть от мусора в БД
    """
    extra = extra or {}
    ids = []
    for i in range(count):
        payload = {**base_payload, **extra, "name": f"{anchor} #{i} {base_payload['name']}"}
        j = admin_api.movies_api.create_movie(payload, expected_status=201).json()
        movie_id = j.get("id") or (j.get("movie") or {}).get("id")
        assert movie_id, "Создание фильма не вернуло id"
        ids.append(movie_id)
    return ids


def _cleanup_movies(admin_api, ids):
    """Небольшая защита от None/пустого списка"""
    for mid in ids or []:  # CHANGED: на случай ids=None
        admin_api.movies_api.delete_movie(mid, expected_status=(200, 204, 202))


# Фикстуры
@pytest.fixture
def movie_payload():
    """Базовый валидный payload на создание фильма"""
    return {
        "name": f"{fake.word().upper()}_{fake.random_int(100, 999)}",
        "description": fake.sentence(nb_words=6),
        "genreId": 1,
        "imageUrl": "https://example.com/movie.jpg",
        "price": 500,
        "location": "MSK",   # по умолчанию MSK; в тестах можем переопределять через extra
        "published": True,
    }


# CRUD
def test_create_movie(admin_api, movie_payload):
    """Создание, чтение, удаление"""
    resp = admin_api.movies_api.create_movie(movie_payload, expected_status=201)
    body = resp.json()

    movie_id = body.get("id") or (body.get("movie") or {}).get("id")
    assert movie_id, "В ответе на создание нет id"

    got = admin_api.movies_api.get_movie(movie_id, expected_status=200).json()
    assert got.get("name") == movie_payload["name"], "Имя не совпало после GET"

    admin_api.movies_api.delete_movie(movie_id, expected_status=(200, 204, 202))


def test_patch_movie(admin_api, movie_payload):
    """PATCH имени и проверка, что поменялось"""
    created = admin_api.movies_api.create_movie(movie_payload, expected_status=201).json()
    movie_id = created.get("id") or (created.get("movie") or {}).get("id")

    patch = {"name": movie_payload["name"] + " PATCH"}
    admin_api.movies_api.patch_movie(movie_id, patch, expected_status=200)

    got = admin_api.movies_api.get_movie(movie_id, expected_status=200).json()
    assert got.get("name", "").endswith("PATCH"), "Имя после PATCH не обновилось"

    admin_api.movies_api.delete_movie(movie_id, expected_status=(200, 204, 202))


def test_delete_movie(admin_api, movie_payload):
    """После DELETE ресурс должен отсутствовать (404)"""
    created = admin_api.movies_api.create_movie(movie_payload, expected_status=201).json()
    movie_id = created.get("id") or (created.get("movie") or {}).get("id")

    admin_api.movies_api.delete_movie(movie_id, expected_status=(200, 204, 202))
    admin_api.movies_api.get_movie(movie_id, expected_status=404)


# Пагинация
def test_movies_pagination_basic(admin_api, movie_payload):
    """
    Пагинация по контракту Swagger: ?page, ?pageSize
    Должно быть:
      - при pageSize=1 возвращается ровно 1 элемент,
      - page=1 и page=2 — РАЗНЫЕ записи (по id)
    """
    anchor = f"PG_{uuid4().hex[:6]}"

    created_ids = _create_movies(admin_api, movie_payload, count=2, anchor=anchor)

    try:
        # page=1
        r1 = admin_api.movies_api.list_movies(
            params={MOVIES_PARAM_PAGE: 1, MOVIES_PARAM_LIMIT: 1},
            expected_status=200
        ).json()
        assert isinstance(r1.get("movies"), list), "Ответ должен содержать список 'movies'"  # FIX
        assert len(r1["movies"]) == 1, "pageSize=1 должен возвращать 1 элемент"
        id1 = r1["movies"][0]["id"]

        # page=2
        r2 = admin_api.movies_api.list_movies(
            params={MOVIES_PARAM_PAGE: 2, MOVIES_PARAM_LIMIT: 1},
            expected_status=200
        ).json()
        assert isinstance(r2.get("movies"), list), "Ответ должен содержать список 'movies'"  # FIX
        assert len(r2["movies"]) == 1, "pageSize=1 должен возвращать 1 элемент"
        id2 = r2["movies"][0]["id"]

        assert id1 != id2, "Элементы page=1 и page=2 не должны совпадать"

        # метаданные страницы (поля по Swagger)
        assert isinstance(r1.get("page"), int), "page должен быть int"   # FIX (опечатка ниже была)
        assert isinstance(r1.get("pageSize"), int), "pageSize должен быть int" # FIX
    finally:
        _cleanup_movies(admin_api, created_ids)