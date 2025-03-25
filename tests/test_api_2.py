import pytest, requests

# open source test API url
ENDPOINT = "https://jsonplaceholder.typicode.com"

@pytest.mark.parametrize("extension", ['/comments', '/posts', '/users'])
def test_get_status_code(extension):
    response = requests.get(ENDPOINT + extension)

    assert response.status_code == 200, f"Could not retrieve data from {extension} with code: {response.status_code}"

@pytest.mark.parametrize("extension", ['/comments?postId=1', '/posts?postId=1', '/users?postId=1'])
def test_get_comments_id(extension):
    response = requests.get(ENDPOINT + extension)

    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert response.status_code == 200, f"Could not retrieve data from {extension} with code: {response.status_code}"