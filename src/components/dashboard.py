import streamlit as st

from src.components.subjects import _get_service
from src.services.dashboard_service import DashboardService
from src.services.xano_client import XanoClient


def render_dashboard() -> None:
    st.write("Bem vindo ao seu assistente academico!")

    subject_service = _get_service()

    try:
        subjects = subject_service.list_subjects()
    except Exception:
        st.warning("Nao foi possivel conectar ao Xano. Exibindo dados sem filtro de disciplina.")
        subjects = []

    selected_subject_id = _render_subject_filter(subjects)

    _render_dashboard_content(subjects, selected_subject_id)


def _render_subject_filter(subjects: list[dict]) -> int | None:
    if not subjects:
        return None

    options = ["Todas as Disciplinas"] + [s["name"] for s in subjects]
    selected = st.selectbox("Filtrar por disciplina", options=options)

    if selected == "Todas as Disciplinas":
        return None

    for s in subjects:
        if s["name"] == selected:
            return s["id"]
    return None


def _render_dashboard_content(subjects: list[dict], subject_id: int | None) -> None:
    if "xano_client" not in st.session_state:
        st.session_state.xano_client = XanoClient()
    dash_service = DashboardService(st.session_state.xano_client)

    try:
        grades = dash_service.fetch_grades(subject_id)
        tasks = dash_service.fetch_tasks(subject_id)
    except Exception:
        grades = []
        tasks = []

    completed = sum(1 for t in tasks if t.get("completed", False))
    total_tasks = len(tasks)

    col1, col2, col3 = st.columns(3)
    col1.metric("Disciplinas ativas", str(len(subjects) if subject_id is None else 1))
    col2.metric("Tarefas pendentes", str(total_tasks - completed))
    if grades:
        avg = sum(g.get("grade", 0) for g in grades) / len(grades)
        col3.metric("Media geral", f"{avg:.1f}")
    else:
        col3.metric("Media geral", "N/A")

    if subjects:
        st.markdown("---")
        _render_subject_summary_cards(subjects, subject_id, dash_service)


def _render_subject_summary_cards(
    subjects: list[dict],
    selected_id: int | None,
    dash_service: DashboardService,
) -> None:
    filtered = [s for s in subjects if s["id"] == selected_id] if selected_id else subjects

    cols = st.columns(min(len(filtered), 3))
    for i, subject in enumerate(filtered):
        col = cols[i % 3]
        with col:
            color = subject.get("color", "#888888")
            st.markdown(
                f"<span style='display:inline-block;width:12px;height:12px;"
                f"background-color:{color};border-radius:50%;margin-right:6px;'></span>"
                f"**{subject['name']}**",
                unsafe_allow_html=True,
            )

            grades = dash_service.fetch_grades(subject["id"])
            tasks = dash_service.fetch_tasks(subject["id"])

            if grades:
                avg = sum(g.get("grade", 0) for g in grades) / len(grades)
                st.metric("Media", f"{avg:.1f}")
            else:
                st.info("Sem notas ainda")

            completed = sum(1 for t in tasks if t.get("completed", False))
            total = len(tasks)
            if total > 0:
                rate = (completed / total) * 100
                st.metric("Tarefas concluidas", f"{completed}/{total} ({rate:.0f}%)")
            else:
                st.info("Sem tarefas")
