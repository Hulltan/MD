import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import mysql.connector
import plotly.graph_objs as go
import plotly.express as px

@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def create_dataframe(data, columns):
    return pd.DataFrame(data, columns=columns)

st.write("# Dados ENEM")
st.markdown("""Selecione uma das consultas ao lado para visualizar 
            informações sobre dados do ENEM realizados entre 2019 e 2021""")


