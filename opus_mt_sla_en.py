from transformers import pipeline
import streamlit as st

st.title('Переводчик со славянских языков на английский')
Text_source = st.text_input('Введите текст: ')

@st.cache(allow_output_mutation=True)
def translate_model():
    classifier = pipeline("translation", model="Helsinki-NLP/opus-mt-sla-en")
    classifier(Text_source)
    return translate_model

st.write('Перевод: ', translate_model)
