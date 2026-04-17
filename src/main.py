import streamlit as st

# Config da pagina

# Titulo na aba do browser

st.set_page_config(page_title='EduTrack AI', page_icon='🏢')

# Titulo principal

st.title('EduTrack IA')

st.sidebar.header('Menu')
opcao_menu = st.sidebar.radio('Navegar', ['Dashboard', 'Disciplinas', 'Tarefas'])


# Conteudo dinamico

if opcao_menu == 'Dashboard':
    st.write('Bem vindo ao seu assistente academico!')
    st.info('Conecte ao xano para ver seus dados reais')

    # Exemplo de metricas visuais

    col1, col2 = st.columns(2)
    col1.metric('Disciplinas ativas', '0')
    col2.metric('Tarefas pendentes', '0')

elif opcao_menu == 'Disciplinas':
    st.subheader('Minhas disciplinas')
    st.write('Aqui listaremos as disciplinas')

else:
    st.subheader('Gerenciamente das tarefas')
    st.checkbox('Exemplo: Estudar python')
    st.checkbox('Exemplo: Estudar streamlit')