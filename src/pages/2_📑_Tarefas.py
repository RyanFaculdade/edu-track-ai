import streamlit as st

st.set_page_config(page_title = 'Tarefas', page_icon = '📑')

st.title('Minhas tarefas')

col1, col2 = st.columns([3, 1])

with col1:
    search = st.text_input('Buscar tarefa...', placeholder = 'Ex: Estudar Pandas')

with col2:
    filtro = st.selectbox('Status', ['Todas', 'Feito', 'Não feito'])

st.markdown('---')

with st.expander('📌 Tarefa 01: Configuração do ambiente (clique para ver)', expanded = True):
    st.write('**Disciplinas:** Innovation Lab')
    st.write('**Prazo:** 20/02/2026')
    st.checkbox('Marcar como concluida', value = False)

