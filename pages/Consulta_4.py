from project import *
consulta_4 = run_query("SELECT NU_NOTA_CH, NU_NOTA_CN, NU_NOTA_LC , NU_NOTA_MT, NU_NOTA_REDACAO , Tp_escola , MED_RENDA_MENSAL , Tp_Sexo , Tp_Cor_raca, Ano FROM enem_dw.fatoprova join (select id, Ano from dimdata) as sDAta join (select id, Tp_Sexo,Tp_escola,Tp_Cor_raca from dimparticipante) as part where fatoprova.dimLocalicadeFeito_id = part.id and fatoprova.dimData_id = sData.id and fatoprova.dimLocalicadeFeito_id = 1;")

columns= [ 'CH','CN','LC','MT','REDACAO','Tipo_de_escola','MED_RENDA_MENSAL','Sexo','Cor_Raca','ANO']


for row in consulta_4:
    st.write(f"{row}")