import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

# Histogram
# Qual o desempenho dos estudantes
# em cada faixa de renda nos bairros do Recife e como isso mudou ao longo dos anos?

@st.cache_data
def load_data(nrows):
    data = pd.read_csv('C:/Users/vicen/Downloads/pokemon.csv', nrows=nrows)
    return data

st.write("## Consulta 2")
st.write('##### Descrição')

# Load 10,000 rows of data into the dataframe.
df = load_data(10000)
type = df['typing'].value_counts(normalize=True) * 100
st.bar_chart(type)