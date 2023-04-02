from project import *

consulta_2 = run_query("SELECT count(dimParticipante_id) as Paticipantes, ANO as Anos, MED_RENDA_MENSAL as Media_Renda_Mensal FROM enem_dw.fatoprova join (select id, ANO from dimdata) as sData where fatoprova.dimData_id = sData.id and fatoprova.dimLocalicadeFeito_id = 1 and MED_RENDA_MENSAL > 0 group by Anos, MED_RENDA_MENSAL;")
columns = ['Quantidade_de_Participante_por_Renda_Mensal', 'Ano','Media_Renda_Mensal']
dados = pd.DataFrame(consulta_2, columns=columns)
chart = (
            alt.Chart(dados)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
st.altair_chart(chart, use_container_width=True)


# Mostra o gráfico no Streamlit
st.line_chart(data=dados, x='Media_Renda_Mensal', y=['Ano'])
st.write(dados)