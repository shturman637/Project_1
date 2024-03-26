from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis", "cointegrated/rubert-tiny2-cedr-emotion-detection")


@app.post("/predict/")
def predict(item: Item):
    """модель показывает эмоциональную окраску текста"""
    return classifier(item.text)[0]
