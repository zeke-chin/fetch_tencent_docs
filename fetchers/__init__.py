"""Document fetchers: jina (default) and tavily."""

from __future__ import annotations

from .base import Fetcher
from .jina import JinaFetcher
from .tavily import TavilyFetcher

__all__ = ["Fetcher", "JinaFetcher", "TavilyFetcher", "create_fetcher"]


def create_fetcher(
    name: str,
    *,
    concurrency: int = 4,
    timeout: float = 60.0,
    tavily_depth: str = "advanced",
) -> Fetcher:
    name = name.lower().strip()
    if name == "jina":
        return JinaFetcher(concurrency=concurrency, timeout=timeout)
    if name == "tavily":
        return TavilyFetcher(
            concurrency=concurrency,
            timeout=timeout,
            extract_depth=tavily_depth,
        )
    raise ValueError(f"Unknown fetcher: {name!r}. Choose from: jina, tavily")
