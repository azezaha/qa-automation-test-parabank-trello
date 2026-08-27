import os
import requests
import pytest
from dotenv import load_dotenv
from jsonschema import validate

load_dotenv()

BASE_URL = "https://api.trello.com/1"
API_KEY = os.getenv("TRELLO_API_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")

AUTH_PARAMS = {
    "key": API_KEY,
    "token": TOKEN
}

BOARD_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "closed": {"type": "boolean"},
        "url": {"type": "string"}
    },
    "required": ["id", "name", "closed"]
}


@pytest.fixture(scope="module")
def created_board():
    url = f"{BASE_URL}/boards/"
    params = {**AUTH_PARAMS, "name": "QA_Automation_Board_Test"}
    response = requests.post(url, params=params)
    assert response.status_code == 200
    board_data = response.json()
    board_id = board_data["id"]

    yield board_data

    delete_url = f"{BASE_URL}/boards/{board_id}"
    requests.delete(delete_url, params=AUTH_PARAMS)


def test_get_board_positive_schema_and_performance(created_board):
    """Positive Flow: Validasi Status 200, Data Value, JSON Schema, & Response Time < 1000ms"""
    board_id = created_board["id"]
    url = f"{BASE_URL}/boards/{board_id}"
    
    response = requests.get(url, params=AUTH_PARAMS)
    
    # 1. Assert Status Code & Value
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "QA_Automation_Board_Test"
    
    # 2. Schema Validation
    validate(instance=data, schema=BOARD_SCHEMA)
    
    # 3. Performance Check (< 1000ms)
    elapsed_ms = response.elapsed.total_seconds() * 1000
    assert elapsed_ms < 1000, f"API response time exceeds limit: {elapsed_ms}ms"


def test_create_list_in_board_positive(created_board):
    """Positive Flow: Membuat List baru di dalam Board"""
    board_id = created_board["id"]
    url = f"{BASE_URL}/lists"
    params = {**AUTH_PARAMS, "name": "Sprint Backlog", "idBoard": board_id}
    
    response = requests.post(url, params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Sprint Backlog"
    assert data["idBoard"] == board_id


def test_get_board_invalid_api_key_negative(created_board):
    """Negative Flow: Validasi penolakan akses (401 Unauthorized) jika API Key salah"""
    board_id = created_board["id"]
    url = f"{BASE_URL}/boards/{board_id}"
    bad_params = {"key": "invalid_key_12345", "token": TOKEN}
    
    response = requests.get(url, params=bad_params)
    assert response.status_code == 401
    assert "invalid key" in response.text.lower()


def test_create_board_missing_required_name_negative():
    """Negative Flow: Validasi error 400 Bad Request jika parameter wajib 'name' kosong"""
    url = f"{BASE_URL}/boards/"
    params = {**AUTH_PARAMS, "name": ""}
    
    response = requests.post(url, params=params)
    assert response.status_code == 400