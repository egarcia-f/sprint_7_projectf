import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('CARROS')
st.dataframe(df)

button_hist = st.button('Construir Histograma')

if button_hist:
    st.write('Creación de histograma para el conjunto de datos de anuncio de coches')

    fig = px.histogram(df, x='odometer')  # Crear Histograma
    st.plotly_chart(fig, use_container_width=True)

button_scatter = st.button('Construir Scatter Plot')

if button_scatter:
    st.write('Creando Scatter Plot')

    fig1 = px.scatter(df, x='model_year', y='price')
    st.plotly_chart(fig1, use_container_width=True)
