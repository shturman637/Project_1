import pytest
import httpx
from fastapi.testclient import TestClient
from Fastapi_catsvsdogs import app

@pytest.fixture
def client():
    return TestClient(app)

def test_cats(client):

    with open("https://koshka.top/uploads/posts/2023-10/1696329610_koshka-top-p-malie-koshki-67.jpg", "rb") as img_file:
        files = {"file": ("https://koshka.top/uploads/posts/2023-10/1696329610_koshka-top-p-malie-koshki-67.jpg", img_file, "image/jpeg")} 
        response = client.post("/recognize", files=files)
    assert response.status_code == 200
    assert "I am" in response.json()["cat"]
def test_dogs(client):

    with open("https://gas-kvas.com/grafic/uploads/posts/2023-10/1696601772_gas-kvas-com-p-kartinki-s-sobakami-22.jpg", "rb") as img_file: 
        files = {"file": ("https://gas-kvas.com/grafic/uploads/posts/2023-10/1696601772_gas-kvas-com-p-kartinki-s-sobakami-22.jpg", img_file, "image/jpeg")} 
        response = client.post("/recognize", files=files)

    assert response.status_code == 200
    assert "I am" in response.json()["dog"]
