import pytest
import requests

# Фикстура для базового URL
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

# Тестовый метод
def test_get_post(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

