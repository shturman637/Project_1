from fastapi import FastAPI, UploadFile, HTTPException
from PIL import Image
from skimage import io
import cv2
import matplotlib.pyplot as plt
from huggingface_hub import from_pretrained_keras
import io

class ItemResponse():
    result: str

app = FastAPI()

@app.post("/recognize")
async def recognize(file: UploadFile):

        image_data = file.file.read()
        img_pil = Image.open(io.BytesIO(image_data))

        if img_pil is not None:
            model = from_pretrained_keras("carlosaguayo/cats_vs_dogs")

            ROWS, COLS = 150, 150
            img = io.imread(io.BytesIO(image_data))
            img_resized = cv2.resize(img, (ROWS, COLS), interpolation=cv2.INTER_CUBIC)
            img_resized = img_resized / 255.0
            img_resized = img_resized.reshape(1, ROWS, COLS, 3)

            prediction = model.predict(img_resized)[0][0]

            if prediction >= 0.5:
                result = 'I am {:.2%} sure this is a Cat'.format(prediction)
            else:
                result = 'I am {:.2%} sure this is a Dog'.format(1 - prediction)

            plt.imshow(img_resized[0], 'Blues')
            plt.axis("off")
            plt.show()

            return ItemResponse(result=result)

