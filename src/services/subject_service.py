from typing import Optional

from src.services.xano_client import XanoClient

SUBJECTS_ENDPOINT = "subjects"


class DuplicateSubjectError(Exception):
    """Raised when a subject name already exists."""


class SubjectService:
    """Service layer for subject CRUD operations against Xano."""

    def __init__(self, client: Optional[XanoClient] = None):
        self.client = client or XanoClient()

    def list_subjects(self) -> list[dict]:
        return self.client.get(SUBJECTS_ENDPOINT)

    def get_subject(self, subject_id: int) -> dict:
        return self.client.get_by_id(SUBJECTS_ENDPOINT, subject_id)

    def create_subject(self, name: str, color: str, description: str = "") -> dict:
        existing = self.list_subjects()
        for sub in existing:
            if sub.get("name", "").strip().lower() == name.strip().lower():
                raise DuplicateSubjectError(
                    f"A subject with the name '{name}' already exists."
                )

        payload = {"name": name.strip(), "color": color}
        if description:
            payload["description"] = description.strip()

        return self.client.post(SUBJECTS_ENDPOINT, json=payload)

    def update_subject(
        self,
        subject_id: int,
        name: Optional[str] = None,
        color: Optional[str] = None,
        description: Optional[str] = None,
    ) -> dict:
        if name is not None:
            existing = self.list_subjects()
            for sub in existing:
                if (
                    sub.get("id") != subject_id
                    and sub.get("name", "").strip().lower() == name.strip().lower()
                ):
                    raise DuplicateSubjectError(
                        f"A subject with the name '{name}' already exists."
                    )

        payload = {}
        if name is not None:
            payload["name"] = name.strip()
        if color is not None:
            payload["color"] = color
        if description is not None:
            payload["description"] = description.strip()

        return self.client.put(SUBJECTS_ENDPOINT, subject_id, json=payload)

    def delete_subject(self, subject_id: int) -> None:
        self.client.delete(SUBJECTS_ENDPOINT, subject_id)
