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
    ### Exercises
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise 1
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given two floats `a` and `b`, and some tolerance `tol`, write an expression that will test whether `a` and `b` are within `tol` of each other.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise 2
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Assume you have some variable `elapsed` that contains elapsed time in seconds.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create three new variables: `hours`, `minutes` and `seconds`, that represent the number of hours, minutes and seconds represented by `elapsed`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, if `elapsed = 7835`, then `hours = 2`, `minutes = 10` and `seconds = 35`
    """)
    return


if __name__ == "__main__":
    app.run()
