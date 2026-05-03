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
    #### Question 1
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given these two lists:
    """)
    return


@app.cell
def _():
    widgets = [f'w{i}' for i in range(1, 21)]
    skus = [f'sku{i}' for i in range(1, len(widgets) + 1)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that uses the `zip` function to generate a dictionary with keys from the `widgets`, and values from the `skus`, i.e.:

    ```
    {
      'w1': 'sku1',
      'w2': 'sku2',
      ...
      'w20': 'sku20'
    }
    ```
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
    Given the following data:
    """)
    return


@app.cell
def _():
    suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
    ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that given those two inputs, returns a list with all 52 cards, consisting of tuples `(rank, suit)`, i.e.

    ```
    [
      [('2', 's'), ('3', 's'), ..., ('K', 's'), ('A', 's')],
      [('2', 'h'), ('3', 'h'), ..., ('K', 'h'), ('A', 'h')],
      ...
    ]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 3
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that receives two arguments:
    - a list of numbers
    - a keyword-only argument `reverse` that defaults to `False` and indicates an ascending sort, but a value of `True` indicates a descending sort
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your function should return three values:
    - a list of the numbers, but sorted (ascending/descending depending on value of `reverse`)
    - the minimum value in the list (this is not affected by the value of `reverse`)
    - the maximum value in the list (this is not affected by the value of `reverse`)
    """)
    return


if __name__ == "__main__":
    app.run()
