# Sai Utility Kit

`Sai Utility Kit` is a small Python package for common text-processing tasks. It is designed to be easy to import, test, and publish to package indexes such as TestPyPI.

## Features

- `slugify(text: str) -> str` converts text into a URL-friendly slug.
- `count_words(text: str) -> int` counts words in a string.
- `to_uppercase(text: str) -> str` normalizes text to uppercase.
- `normalize_whitespace(text: str) -> str` collapses repeated whitespace.

## Installation

```bash
pip install sai-utility-kit
```

## Example

```python
from sai_utility_kit import slugify, count_words, normalize_whitespace

print(slugify("Hello, World!"))
print(count_words("one two three"))
print(normalize_whitespace("  hello    world  "))
```

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install pytest pytest-cov build twine
pytest --cov=sai_utility_kit
python -m build
```
