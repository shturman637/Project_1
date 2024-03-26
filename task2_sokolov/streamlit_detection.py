import base64
import streamlit as st
from transformers import pipeline

st.title("Приложение для определения эмоциональной окраски введенного текста")

# Инициализация модели
classifier = pipeline("sentiment-analysis", "cointegrated/rubert-tiny2-cedr-emotion-detection")

# Поле для ввода текста
text = st.text_input("Введите текст для анализа")

if st.button("Анализировать текст"):
    result = classifier(text)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        st.success(f'{label} sentiment (score: {score})')
    else:
        st.error(f'{label} sentiment (score: {score})')


# Устанавливаем фон

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_background('./images/file5.png')
