import time
import logging
from typing import Optional

import requests

from src.config import XANO_BASE_URL, XANO_API_KEY

logger = logging.getLogger(__name__)

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2


class XanoClient:
    """HTTP client for Xano API with retry logic for rate limits."""

    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None):
        self.base_url = (base_url or XANO_BASE_URL).rstrip("/")
        self.api_key = api_key or XANO_API_KEY
        self._session = requests.Session()
        if self.api_key:
            self._session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def _request_with_retry(
        self,
        method: str,
        endpoint: str,
        retries: int = MAX_RETRIES,
        **kwargs,
    ) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        last_exception = None

        for attempt in range(retries):
            try:
                response = self._session.request(method, url, **kwargs)

                if response.status_code == 429:
                    wait = RETRY_DELAY_SECONDS * (attempt + 1)
                    logger.warning(
                        "Rate limited on %s %s, retry %d/%d after %ds",
                        method,
                        endpoint,
                        attempt + 1,
                        retries,
                        wait,
                    )
                    time.sleep(wait)
                    last_exception = None
                    continue

                response.raise_for_status()
                return response

            except requests.exceptions.RequestException as exc:
                last_exception = exc
                if attempt < retries - 1:
                    wait = RETRY_DELAY_SECONDS * (attempt + 1)
                    logger.warning(
                        "Request failed on %s %s, retry %d/%d: %s",
                        method,
                        endpoint,
                        attempt + 1,
                        retries,
                        exc,
                    )
                    time.sleep(wait)

        if last_exception:
            raise last_exception
        return response

    def get(self, endpoint: str, params: Optional[dict] = None) -> list:
        resp = self._request_with_retry("GET", endpoint, params=params)
        return resp.json() if resp.content else []

    def get_by_id(self, endpoint: str, record_id: int) -> dict:
        resp = self._request_with_retry("GET", f"{endpoint}/{record_id}")
        return resp.json()

    def post(self, endpoint: str, json: dict) -> dict:
        resp = self._request_with_retry("POST", endpoint, json=json)
        return resp.json()

    def put(self, endpoint: str, record_id: int, json: dict) -> dict:
        resp = self._request_with_retry("PUT", f"{endpoint}/{record_id}", json=json)
        return resp.json()

    def delete(self, endpoint: str, record_id: int) -> Optional[dict]:
        resp = self._request_with_retry("DELETE", f"{endpoint}/{record_id}")
        return resp.json() if resp.content else None
