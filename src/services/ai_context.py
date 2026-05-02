from src.services.subject_service import SubjectService
from src.services.xano_client import XanoClient


SYSTEM_PROMPT_BASE = (
    "Voce e um assistente academico dedicado a ajudar estudantes a alcancarem "
    "seus objetivos de estudo. Forneca recomendacoes praticas e motivacionais."
)


def build_ai_context(subject_id: int | None = None) -> str:
    """Build subject-enriched context for the AI assistant prompt."""
    client = XanoClient()
    service = SubjectService(client=client)

    subjects = service.list_subjects()
    if not subjects:
        return SYSTEM_PROMPT_BASE

    context_parts = [SYSTEM_PROMPT_BASE]

    if subject_id:
        target = next((s for s in subjects if s["id"] == subject_id), None)
        if target:
            context_parts.append(
                f"O estudante esta focando na disciplina '{target['name']}'."
            )
            if target.get("description"):
                context_parts.append(
                    f"Informacoes sobre a disciplina: {target['description']}."
                )
    else:
        names = [s["name"] for s in subjects]
        context_parts.append(
            f"O estudante esta cursando as seguintes disciplinas: {', '.join(names)}."
        )

    return " ".join(context_parts)


def get_subject_recommendation_prompt(subject_name: str) -> str:
    """Generate a prompt for subject-specific recommendations."""
    return (
        f"O estudante precisa de orientacao especifica para a disciplina "
        f"'{subject_name}'. Sugira um plano de estudo, recursos e dicas "
        f"para melhorar o desempenho nesta disciplina."
    )
