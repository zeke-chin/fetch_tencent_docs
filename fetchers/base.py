"""Abstract markdown fetcher interface."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Fetcher(ABC):
    """Fetch a remote page and return Markdown text."""

    name: str

    @abstractmethod
    def fetch(self, url: str) -> str:
        """Return markdown content for *url*. Raise on failure."""

    def close(self) -> None:
        """Release network resources."""

    def __enter__(self) -> Fetcher:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()
