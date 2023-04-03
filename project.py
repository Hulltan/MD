import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import mysql.connector
import altair as alt


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

# Histogram
# Qual é a taxa de participação no ENEM em cada bairro do Recife
# e como isso mudou ao longo dos anos?

