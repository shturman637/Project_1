from transformers import pipeline
import streamlit as st

st.title('Переводчик со славянских языков на английский')
Text_source = st.text_input('Введите текст: ')

@st.cache(allow_output_mutation=True)
def translate_model(Text_source):
    classifier = pipeline("translation", model="Helsinki-NLP/opus-mt-sla-en")
    translation_result = classifier(Text_source, max_length=50)
    return translation_result[0]['translation_text']

if Text_source:
    translation = translate_model(Text_source)
    st.write('Перевод:', translation)
