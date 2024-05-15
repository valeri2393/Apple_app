import streamlit as st
import yfinance as yf

#метод st.set_page_config() устан конфигурацию для приложения
#заголовок страницы (page_title)
#иконка страницы (page_icon) 
#раскладка страницы (layout) 
st.set_page_config(page_title="Котировки компании Apple", page_icon=":chart_with_upwards_trend:", layout="wide")



# Заголовок приложения
st.title('Данные о котировках компании Apple')

# Получаем данные о котировках компании Apple
apple_data = yf.download('AAPL')

# график цены закрытия акций
st.subheader('График цены закрытия')    #подзаголовок на странице приложения
st.line_chart(apple_data['Close'])   #график на странице приложения

# Отображаем статистику по ценам акций
st.subheader('Статистика по ценам акций')

#выводим данные на страницу приложения
st.write(apple_data.describe())     #метод describe() - статистика по ценам

# Отображаем последние несколько строк данных
st.subheader('Последние данные')
st.write(apple_data.tail())     #метод tail() - отображает последние несколько строк данных

st.subheader('Графики цен открытия и закрытия')
st.line_chart(apple_data[['Open', 'Close']])
st.subheader('График объема торгов')
st.line_chart(apple_data['Volume'])



