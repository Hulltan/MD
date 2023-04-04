from project import *

# Carrega os dados do ENEM
consulta_4 = run_query("SELECT DD.ANO, DP.NU_INSCRICAO, DLF.CO_MUNICIPIO_PROVA, NU_NOTA_CN, NU_NOTA_CH, NU_NOTA_LC, NU_NOTA_MT, NU_NOTA_REDACAO FROM enem_dw.fatoProva AS FP  JOIN enem_dw.dimData AS DD ON DD.id=FP.dimData_id JOIN enem_dw.dimParticipante AS DP ON DP.id=FP.dimParticipante_id JOIN enem_dw.dimLocalicadeFeito AS DLF ON DLF.id=FP.dimLocalicadeFeito_id;")
df = create_dataframe(consulta_4, columns=['ano', 'inscricao', 'co_municipio_prova', 'nota_cn', 'nota_ch', 'nota_lc', 'nota_mt', 'nota_redacao'])

# Define o título da página
st.title('Análise das notas por Escola')

# Filtra os dados pela escola selecionada
escola = st.selectbox('Selecione uma escola', df['co_municipio_prova'].unique())
dados_escola = df[df['co_municipio_prova'] == escola]

# Plota o gráfico com as notas
fig = px.box(dados_escola, x='ano', y=['nota_cn', 'nota_ch', 'nota_lc', 'nota_mt'], 
            labels={'variable': 'Área de conhecimento', 'value': 'Nota', 'ano': 'Ano'})
st.plotly_chart(fig)