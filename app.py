import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

car_data = pd.read_csv("vehicles_us.csv")

st.header("Proyecto ventas automoviles USA")
# st.set_page_config(page_title="proyecto ventas",layout="wide")

# st.title("proyecto ventas")

# st.dataframe(data)  # objeto para visualizar dataframes
# Creacion de boton en la aplicacion de streamlit
# hist_buttoon = st.button('Construir histograma')
checkbox_hist = st.checkbox('Mostrar histograma del odometro')
checkbox_scatter = st.checkbox(
    'Mostrar grafico de dispersion odometro vs precio')

# Logica a ejecutar cuando se presiona el boton
if checkbox_hist:
    # Escribir mensaje en la aplicacion
    st.write('Creación de conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacia y luego se añade un rastro histograma
    fig = go.Figure(data=go.Histogram(x=car_data['odometer']))

    # Titulo del grafico
    fig.update_layout(title_text='Distribución del Odometro')

    # Mostrar el graficocon streamlit
    # 'use_container_width=True' hace que el grafico ocupe todo el ancho disponible
    st.plotly_chart(fig, use_container_width=True)

# scatter_button = st.button('Construir grafico de dispersión')

if checkbox_scatter:
    # Mensaje de la aplicacion
    st.write('Grafico de dispersión entre odometro y precio')
    # Crear un grafico de dispersion utilizando plotly.graph_objects
    # Se crea una figura vacia y luego se añade un rastro de dispersion
    fig_s = go.Figure(data=go.Scatter(
        x=car_data['odometer'], y=car_data['price'], mode='markers'))

    # Titulo del grafico
    fig_s.update_layout(title_text='Relacion entre Odometro y Precio')

    # Mostrar el grafico con streamlit
    st.plotly_chart(fig_s, use_container_width=True)
