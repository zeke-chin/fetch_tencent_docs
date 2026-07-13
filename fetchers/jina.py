"""Fetch page markdown via Jina Reader (https://r.jina.ai/)."""

from __future__ import annotations

import os

import httpx

from .base import Fetcher


class JinaFetcher(Fetcher):
    name = "jina"
    base_url = "https://r.jina.ai"

    def __init__(
        self,
        *,
        api_key: str | None = None,
        concurrency: int = 4,
        timeout: float = 60.0,
    ) -> None:
        self.api_key = (
            api_key
            or os.environ.get("JINA_API_KEY")
            or os.environ.get("jina_key")
            or os.environ.get("JINA_KEY")
            or ""
        )
        self._base_headers = {
            "Accept": "text/markdown",
            "X-Return-Format": "markdown",
        }
        self._client = httpx.Client(
            timeout=httpx.Timeout(timeout, connect=15.0),
            follow_redirects=True,
            limits=httpx.Limits(
                max_connections=max(concurrency, 1),
                max_keepalive_connections=max(concurrency, 1),
            ),
        )

    def _headers(self, *, with_auth: bool) -> dict[str, str]:
        headers = dict(self._base_headers)
        if with_auth and self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def fetch(self, url: str) -> str:
        # r.jina.ai/<target-url> — keep full scheme+host of target
        target = url if url.startswith("http") else f"https://{url}"
        endpoint = f"{self.base_url}/{target}"

        response = self._client.get(endpoint, headers=self._headers(with_auth=True))

        # Paid key may 401/402/403 when invalid or balance empty → free tier.
        if response.status_code in {401, 402, 403} and self.api_key:
            response = self._client.get(
                endpoint, headers=self._headers(with_auth=False)
            )

        if response.status_code >= 400:
            raise RuntimeError(
                f"Jina HTTP {response.status_code}: {response.text[:300]}"
            )
        content = response.text.strip()
        if not content:
            raise RuntimeError(f"Jina returned empty content for {url}")
        return content

    def close(self) -> None:
        self._client.close()
