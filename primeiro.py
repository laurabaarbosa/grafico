import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
st.title("Gerar Gráfico a Partir de Arquivo CSV")
df = pd.read_csv('https://perfil-i.ibict.br/media/uploads/user_sum.csv')
st.subheader("Dados Carregados")
st.write(df.head())

colunas = df.columns.tolist()
    x_col = st.selectbox("Escolha a coluna para o eixo X (categorias)", colunas)
    y_col = st.selectbox("Escolha a coluna para o eixo Y (valores)", colunas)

st.subheader("Gráfico de Barras")
    st.bar_chart(data=df, x=x_col, y=y_col, use_container_width=True)
