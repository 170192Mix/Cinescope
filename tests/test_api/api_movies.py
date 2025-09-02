
from custom_requester.custom_requester import CustomRequester
from typing import Any, Dict, Optional
from constants import API_BASE, MOVIES_ENDPOINT

class MoviesAPI(CustomRequester):
    def __init__(self, session, base_url: str = API_BASE, headers: Optional[Dict[str, str]] = None):
        super().__init__(session=session, base_url=base_url, headers=headers)

    # единая точка отправки запросов
    def _call(
        self,
        method: str,
        path: str,
        *,
        expected_status: int | tuple[int, ...] = 200,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Any = None,
        files: Any = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        # все пути строим относительно /movies
        endpoint = f"{MOVIES_ENDPOINT}{path}"
        return self.send_request(
            method=method,
            endpoint=endpoint,
            expected_status=expected_status,
            params=params,
            json=json,
            data=data,
            files=files,
            headers=headers,
        )

    # POST /movies
    def create_movie(self, payload: Dict[str, Any], expected_status: int | tuple[int, ...] = 201):
        return self._call("POST", "", json=payload, expected_status=expected_status)

    # GET /movies/{id}
    def get_movie(self, movie_id: str | int, expected_status: int | tuple[int, ...] = 200):
        return self._call("GET", f"/{movie_id}", expected_status=expected_status)

    # PATCH /movies/{id}
    def patch_movie(self, movie_id: str | int, payload: Dict[str, Any], expected_status: int | tuple[int, ...] = 200):
        return self._call("PATCH", f"/{movie_id}", json=payload, expected_status=expected_status)

    # PUT /movies/{id}
    def put_movie(self, movie_id: str | int, payload: Dict[str, Any], expected_status: int | tuple[int, ...] = 200):
        return self._call("PUT", f"/{movie_id}", json=payload, expected_status=expected_status)

    # DELETE /movies/{id}
    def delete_movie(self, movie_id: str | int, expected_status: int | tuple[int, ...] = 200):
        return self._call("DELETE", f"/{movie_id}", expected_status=expected_status)

    # GET /movies
    def list_movies(self, params: Optional[Dict[str, Any]] = None, expected_status: int | tuple[int, ...] = 200):
        return self._call("GET", "", params=params or {}, expected_status=expected_status)
