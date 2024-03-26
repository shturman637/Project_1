from transformers import pipeline
import streamlit as st

# Установка конфигурации страницы
st.set_page_config(
    page_title="Переводчик со славянских языков на английский",
    page_icon="🧊")

# Содержание страницы
st.title('Переводчик со славянских языков на английский')
Text_source = st.text_input('Введите текст: ')

# Отображение собственного сообщения вместо "Running translate_model(...)."
if st.button('Перевести'):
    st.text('Выполняется перевод...')

if Text_source:

    @st.cache(allow_output_mutation=True, show_spinner=False)
    def translate_model(Text_source):
        classifier = pipeline("translation", model="Helsinki-NLP/opus-mt-sla-en")
        translation_result = classifier(Text_source, max_length=50)
        return translation_result[0]['translation_text']

    translation = translate_model(Text_source)

    # Вывод результата
    st.success('Перевод выполнен успешно!')
    st.write('Перевод:', translation)
