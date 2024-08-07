import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Carregar os dados
dados = pd.read_csv('athlete_events.csv')

# Título da aplicação
st.title('Histograma de Idade dos Atletas')

# Exibir o DataFrame
st.write(dados.head())

# Criar o histograma
fig, ax = plt.subplots()
dados.hist(column='Age', bins=100, ax=ax)
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Histograma da Idade dos Atletas')

# Exibir o histograma
st.pyplot(fig)

# Criar o histograma
fig, ax = plt.subplots()
dados.hist(column='Weight', bins=100,ax=ax)
plt.xlabel('Peso')
plt.ylabel('Frequência')
plt.title('Histograma do Peso dos Atletas')
st.pyplot(fig)