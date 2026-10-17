from sai_utility_kit import count_words, normalize_whitespace, slugify, to_uppercase


def test_slugify_basic():
    assert slugify("Hello World!") == "hello-world"
    assert slugify("  leading and trailing spaces  ") == "leading-and-trailing-spaces"


def test_slugify_special_chars_and_underscores():
    assert slugify("Hello_World---Again") == "hello-world-again"
    assert slugify("Café & Co") == "cafe-co"


def test_count_words():
    assert count_words("one two three") == 3
    assert count_words("   spaced   words  here ") == 3
    assert count_words("") == 0


def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("already uppercase") == "ALREADY UPPERCASE"


def test_normalize_whitespace():
    assert normalize_whitespace("  hello    world  ") == "hello world"
    assert normalize_whitespace("line\n  break\twith spaces") == "line break with spaces"
