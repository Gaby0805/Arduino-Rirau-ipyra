from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "availability": True
    }