from Project import *


consulta_1 = run_query("SELECT count(dimParticipante_id) as Paticipantes, ANO as Anos FROM enem_dw.fatoProva join (select id, ANO from dimData) as sData where fatoProva.dimData_id = sData.id and fatoProva.dimLocalicadeFeito_id = 1 group by Anos;")
columns = ['Participante', 'Ano']
dataFrame = create_dataframe(consulta_1, columns)
st.title('Quantidade de participantes por Ano')
st.bar_chart(data=dataFrame, x='Ano', y='Participante')

st.write(dataFrame)