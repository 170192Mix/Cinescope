
from typing import Any, Dict, Optional
from custom_requester.custom_requester import CustomRequester
from constants import API_BASE, MOVIES_ENDPOINT

class MoviesAPI(CustomRequester):
    """
    Класс-обёртка над эндпоинтами /movies.
    Наследуемся от CustomRequester, чтобы использовать:
      - send_request/post/get/patch/delete
      - expected_status
      - общий лог/хедеры/базовый URL
    """

    def __init__(self, session, base_url: str = API_BASE, headers: Optional[Dict[str, str]] = None):
        super().__init__(session=session, base_url=base_url, headers=headers)

    # POST /movies
    def create_movie(self, payload: Dict[str, Any], expected_status: int = 201):
        return self.post(MOVIES_ENDPOINT, json=payload, expected_status=expected_status)

    # GET /movies/id
    def get_movie(self, movie_id: str, expected_status: int = 200):
        return self.get(f"{MOVIES_ENDPOINT}/{movie_id}", expected_status=expected_status)

    # PATCH /movies/id
    def patch_movie(self, movie_id: str, payload: Dict[str, Any], expected_status: int = 200):
        return self.patch(f"{MOVIES_ENDPOINT}/{movie_id}", json=payload, expected_status=expected_status)

    # PUT /movies/id (если в контракте есть)
    def put_movie(self, movie_id: str, payload: Dict[str, Any], expected_status: int = 200):
        return self.put(f"{MOVIES_ENDPOINT}/{movie_id}", json=payload, expected_status=expected_status)

    # DELETE /movies/id
    def delete_movie(self, movie_id: str, expected_status: int = 200):
        return self.delete(f"{MOVIES_ENDPOINT}/{movie_id}", expected_status=expected_status)

    # GET /movies (листинг/фильтры/сортировка/пагинация)
    def list_movies(self, params: Optional[Dict[str, Any]] = None, expected_status: int = 200):
        return self.get(MOVIES_ENDPOINT, params=params or {}, expected_status=expected_status)