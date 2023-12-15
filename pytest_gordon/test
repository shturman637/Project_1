import requests
import pytest
from fastapi.testclient import TestClient
from Model_2 import app 

client = TestClient(app)

def test_predict_endpoint():
    test_data = {
        "Text_source": "Home",
        "Text_1": "Home",
        "Text_2": "Home"
    }
    response = client.post("/predict/", json=payload)
    assert response.status_code == 200
    assert result['Предложение_1'] > 99
    assert result['Предложение_2'] > 99
