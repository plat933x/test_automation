import requests

ENDPOINT = "https://todo.pixegami.io"

response = requests.get(ENDPOINT)
data = response.json()
status = response.status_code

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def new_task_payload():
    return {
        "content": "test content to check",
        "user_id": "124.9.1b",
        "task_id": "TSKID-178",
        "is_done": False
    }
def test_endpoint_available():
    assert response
    assert status == 200

def test_create_task():
    payload = new_task_payload()
    create_response = create_task(payload)
    assert create_response.status_code == 200

    data = create_response.json()
    task_id = data["task"]["task_id"]

    get_response = update_task(task_id)
    assert get_response.status_code == 200

    get_response_data = get_response.json()
    assert get_response_data["content"] == payload["content"]
    assert get_response_data["user_id"] == payload["user_id"]