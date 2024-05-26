import streamlit as st
import pandas as pd
import sqlite3
import json

# Подключение к SQLite
conn = sqlite3.connect('data.db')
c = conn.cursor()

st.title("Обработка данных из SQLite")

# Загрузить данные из SQLite
c.execute('SELECT json_data FROM data')
rows = c.fetchall()
data = [json.loads(row[0]) for row in rows]
df = pd.DataFrame(data)

if not df.empty:
    st.write("Данные из SQLite:", df)

    # Пример фильтрации данных
    columns = df.columns.tolist()
    filter_column = st.selectbox("Выберите столбец для фильтрации", columns)
    filter_value = st.text_input("Введите значение для фильтрации")

    if st.button("Фильтровать"):
        filtered_df = df[df[filter_column].astype(str).str.contains(filter_value, na=False)]
        st.write("Отфильтрованные данные:", filtered_df)
else:
    st.warning("Данные в SQLite отсутствуют. Пожалуйста, загрузите данные через первое приложение.")
