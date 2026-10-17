"""Utility functions for common text processing tasks."""

from __future__ import annotations

import re
import unicodedata


def slugify(text: str) -> str:
    """Convert arbitrary text into a URL-friendly slug."""
    normalized = unicodedata.normalize("NFKD", text)
    normalized = normalized.encode("ascii", "ignore").decode("ascii")
    normalized = normalized.lower().strip()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    return normalized.strip("-")


def count_words(text: str) -> int:
    """Return the number of words in a string."""
    if not text.strip():
        return 0
    return len(text.split())


def to_uppercase(text: str) -> str:
    """Convert a string to uppercase."""
    return text.upper()


def normalize_whitespace(text: str) -> str:
    """Collapse repeated whitespace into a single space."""
    return " ".join(text.split())
