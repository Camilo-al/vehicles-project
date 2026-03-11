import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vehicles App", layout="wide")

st.title(" Vehicles Data Explorer")

car_data = pd.read_csv('data/vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão

 #-------       
if hist_button: # se o botão for clicado
            # escrever uma mensagem
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
            fig = px.histogram(car_data, x="odometer")
        
            # exibir um gráfico Plotly interativo
            st.plotly_chart(fig, use_container_width=True)

 # criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')
if build_histogram:
        # escrever uma mensagem
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            # criar um histograma
            fig = px.histogram(car_data, x="odometer")
        
            # exibir um gráfico Plotly interativo
            st.plotly_chart(fig, use_container_width=True)



#--------


# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/vehicles.csv")

df = load_data()

st.subheader("Dataset")
st.dataframe(df)

# Price distribution
st.subheader("Distribuição de Preços")
fig_price = px.histogram(df, x="price", nbins=50, title="Distribuição de Preços")
st.plotly_chart(fig_price, use_container_width=True)

# Scatter: price vs odometer
st.subheader("Preço vs Quilometragem")
fig_scatter = px.scatter(
    df,
    x="odometer",
    y="price",
    color="condition",
    title="Preço vs Quilometragem por Condição"
)
st.plotly_chart(fig_scatter, use_container_width=True)
