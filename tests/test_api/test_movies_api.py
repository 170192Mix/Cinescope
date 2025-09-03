
from typing import Any, Dict, Optional, Union, Tuple # для аннотаций — чтобы код был понятнее

from constants import API_BASE, MOVIES_ENDPOINT
from custom_requester.custom_requester import CustomRequester


Expected = Union[int, Tuple[int, ...]] # это просто удобное сокращение типа для параметра expected_status


class MoviesAPI(CustomRequester):
    """
    Клиент для работы с эндпоинтами /movies.
    Схема такая же, как в других API-классах проекта: наследуемся от
    CustomRequester и в методах напрямую зовём send_request
    """

    def __init__(self, session, base_url: str = API_BASE, headers: Optional[Dict[str, str]] = None):
        super().__init__(session=session, base_url=base_url, headers=headers)

    # POST /movies
    def create_movie(self, payload: Dict[str, Any], expected_status: Expected = 201):
        return self.send_request(
            method="POST",
            endpoint=MOVIES_ENDPOINT,
            json=payload,
            expected_status=expected_status,
        )

    # GET /movies/{id}
    def get_movie(self, movie_id: Union[str, int], expected_status: Expected = 200):
        return self.send_request(
            method="GET",
            endpoint=f"{MOVIES_ENDPOINT}/{movie_id}",
            expected_status=expected_status,
        )

    # PATCH /movies/{id}
    def patch_movie(self, movie_id: Union[str, int], payload: Dict[str, Any], expected_status: Expected = 200):
        return self.send_request(
            method="PATCH",
            endpoint=f"{MOVIES_ENDPOINT}/{movie_id}",
            json=payload,
            expected_status=expected_status,
        )

    # PUT /movies/{id}  (если нужно по контракту)
    def put_movie(self, movie_id: Union[str, int], payload: Dict[str, Any], expected_status: Expected = 200):
        return self.send_request(
            method="PUT",
            endpoint=f"{MOVIES_ENDPOINT}/{movie_id}",
            json=payload,
            expected_status=expected_status,
        )

    # DELETE /movies/{id}
    def delete_movie(self, movie_id: Union[str, int], expected_status: Expected = 200):
        return self.send_request(
            method="DELETE",
            endpoint=f"{MOVIES_ENDPOINT}/{movie_id}",
            expected_status=expected_status,
        )

    # GET /movies  (листинг/фильтры/сортировка/пагинация)
    def list_movies(self, params: Optional[Dict[str, Any]] = None, expected_status: Expected = 200):
        return self.send_request(
            method="GET",
            endpoint=MOVIES_ENDPOINT,
            params=params or {},
            expected_status=expected_status,
        )