from project import *
dicionary = {
    1:'Não Respondeu',
    2:'Pública',
    3:'Privada',
    4:'Exterior'
} 
consulta_3 = run_query("SELECT avg(NU_NOTA_CH) as CH, avg(NU_NOTA_CN) as CN, avg(NU_NOTA_LC) as LC, avg(NU_NOTA_MT) as MT, avg(NU_NOTA_REDACAO) as REDACAO, ANO as Anos, tp_escola as Tipo_de_escola, count(tp_escola) as Participante_por_tipo_de_escola FROM enem_dw.fatoprova join (select id, ANO from dimdata) as sData join (select id, TP_ESCOLA from dimparticipante) as part where fatoprova.dimData_id = sData.id and fatoprova.dimLocalicadeFeito_id = 1 and fatoprova.dimParticipante_id = part.id group by Anos, Tipo_de_escola;")
columns= [ 'CH','CN','LC','MT','REDACAO','ANO','Tipo_de_escola','Participante_por_tipo_de_escola']



for row in consulta_3:
    st.write(f"{row}")