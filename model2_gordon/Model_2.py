import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

#Создание заголовка 
st.title('Сравнение текстов предложений')

#Вводим предложения, которые будут сравниваться с Главным:
Text_source = st.text_input('Главное предложение: ')
Text_1 = st.text_input('Предложение 1: ')
Text_2 = st.text_input('Предложение 2: ')

sentences = [Text_source, Text_1, Text_2]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
#Находим косинусное сходство, для удобной интерпретации сходства:
similarity_matrix = cosine_similarity(embeddings, embeddings)

#Отображаем по 100-бальной шкале степень сходства предложений относительно Главного:
st.write('Предложение 1: ', similarity_matrix[0][1]*100)
st.write('Предложение 2: ', similarity_matrix[0][2]*100)
