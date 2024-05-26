import streamlit as st
import pandas as pd
import sqlite3

# Подключение к SQLite
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Создание таблицы, если она еще не создана
c.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY,
        json_data TEXT
    )
''')

st.title("Загрузка данных в SQLite")

uploaded_file = st.file_uploader("Загрузите файл Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Предпросмотр данных:", df)

    if st.button("Сохранить в SQLite"):
        # Очистить существующие данные
        c.execute('DELETE FROM data')
        conn.commit()

        # Сохранить данные в SQLite
        for i, row in df.iterrows():
            c.execute('INSERT INTO data (json_data) VALUES (?)', (row.to_json(),))
        conn.commit()

        st.success("Данные успешно сохранены в SQLite")
