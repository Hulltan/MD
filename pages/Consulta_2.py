from project import *

consulta_2 = run_query("SELECT ANO as Anos, count(dimParticipante_id) as Paticipantes, MED_RENDA_MENSAL as Media_Renda_Mensal FROM enem_dw.fatoprova join (select id, ANO from dimdata) as sData where fatoprova.dimData_id = sData.id and fatoprova.dimLocalicadeFeito_id = 1 and MED_RENDA_MENSAL > 0 group by Anos, MED_RENDA_MENSAL;")
columns = ['Ano', 'Quantidade_de_Participante_por_Renda_Mensal', 'Media_Renda_Mensal']
dados = create_dataframe(consulta_2, columns)
chart = alt.Chart(dados).mark_circle().encode(x='Ano', y='Media_Renda_Mensal', size='Quantidade_de_Participante_por_Renda_Mensal')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)
# Mostra o gráfico no Streamlit
st.altair_chart(chart)
st.write(dados)
