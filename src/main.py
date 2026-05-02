import streamlit as st
from src.components.subjects import render_subjects_page
from src.components.dashboard import render_dashboard

st.set_page_config(page_title='EduTrack AI', page_icon='🏢')

st.title('EduTrack IA')

st.sidebar.header('Menu')
opcao_menu = st.sidebar.radio('Navegar', ['Dashboard', 'Disciplinas', 'Tarefas'])


if opcao_menu == 'Dashboard':
    render_dashboard()

elif opcao_menu == 'Disciplinas':
    render_subjects_page()

else:
    st.subheader('Gerenciamente das tarefas')
    st.checkbox('Exemplo: Estudar python')
    st.checkbox('Exemplo: Estudar streamlit')