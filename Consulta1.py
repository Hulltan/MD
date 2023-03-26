import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

# Histogram
# Qual é a taxa de participação no ENEM em cada bairro do Recife
# e como isso mudou ao longo dos anos?

@st.cache_data
def load_data(nrows):
    data = pd.read_csv('C:/Users/vicen/Downloads/pokemon.csv', nrows=nrows)
    return data

st.write("## Consulta 1")
st.write('##### Descrição')

# Load 10,000 rows of data into the dataframe.
df = load_data(10000)
labels = list(df['typing'])
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

ax.pie(df['pokedex_number'], labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
#ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig)


# Add a selectbox to the sidebar:
#selectbox = st.sidebar.selectbox(
#    'How would you like to be contacted?',  - title
#    ('Email', 'Home phone', 'Mobile phone') - options
#)


# Add a slider to the sidebar:
#slider = st.sidebar.slider(
#    'Select a range of values', - title
#    0.0, 100.0, (25.0, 75.0)    - min, max, default select range()
#)