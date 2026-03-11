import streamlit as st
import pandas as pd
import plotly.express as px

st.title(" Vehicles Data Explorer")

# Carregar dados
df = pd.read_csv("data/vehicles.csv")

st.write("### Dataset")
st.dataframe(df)

st.write("### Escolha os gráficos que deseja visualizar")

# Checkbox 1 — Histograma
if st.checkbox("Mostrar histograma de preços"):
    fig = px.histogram(df, x="price", nbins=50, title="Distribuição dos Preços")
    st.plotly_chart(fig)

# Checkbox 2 — Scatter Plot
if st.checkbox("Mostrar gráfico de dispersão (Preço vs Quilometragem)"):
    fig = px.scatter(df, x="odometer", y="price",
                     title="Preço vs Quilometragem",
                     opacity=0.6)
    st.plotly_chart(fig)

# Checkbox 3 — Boxplot
if st.checkbox("Mostrar boxplot por condição"):
    fig = px.box(df, x="condition", y="price",
                 title="Preço por Condição do Veículo")
    st.plotly_chart(fig)

# Checkbox 4 — Bar Chart
if st.checkbox("Mostrar gráfico de barras (Contagem por tipo de combustível)"):
    fuel_counts = df["fuel"].value_counts().reset_index()
    fuel_counts.columns = ["fuel", "count"]

    fig = px.bar(fuel_counts, x="fuel", y="count",
                 title="Número de Veículos por Tipo de Combustível")
    st.plotly_chart(fig)
