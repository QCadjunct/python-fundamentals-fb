import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    ### Variables
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Recall that we use the = symbol as the assignment operator.
    We specify a variable name on the left hand side,
    and the value on the right hand side.
    """)
    return


@app.cell
def _():
    a_int = 100
    a_int
    return (a_int,)


@app.cell
def _(a_int):
    b = a_int + 11
    b
    return


@app.cell
def _(mo):
    mo.md("""
    Note: the following raises SyntaxError - cannot assign to a literal:

    ```python
    10 = 10
    ```
    """)
    return


@app.cell
def _():
    a_float = 3.14
    a_float
    return


@app.cell
def _():
    test = 10
    test_1 = 10
    _test_1_ = 10
    __test__ = 10
    TEST = 10
    return


@app.cell
def _(mo):
    mo.md("""
    Invalid names - shown here as documentation only:

    ```python
    1_test = 10   # SyntaxError - cannot start with digit
    if = 10       # SyntaxError - reserved keyword
    ```
    """)
    return


@app.cell
def _():
    a_from_float = float(10)
    a_from_float
    return


@app.cell
def _(mo):
    mo.md("""
    Shadowing float is possible but dangerous:

    ```python
    float = 100.5      # shadows built-in
    a = float(10)      # TypeError: float object is not callable
    del float          # restores built-in
    ```
    """)
    return


@app.cell
def _():
    a_restored = float(10)
    print(a_restored)
    return


@app.cell
def _(mo):
    mo.md("""
    #### Naming Conventions - PEP8
    """)
    return


@app.cell
def _():
    current_balance = 100.0
    currentBalance = 100.0
    return


@app.cell
def _(mo):
    mo.md("""
    Poor naming - hard to understand:
    """)
    return


@app.cell
def _():
    x = 100
    y = 0.1
    z = 10
    r = x * ((1 + y/12) ** (z * 12))
    print(r)
    return


@app.cell
def _(mo):
    mo.md("""
    Good naming - immediately clear:
    """)
    return


@app.cell
def _():
    principal = 100
    apr = 0.1
    years = 10
    future_value = principal * ((1 + apr/12) ** (years * 12))
    print(future_value)
    return


if __name__ == "__main__":
    app.run()
