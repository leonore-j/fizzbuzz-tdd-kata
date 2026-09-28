# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.24.2",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import pytest

@app.function
def fizzbuzz(n: int) -> str:
    """Return the FizzBuzz representation of the integer n.

    Contract:
    - if n is a multiple of 3 AND 5: "FizzBuzz"
    - if n is a multiple of 3 only: "Fizz"
    - if n is a multiple of 5 only: "Buzz"
    - otherwise: str(n)

    Raises ValueError if n is not a strictly positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("fizzbuzz expects a strictly positive integer")

    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result or str(n)

@app.cell
def _():
    mo.md(r"""
    ## Final test suite (parametrized)

    Once the contract is stable, we can group all the cases into a
    single parametrized test — more readable and easier to extend
    than separate tests.
    """)
    return

def _():
    mo.md(r"""
    ## Explore interactively

    Use the field below to call `fizzbuzz` on an integer of your
    choice and see the result live — handy for a classroom demo.
    """)
    return


@app.cell
def _():
    n_input = mo.ui.number(start=1, stop=1000, step=1, value=15, label="n")
    n_input
    return (n_input,)


@app.cell
def _(n_input):
    try:
        result = fizzbuzz(n_input.value)
        output = mo.md(f"`fizzbuzz({n_input.value})` → **{result}**")
    except ValueError as e:
        output = mo.md(f"⚠️ Error: {e}")
    output
    return