from project import *

consulta_2 = run_query("SELECT ANO as Anos, count(dimParticipante_id) as Paticipantes, MED_RENDA_MENSAL as Media_Renda_Mensal FROM enem_dw.fatoProva join (select id, ANO from dimData) as sData where fatoProva.dimData_id = sData.id and fatoProva.dimLocalicadeFeito_id = 1 and MED_RENDA_MENSAL > 0 group by Anos, MED_RENDA_MENSAL;")
columns = ['Ano', 'Quantidade_de_Participante_por_Renda_Mensal', 'Media_Renda_Mensal']

dados = create_dataframe(consulta_2, columns=columns).sort_values(by="Media_Renda_Mensal",ascending=True)
dados['Media_Renda_Mensal'] = dados['Media_Renda_Mensal'].apply(str)

chart = (
            alt.Chart(dados)
            .mark_line(opacity=0.3)
            .encode(
                x="Ano",
                y="Quantidade_de_Participante_por_Renda_Mensal",
                color="Media_Renda_Mensal",
            )
        )
st.title('Número de participantes x renda')
st.write("""O gráfico exibe a quantidade de participantes do ENEM por ano e 
         faixa de renda mensal em que se encaixam. Cada cor no gráfico representa uma faixa de renda mensal, 
         e no eixo y é exibida a quantidade de participantes do ENEM nessa faixa de renda 
         para cada ano.""")
st.altair_chart(chart, use_container_width=True)
st.write(dados)
