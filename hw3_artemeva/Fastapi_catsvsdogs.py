from fastapi import FastAPI
from skimage import io
import cv2
import matplotlib.pyplot as plt
from huggingface_hub import from_pretrained_keras
from pydantic import BaseModel

class ItemRequest(BaseModel):
    img_url: str

class ItemResponse(BaseModel):
    prediction: float

app = FastAPI()
@app.post("/predict/")

def predict(request: ItemRequest):
    model = from_pretrained_keras("carlosaguayo/cats_vs_dogs")
    ROWS, COLS = 150, 150
    img_url = request.img_url

    img = io.imread(img_url)
    img = cv2.resize(img, (ROWS, COLS), interpolation=cv2.INTER_CUBIC)
    img = img / 255.0
    img = img.reshape(1,ROWS,COLS,3)

    prediction = model.predict(img)[0][0]
        
    if prediction >= 0.5:
        result = 'I am {:.2%} sure this is a Cat'.format(prediction)
    else:
        result = 'I am {:.2%} sure this is a Dog'.format(1 - prediction)
    plt.imshow(img[0], 'Blues')
    plt.axis("off")
    plt.show()

    return ItemResponse(prediction=prediction, result=result)
