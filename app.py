import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Encabezado
st.header('Aplicación de Vehículos Usados')
          
hist_button = st.button ('construir hostograma') #crear el botón
          
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
            
# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    # Mostrar mensaje
    st.write('Construir un gráfico de dispersión para las columnas "odometer" y "price"')
    
    # Crear el gráfico de dispersión
    fig_2 = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar gráfico interactivo
    st.plotly_chart(fig_2, use_container_width=True)
