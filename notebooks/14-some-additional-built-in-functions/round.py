import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### round
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can use the `round()` built-in function to round floats and integers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By default, `round()` will round to the closest integer (using banker's rounding):
    """)
    return


@app.cell
def _():
    round(0.325)
    return


@app.cell
def _():
    round(0.875)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And for ties:
    """)
    return


@app.cell
def _():
    round(13.5)
    return


@app.cell
def _():
    round(12.5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see it rounds to the closest **even** integer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can pass a second argument to `round()` to specify what multiple of 1/10 we want to round to.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, we can round to the closest multiple of `0.1` this way:
    """)
    return


@app.cell
def _():
    round(0.125, 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and to the closest multiple of `0.01`:
    """)
    return


@app.cell
def _():
    round(0.125, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But that second argument can be negative, and that allows us to round to the closest multiple of `10`, `100`, etc...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example:
    """)
    return


@app.cell
def _():
    round(123456, -1)
    return


@app.cell
def _():
    round(123456, -2)
    return


@app.cell
def _():
    round(123456, -3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Again, ties will go the closest number ending in an even digit:
    """)
    return


@app.cell
def _():
    round(1235, -1)
    return


@app.cell
def _():
    round(1245, -1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's go back to floats for a bit now. The problem is that floats do not have exact representations (at least the majority of them).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A number such as `0.125` does have an exact representation, so if we round to the closest multiple of `0.01`:
    """)
    return


@app.cell
def _():
    round(0.125, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    we see that the rounding rounded down to `1.2` - since `1.3` ends with an odd digit, `1.2` was picked.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But wee may sometimes observe odd behavior, where this is not happening!
    """)
    return


@app.cell
def _():
    round(0.325, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We woud have expected the answer to be `0.32`, not `0.33`. An in a prefect world, that would be the case - but `0.325` does not have an exact representation as a float:
    """)
    return


@app.cell
def _():
    format(0.325, '.20f')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, this number is not **exactly** `0.325`, but rather slightly higher. This means that when we round this number we do **not** actually have a tie - it simply rounds to the closest multiple of `0.01`, which is `0.33`.
    """)
    return


if __name__ == "__main__":
    app.run()
