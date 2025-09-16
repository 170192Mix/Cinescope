from typing import Any, Dict, Optional, Iterable
from custom_requester.custom_requester import CustomRequester
from constants import API_BASE, MOVIES_ENDPOINT


def _join(base: str, path: str) -> str:
    base = base.rstrip("/")
    if not path:
        return base
    if not path.startswith("/"):
        path = "/" + path
    return base + path


class MoviesAPI(CustomRequester):
    def __init__(self, session, base_url: str = API_BASE, headers: Optional[Dict[str, str]] = None):
        super().__init__(session=session, base_url=base_url, headers=headers)
        self._base = MOVIES_ENDPOINT  # "/movies"

    def create_movie(self, payload: Dict[str, Any], expected_status: int | Iterable[int] = 201):
        return self.send_request("POST", _join(self._base, ""), json=payload, expected_status=expected_status)

    def get_movie(self, movie_id: str | int, expected_status: int | Iterable[int] = 200):
        return self.send_request("GET", _join(self._base, f"{movie_id}"), expected_status=expected_status)

    def patch_movie(self, movie_id: str | int, payload: Dict[str, Any], expected_status: int | Iterable[int] = 200):
        return self.send_request("PATCH", _join(self._base, f"{movie_id}"), json=payload, expected_status=expected_status)

    def put_movie(self, movie_id: str | int, payload: Dict[str, Any], expected_status: int | Iterable[int] = 200):
        return self.send_request("PUT", _join(self._base, f"{movie_id}"), json=payload, expected_status=expected_status)

    def delete_movie(self, movie_id: str | int, expected_status: int | Iterable[int] = (200, 204, 202)):
        return self.send_request("DELETE", _join(self._base, f"{movie_id}"), expected_status=expected_status)

    def list_movies(self, params: Optional[Dict[str, Any]] = None, expected_status: int | Iterable[int] = 200):
        return self.send_request("GET", _join(self._base, ""), params=params or {}, expected_status=expected_status)