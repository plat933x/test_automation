import requests, pytest

URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.parametrize("endpoint", ["/users", "/comments"])
def test_response_time(endpoint):
    response = requests.get(URL + endpoint)
    response_time = response.elapsed.total_seconds()

    print(f"Response_time for {endpoint}: {response_time}")

    assert response_time < .5, f"Response time too long!"