from src.services.xano_client import XanoClient


class DashboardService:
    """Service for fetching dashboard data grouped by subject."""

    def __init__(self, client: XanoClient):
        self.client = client

    def fetch_grades(self, subject_id: int | None = None) -> list[dict]:
        params = {}
        if subject_id is not None:
            params["subject_id"] = subject_id
        return self.client.get("grades", params=params if params else None)

    def fetch_tasks(self, subject_id: int | None = None) -> list[dict]:
        params = {}
        if subject_id is not None:
            params["subject_id"] = subject_id
        return self.client.get("tasks", params=params if params else None)

    def fetch_goals(self, subject_id: int | None = None) -> list[dict]:
        params = {}
        if subject_id is not None:
            params["subject_id"] = subject_id
        return self.client.get("goals", params=params if params else None)
