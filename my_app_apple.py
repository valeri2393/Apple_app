import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Котировки компании Apple", page_icon=":chart_with_upwards_trend:", layout="wide")

st.title('Данные о котировках компании Apple')

# виджет для выбора количества дней для анализа данных (слайдер)
num_days = st.slider('Выберите количество дней для анализа данных', min_value=1, max_value=100, value=30, step=1)

# данные о котировках за выбранный период
apple_data = yf.download('AAPL', period=f'{num_days}d')

st.subheader('График')

# виджет для выбора графика
chart_type = st.selectbox('Выберите тип графика', ['Цена закрытия', 'Объем торгов'])

# вывести график в зависимости от выбранного типа
if chart_type == 'Цена закрытия':
    st.line_chart(apple_data['Close'])
elif chart_type == 'Объем торгов':
    st.line_chart(apple_data['Volume'])

st.subheader('Статистика по ценам акций')
st.write(apple_data.describe())

st.subheader('Последние данные')
st.write(apple_data.tail())

# виджеты для загрузки и выгрузки данных
st.subheader('Загрузка и выгрузка данных')

# Виджет для загрузки данных
uploaded_file = st.file_uploader("Выберите файл для загрузки", type=['csv', 'xlsx'])

if uploaded_file is not None:
    if uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)
    st.write(df)

# скачать данные
st.write(' ')
st.subheader('Скачать данные')
if st.button('Скачать данные в формате CSV'):
    apple_data.to_csv('apple_data.csv', index=False)
    st.download_button(label='Скачать CSV', data='apple_data.csv', file_name='apple_data.csv', mime='text/csv')
