from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pydantic import BaseModel

class ItemRequest(BaseModel):
    Text_source: str
    Text_1: str
    Text_2: str

class ItemResponse(BaseModel):
    Предложение_1: float
    Предложение_2: float

app = FastAPI()
@app.post("/predict/")

def predict(request: ItemRequest):
    """Данная модель сравнивает, введённые Вами предложения"""
    sentences = [request.Text_source, request.Text_1, request.Text_2]

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    embeddings = model.encode(sentences)

    similarity_matrix = cosine_similarity(embeddings, embeddings)

    return ItemResponse(
        Предложение_1=similarity_matrix[0][1] * 100,
        Предложение_2=similarity_matrix[0][2] * 100,
    )

