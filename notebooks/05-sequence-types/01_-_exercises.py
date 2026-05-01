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
    #### Exercise 1
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the following string:
    """)
    return


@app.cell
def _():
    s = 'FfEeDdCcBbAa'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create two new variables that contain just the lower and upper case letters of `s` respectively, in the correct alphabetical order, i.e:

    - `'ABCDEF'`
    - `'abcdef'`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Exercise 2
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Concatenate the following tuples into a single one, but replacing the odd values with zeros (`0`).
    """)
    return


@app.cell
def _():
    t1 = 1, 2, 3, 4, 5, 6
    t2 = 7, 8, 9, 10
    t3 = 11, 12, 13, 14, 15, 16, 17
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can assume that every tuple is a sequence of consecutive integers starting with an odd integer.

    Try to write your code to be as generic as possible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Exercise 3
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the following matrix:
    """)
    return


@app.cell
def _():
    m = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Make this matrix into an identity matrix (setting the diagonal elements to `1`).

    Your code should *mutate* `m`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Exercise 4
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Do the same problem as Exercise 3, but do **not** mutate `m`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Exercise 5
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You are given a list of tuples that each contain 4 values:

    ```
    (amount, currency, target_currency, exchange_rate)
    ```
    """)
    return


@app.cell
def _():
    data = [
        (100, 'USD', 'EUR', 0.83),
        (100, 'USD', 'CAD', 1.27),
        (100, 'CAD', 'EUR', 0.65)
    ]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write code that converts the `amount` from its `currency` to its `target_currency` using the `exchange_rate` (which is the exchange rate for `1` `currency` in `target_currency`).

    Try to make your code as generic as possible (we'll see later how to use loops so we don't have to write three separate statements).

    In other words, you'll need three blocks of code here that are essentially almost identical.

    Use unpacking to assign the values in each tuple to variables.

    Your result for each row should print something like this out:

    ```
    100 USD = 83 EUR
    ```
    """)
    return


if __name__ == "__main__":
    app.run()
