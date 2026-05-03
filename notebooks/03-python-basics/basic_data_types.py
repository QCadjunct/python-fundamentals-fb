# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.23.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Basic Data Types
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We are going to use literals to create integers, floats and booleans:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here are a few integers:
    """)
    return


@app.cell
def _():
    1
    return


@app.cell
def _():
    -10
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To create floats, we can just use a decimal (`.`) point:
    """)
    return


@app.cell
def _():
    1.0
    return


@app.cell
def _():
    -10.5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And for booleans, we use the **keywords** `True` and `False`:
    """)
    return


@app.cell
def _():
    True
    return


@app.cell
def _():
    False
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Recall what we discussed in the lecture: floats do not always have exact internal representations.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Specifically, we saw that `0.1` does not have an exact binary representation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, why does this look like `0.1` is exact?
    """)
    return


@app.cell
def _():
    0.1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have to be a bit careful! The output we are seeing here is Python's string representation (any output to the terminal is a string - a bunch of characters) - not the actual internal value.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And Python tries to be "nice" by formatting the number in a more human readable fashion.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The problem here is that this hides the internals.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To fix this, we are going to use the `format` function (we'll explain functions later) to specify the number of digits we want after the decimal point in the display:
    """)
    return


@app.cell
def _():
    format(0.1, '.25f')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here Python is basically rounding the internal number `0.1` to `25` digits after the decimal point - and now we can see that `0.1` is not stored exactly.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    However, a float such as `0.125`, which is `1/8`, **is** therefore representable as a finite binary fraction (`1/2^3`):
    """)
    return


@app.cell
def _():
    format(0.125, '0.25f')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So that is stored exactly.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The reason it is important to understand this is when we try to compare floats.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When we deal with integers it is perfectly fine to compare two integers using equality (we'll cover `==` in detail later):
    """)
    return


@app.cell
def _():
    1 + 1 + 1 == 3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, the sum of the three integer `1`, `1` and `1` is exactly equal to the integer `3`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But not so with floats!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Consider adding `0.125` three times - we expect that the result should be `0.375`:
    """)
    return


@app.cell
def _():
    0.125 + 0.125 + 0.125 == 0.375
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That turns out to be the result we expect - but that's because `0.125` (and hence `0.375` has an exact float representation).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But consider this example using `0.1` which we know does not have an exact representation:
    """)
    return


@app.cell
def _():
    0.1 + 0.1 + 0.1 == 0.3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This result is not what we would expect.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can see why by looking at a more detailed string representation of those numbers:
    """)
    return


@app.cell
def _():
    format(0.1 + 0.1 + 0.1, '.25f')
    return


@app.cell
def _():
    format(0.3, '.25f')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we can clearly see, the internal representations are not exactly the same. Hence why using `==` evaluated to `False`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When dealing with `float` numbers, we should not, in general, use `==` - instead we should use some measure of closeness (within `0.01` for example).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So instead we might do something like this:
    """)
    return


@app.cell
def _():
    abs((0.1 + 0.1 + 0.1) - 0.3) < 0.001
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    (Here, `abs` is a Python built-in function that calculates the absolute value of a number)
    """)
    return


if __name__ == "__main__":
    app.run()
