"""Fetch page markdown via official tavily-python SDK."""

from __future__ import annotations

import os

from tavily import TavilyClient

from .base import Fetcher


class TavilyFetcher(Fetcher):
    name = "tavily"

    def __init__(
        self,
        *,
        api_key: str | None = None,
        concurrency: int = 4,  # kept for create_fetcher interface; SDK is request-based
        timeout: float = 60.0,
        extract_depth: str = "advanced",
    ) -> None:
        del concurrency  # unused; ThreadPoolExecutor in main handles concurrency
        self.api_key = (
            api_key
            or os.environ.get("TAVILY_API_KEY")
            or os.environ.get("tavily_key")
            or os.environ.get("TAVILY_KEY")
            or ""
        )
        if not self.api_key:
            raise RuntimeError(
                "Tavily API key not found. Set TAVILY_API_KEY or tavily_key in .env"
            )
        self.extract_depth = extract_depth
        self.timeout = timeout
        self._client = TavilyClient(self.api_key)

    def fetch(self, url: str) -> str:
        response = self._client.extract(
            urls=[url],
            extract_depth=self.extract_depth,
            format="markdown",
            timeout=self.timeout,
        )
        results = response.get("results") or []
        if results:
            content = (results[0].get("raw_content") or "").strip()
            if content:
                return content

        failed = response.get("failed_results") or []
        reason = ""
        if failed:
            reason = failed[0].get("error") or str(failed[0])
        raise RuntimeError(reason or f"No content extracted from {url}")

    def close(self) -> None:
        close = getattr(self._client, "close", None)
        if callable(close):
            close()
