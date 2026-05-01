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
    ### Exercises
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Question 1
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There is a file named `transactions.csv` which is a list of purchases and sales.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write code that loads this data and calculates the total of these purchases and sales.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Take two approaches - one using floats, and one using Decimal objects. Calculate the difference between the two results.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Also, time how long it takes to run your code using floats and using Decimals.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 2
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Using the same file (`transactions.csv`), we now want to calculate a fee on each transaction.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Irrespective of whether the transaction was a credit or a debit, we will calculate a `0.123%` transaction fee for the (absolute) values of each transaction.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Each** fee calculation precision should be limited to `8` digits after the decimal point (so use `round(val, 8)`)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In addition, any rounding should always round ties away from `0` (`ROUND_HALF_UP`) - and not use Banker's rounding (`ROUND_HALF_EVEN`).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Only implement this solution using `Decimal` objects, as floats do not offer a rounding algorithm choice, and writing our own rounding algorithm can be overly complicated.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Also calculate the different in the fee totals when using `ROUND_HALF_UP` vs `ROUND_HALF_EVEN`
    """)
    return


if __name__ == "__main__":
    app.run()
