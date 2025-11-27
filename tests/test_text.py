import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("ТЕСТ123!!!", "тест123!!!"),
        ("", ""),
        ("   ", ""),
        ("\n\t\r", ""),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "sourse, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello world test", ["hello", "world", "test"]),
        ("один, два. три!", ["один", "два", "три"]),
        ("", []),
        ("   ", []),
        ("word", ["word"]),
        ("много    пробелов", ["много", "пробелов"]),
    ],
)
def test_tokenize_basic(sourse, expected):
    assert tokenize(sourse) == expected


def test_count_freq_and_top_n_basic():
    tokens = ["яблоко", "банан", "яблоко", "яблоко", "банан", "яблоко"]
    expected = {"яблоко": 4, "банан": 2}
    assert count_freq(tokens) == expected

    top = top_n(count_freq(tokens), 1)
    assert top == [("яблоко", 4)]


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_top_n_large():
    freq = {"яблоко": 2, "бананы": 1}
    expected = [("яблоко", 2), ("бананы", 1)]
    assert top_n(freq, 10) == expected


def test_top_n_zero():
    freq = {"ялоко": 2, "бананы": 1}
    assert top_n(freq, 0) == []


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"яблоко": 3, "банан": 3, "апельсин": 1}, 2, [("банан", 3), ("яблоко", 3)]),
    ],
)
def test_top_n_tie_breaker(freq, n, expected):
    result = top_n(freq, n)
    assert result == expected
