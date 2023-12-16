import pytest
from Model_3 import app
from fastapi.testclient import TestClient
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

client = TestClient(app)

def test_predict_endpoint():

    test_data = {
        "Text_source": "Home",
        "Text_1": "Home",
        "Text_2": "Home"
    }
    
    sentences = [test_data["Text_source"], test_data["Text_1"], test_data["Text_2"]]
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    similarity_matrix = cosine_similarity(embeddings, embeddings)

    response = client.post("/predict/", json=test_data)

    assert response.status_code == 200
    
    predictions = response.json()
    
    assert "Предложение_1" in predictions
    assert "Предложение_2" in predictions

    assert predictions["Предложение_1"] == similarity_matrix[0][1] * 100
    assert predictions["Предложение_2"] == similarity_matrix[0][2] * 100
