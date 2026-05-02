import streamlit as st

from src.config import SUBJECT_COLOR_PALETTE
from src.services.subject_service import SubjectService, DuplicateSubjectError
from src.services.xano_client import XanoClient


def _get_service() -> SubjectService:
    if "xano_client" not in st.session_state:
        st.session_state.xano_client = XanoClient()
    return SubjectService(client=st.session_state.xano_client)


def _color_swatch_hex(color: str) -> str:
    return color if color.startswith("#") else f"#{color}"


def render_subjects_page() -> None:
    st.title("Gestao de Disciplinas")

    tab_lista, tab_novo = st.tabs(["Lista", "Nova Disciplina"])

    with tab_lista:
        _render_subject_list()

    with tab_novo:
        _render_add_subject_form()


def _render_subject_list() -> None:
    service = _get_service()

    try:
        subjects = service.list_subjects()
    except Exception:
        st.error("Nao foi possivel carregar as disciplinas. Verifique a conexao com o Xano.")
        return

    if not subjects:
        st.info("Nenhuma disciplina cadastrada. Crie a primeira na aba 'Nova Disciplina'.")
        return

    for subject in subjects:
        _render_subject_card(subject)


def _render_subject_card(subject: dict) -> None:
    color = subject.get("color", "#888888")
    name = subject.get("name", "Sem nome")
    description = subject.get("description", "")

    with st.expander(f"{_color_swatch_hex(color)} **{name}**"):
        if description:
            st.write(description)

        col_edit, col_delete = st.columns([3, 1])

        with col_edit:
            if st.button("Editar", key=f"edit_{subject['id']}"):
                st.session_state[f"editing_{subject['id']}"] = True

        with col_delete:
            if st.button("Excluir", key=f"del_{subject['id']}", type="secondary"):
                st.session_state[f"deleting_{subject['id']}"] = True

        if st.session_state.get(f"editing_{subject['id']}"):
            _render_edit_form(subject)

        if st.session_state.get(f"deleting_{subject['id']}"):
            _render_delete_confirmation(subject)


def _render_edit_form(subject: dict) -> None:
    service = _get_service()

    with st.form(key=f"edit_form_{subject['id']}"):
        name = st.text_input(
            "Nome",
            value=subject.get("name", ""),
            key=f"edit_name_{subject['id']}",
        )
        description = st.text_area(
            "Descricao",
            value=subject.get("description", ""),
            key=f"edit_desc_{subject['id']}",
        )
        color = st.selectbox(
            "Cor",
            options=SUBJECT_COLOR_PALETTE,
            index=SUBJECT_COLOR_PALETTE.index(subject.get("color", SUBJECT_COLOR_PALETTE[0]))
            if subject.get("color") in SUBJECT_COLOR_PALETTE
            else 0,
            key=f"edit_color_{subject['id']}",
        )

        col_save, col_cancel = st.columns(2)
        with col_save:
            saved = st.form_submit_button("Salvar")
        with col_cancel:
            cancelled = st.form_submit_button("Cancelar")

        if saved:
            if not name.strip():
                st.error("O nome da disciplina e obrigatorio.")
                return
            try:
                service.update_subject(
                    subject_id=subject["id"],
                    name=name,
                    description=description,
                    color=color,
                )
                st.success("Disciplina atualizada com sucesso!")
                st.session_state.pop(f"editing_{subject['id']}", None)
                st.rerun()
            except DuplicateSubjectError as e:
                st.error(str(e))

        if cancelled:
            st.session_state.pop(f"editing_{subject['id']}", None)
            st.rerun()


def _render_delete_confirmation(subject: dict) -> None:
    name = subject.get("name", "Sem nome")
    st.warning(f"Tem certeza que deseja excluir '{name}'?")

    col_confirm, col_cancel = st.columns(2)
    with col_confirm:
        confirmed = st.button("Confirmar exclusao", key=f"confirm_del_{subject['id']}", type="primary")
    with col_cancel:
        cancelled = st.button("Cancelar", key=f"cancel_del_{subject['id']}")

    if confirmed:
        service = _get_service()
        try:
            service.delete_subject(subject["id"])
            st.success(f"Disciplina '{name}' excluida com sucesso!")
            st.session_state.pop(f"deleting_{subject['id']}", None)
            st.rerun()
        except Exception:
            st.error("Nao foi possivel excluir a disciplina. Verifique a conexao com o Xano.")

    if cancelled:
        st.session_state.pop(f"deleting_{subject['id']}", None)
        st.rerun()


def _render_add_subject_form() -> None:
    service = _get_service()

    with st.form("form_nova_disciplina"):
        st.subheader("Cadastrar nova disciplina")
        nome = st.text_input("Nome da disciplina")
        professor = st.text_input("Nome do professor (opcional)")
        dia_semana = st.selectbox(
            "Dia da aula",
            ["Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"],
        )
        cor = st.selectbox("Cor da disciplina", options=SUBJECT_COLOR_PALETTE)

        submitted = st.form_submit_button("Salvar")

        if submitted:
            if not nome.strip():
                st.error("O nome da disciplina e obrigatorio.")
                return

            description_parts = []
            if professor.strip():
                description_parts.append(f"Professor: {professor.strip()}")
            description_parts.append(f"Dia: {dia_semana}")
            description = " | ".join(description_parts)

            try:
                service.create_subject(name=nome, color=cor, description=description)
                st.success(f"Disciplina '{nome}' cadastrada com sucesso!")
                st.rerun()
            except DuplicateSubjectError as e:
                st.error(str(e))
