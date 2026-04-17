import streamlit as st

st.set_page_config(page_title = 'Disciplinas', page_icon = '📚')

st.title('Gestão de Disciplinas')

tab_lista, tab_novo = st.tabs(['📋 Listar', '➕ Nova Disciplina'])

with tab_novo:
    st.subheader('Cadastrar nova disciplina')
    with st.form('form_disciplinas'):
        nome = st.text_input('Nome da disciplina: ')
        professor = st.text_input('Nome do professor: ')
        dia_semana = st.selectbox('Dia da aula', ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'])

        submitted = st.form_submit_button('Salvar')

        if submitted:
            st.success(f'Disciplina {nome} cadastrada! (simulação)')



with tab_lista:
    st.info('A conexão com o xano virá na terafa 13.')
    st.dataframe([
        {'Nome': 'Python Basics', 'Professor': 'Oriel', 'Dia': 'Segunda'},
        {'Nome': 'Inovation lab', 'Professor': 'Giuliano', 'Dia': 'Quinta'},
        {'Nome': 'Data Base Design', 'Professor': 'Takai', 'Dia': 'Terça'}
    ], use_container_width = True)