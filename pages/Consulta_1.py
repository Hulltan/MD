from project import *


consulta_1 = run_query("SELECT count(dimParticipante_id) as Paticipantes, ANO as Anos FROM enem_dw.fatoprova join (select id, ANO from dimdata) as sData where fatoprova.dimData_id = sData.id and fatoprova.dimLocalicadeFeito_id = 1 group by Anos;")
columns = ['Participante', 'Ano']
dataFrame = pd.DataFrame(consulta_1, columns=columns)
st.title('Quantidade de participantes por Ano')
st.bar_chart(data=dataFrame, x='Ano', y='Participante')

st.write(dataFrame)