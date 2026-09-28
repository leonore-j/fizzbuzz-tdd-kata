# tests/test_core.py
import marimo
import pytest
from fizzbuzz_tdd_kata.core import fizzbuzz

__generated_with = "0.24.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import pytest

@app.function
@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (5, "Buzz"),
        (6, "Fizz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
        (100, "Buzz"),
    ],
)
def test_cases(n, expected):
    assert fizzbuzz(n) == expected


@app.cell
def test_fizzbuzz_rejects_invalid_input():
    with pytest.raises(ValueError):
        fizzbuzz(0)
    with pytest.raises(ValueError):
        fizzbuzz(-5)
    return
