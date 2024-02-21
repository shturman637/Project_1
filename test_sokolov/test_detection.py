import pytest # noqa: F401
from fastapi.testclient import TestClient
from detection_fast import app

client = TestClient(app)


def test_predict_joy():
    response = client.post("/predict/", json={
        "text": "смотрю фотки,все  такие смешные "})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'joy'


def test_predict_sadness():
    response = client.post("/predict/",
                           json={"text": "Как хочется кому-то уткнуться в \
                                        плечо, высказаться и поплакать?"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'sadness'


def test_predict_surprise():
    response = client.post("/predict/", json={
        "text": "Сходство просто поразительное, сэр."})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'surprise'


def test_predict_fear():
    response = client.post("/predict/", json={"text": "Опять чудовища"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'fear'


def test_predict_anger():
    response = client.post("/predict/",
                           json={"text": "Люди разгневаны тем, что этот \
                                 хулиган и его друг считают смешным и \
                                 безобидным"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'anger'


def test_predict_no_emotion():
    response = client.post("/predict/",
                           json={"text": "Те самые плантации странных пальм ."}
                           )
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'no_emotion'
