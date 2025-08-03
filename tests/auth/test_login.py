from fastapi.testclient import TestClient 
from  app.main import app


client = TestClient(app)

def test_login_endpoint():
    response = client.post("/auth/login", data={"username": "john", "password": "123"})
    assert response.status_code == 200
    assert response.json() == {
        "name": "john@gmail.com",
        "token": "token"
    }
