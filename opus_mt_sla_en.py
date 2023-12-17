from transformers import pipeline
import streamlit as st

# Установка фоновой картинки через CSS
st.markdown(
    """
    <style>
        body {
            background-image: url('https://img.freepik.com/free-vector/neon-lights-background-theme_52683-44625.jpg?w=740&t=st=1702773847~exp=1702774447~hmac=3b762aefe8ac580565d6ebf413b435d78d9e72aa030674d043d18e48fab382b3.jpg');
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

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
