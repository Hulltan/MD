from project import *


consulta_3 = run_query("SELECT avg(NU_NOTA_CH) as CH, avg(NU_NOTA_CN) as CN, avg(NU_NOTA_LC) as LC, avg(NU_NOTA_MT) as MT, avg(NU_NOTA_REDACAO) as REDACAO, ANO as Anos, tp_escola as Tipo_de_escola, count(tp_escola) as Participante_por_tipo_de_escola FROM enem_dw.fatoprova join (select id, ANO from dimdata) as sData join (select id, TP_ESCOLA from dimparticipante) as part where fatoprova.dimData_id = sData.id and fatoprova.dimLocalicadeFeito_id = 1 and fatoprova.dimParticipante_id = part.id group by Anos, Tipo_de_escola;")
columns= [ 'CH','CN','LC','MT','REDACAO','Anos','Tipo_de_escola','Participante_por_tipo_de_escola']
dataFrame = create_dataframe(consulta_3, columns=columns).sort_values(by="Tipo_de_escola",ascending=True)

cores = {
    'CH': 'blue',
    'CN': 'red',
    'LC': 'green',
    'MT': 'orange',
    'REDACAO': 'purple'
}
notas = ['CH', 'CN', 'LC', 'MT', 'REDACAO']
opcoes_notas = st.multiselect('Selecionar notas:', notas, default=notas)
colunas = opcoes_notas + ['Tipo_de_escola', 'Anos']

df_filtrado = dataFrame[colunas]

df_melted = pd.melt(df_filtrado, id_vars=['Tipo_de_escola', 'Anos'], value_vars=opcoes_notas, var_name='AREA', value_name='NOTA')

df_melted['NOTA'] = pd.to_numeric(df_melted['NOTA'], errors='coerce')


min_nota = df_melted['NOTA'].min()
max_nota = df_melted['NOTA'].max()

chart = alt.Chart(df_melted).mark_line().encode(
    x='Anos',
    y=alt.Y('NOTA:Q', scale=alt.Scale(zero=False, nice=False)),
    color='AREA:N',
    strokeDash='AREA:N'
)
st.title('Gráfico de notas por área e tipo de escola ')
st.write("""Este gráfico mostra a média das notas de cada área (Ciências Humanas, 
         Ciências da Natureza, Linguagens e Códigos, Matemática e Redação) por ano 
         e por tipo de escola (pública ou privada). As áreas selecionadas estão destacadas 
         em cores diferentes e podem ser escolhidas usando o menu suspenso 'Selecionar 
         notas'.""")
st.altair_chart(chart, use_container_width=True)
st.table(dataFrame)

