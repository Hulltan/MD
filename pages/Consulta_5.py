from project import *

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

st.title("""Relação de desenpenho em matemática x outras áreas
        """)
st.write("""Este gráfico apresenta uma visualização em forma de dispersão (scatterplot) 
         das notas de Matemática em relação à nota escolhida pelo usuário (selecionada 
         através do widget na barra lateral) em uma determinada área do conhecimento. 
         O eixo x representa as notas da área selecionada e o eixo y representa as notas de Matemática. 
         As bolhas indicam cada estudante e seu respectivo desempenho nas duas notas 
         selecionadas. Além disso, ao passar o mouse sobre as bolhas, é possível ver as 
         informações das notas de ambas as áreas selecionadas e o ano em que o exame foi 
         realizado.
         """)

# Exibe o gráfico
st.altair_chart(grafico)
