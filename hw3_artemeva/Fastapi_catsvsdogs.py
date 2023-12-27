from fastapi import FastAPI, UploadFile
from PIL import Image
from skimage import io
import cv2
import matplotlib.pyplot as plt
from huggingface_hub import from_pretrained_keras

class ItemResponse():
    result: str

app = FastAPI()
@app.post("/recognize")
async def recognize(file: UploadFile):
    image_data = file.file.read()
    img = Image.open(io.BytesIO(image_data))
    img = list()
    
    if img is not None:
        model = from_pretrained_keras("carlosaguayo/cats_vs_dogs")
        
        ROWS, COLS = 150, 150
        img = io.imread(io.BytesIO(image_data))
        img = cv2.resize(img, (ROWS, COLS), interpolation=cv2.INTER_CUBIC)
        img = img / 255.0
        img = img.reshape(1, ROWS, COLS, 3)

        prediction = model.predict(img)[0][0]
        
        if prediction >= 0.5:
            result = 'I am {:.2%} sure this is a Cat'.format(prediction)
        else:
            result = 'I am {:.2%} sure this is a Dog'.format(1 - prediction)

        plt.imshow(img[0], 'Blues')
        plt.axis("off")
        plt.show()

    return ItemResponse(result=result)