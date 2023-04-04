from Project import *

# Carrega os dados do ENEM
consulta_5 = run_query("SELECT DD.ANO, NU_NOTA_CN, NU_NOTA_MT, NU_NOTA_CH, NU_NOTA_LC FROM enem_dw.fatoProva AS FP JOIN enem_dw.dimData AS DD ON DD.id=FP.dimData_id JOIN enem_dw.dimParticipante AS DP ON DP.id=FP.dimParticipante_id;")
df = create_dataframe(consulta_5, ["ANO", "NU_NOTA_CN", "NU_NOTA_MT", "NU_NOTA_CH", "NU_NOTA_LC"])

# Cria um widget de seleção do ano e da matéria
anos = sorted(df['ANO'].unique())
ano_selecionado = st.sidebar.selectbox('Selecione um ano', anos)

materias = ["NU_NOTA_CN", "NU_NOTA_MT", "NU_NOTA_CH", "NU_NOTA_LC"]
materia_selecionada = st.sidebar.selectbox('Selecione uma matéria', materias)

# Filtra o dataframe pelo ano e matéria selecionados
df_filtrado = df[(df['ANO'] == ano_selecionado) & (df[materia_selecionada].notnull())]

# Cria o gráfico
grafico = alt.Chart(df_filtrado).mark_circle(size=60).encode(
    x=alt.X(materia_selecionada, title=materia_selecionada.split("_")[2].title()),
    y=alt.Y('NU_NOTA_MT', title='Matemática'),
    tooltip=[materia_selecionada, 'NU_NOTA_MT']
).interactive()

# Exibe o gráfico
st.altair_chart(grafico)
