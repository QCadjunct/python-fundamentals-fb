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
    ### Operator Precedence
    """)
    return


@app.cell
def _():
    100 - 20 + 50
    return


@app.cell
def _():
    principal = 100
    apr = 0.1
    years = 10
    future_value_1 = principal * ((1 + apr/12) ** (years * 12))
    print(future_value_1)
    return apr, principal, years


@app.cell
def _(apr, principal, years):
    future_value_2 = principal * (1 + apr/12) ** (years * 12)
    print(future_value_2)
    return


@app.cell
def _():
    n = 10
    n * n + 1
    return (n,)


@app.cell
def _(n):
    n * (n + 1)
    return


if __name__ == "__main__":
    app.run()
