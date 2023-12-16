import pytest
from fastapi.testclient import TestClient
from Model_2 import app
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
    
    assert predictions["similarity_1"] == similarity_matrix[0][1] * 100
    assert predictions["similarity_2"] == similarity_matrix[0][2] * 100
