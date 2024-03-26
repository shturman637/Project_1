from skimage import io
import cv2
import matplotlib.pyplot as plt
from huggingface_hub import from_pretrained_keras

ROWS, COLS = 150, 150

model = from_pretrained_keras("carlosaguayo/cats_vs_dogs")

# Используем картинку по url
img_url = 'https://ichef.bbci.co.uk/news/640/cpsprodpb/42E2/production/\
    _96522171_gettyimages-450864271.jpg'

img = io.imread(img_url)
img = cv2.resize(img, (ROWS, COLS), interpolation=cv2.INTER_CUBIC)
img = img / 255.0
img = img.reshape(1, ROWS, COLS, 3)

# Предсказание результата моделью
prediction = model.predict(img)[0][0]
if prediction >= 0.5:
    print('I am {:.2%} sure this is a Cat'.format(prediction))
else:
    print('I am {:.2%} sure this is a Dog'.format(1-prediction))

plt.imshow(img[0], 'Blues')
plt.axis("off")
plt.show()
