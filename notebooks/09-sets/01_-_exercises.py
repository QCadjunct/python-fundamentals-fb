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
    #### Question 1
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You are given a list of strings from which you want to generate all the unique values.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, if you were given this list:

    ```
    ['a', 'A', 'b', 'B', 'B', 'A', 'a', 'c']
    ```

    your result should contain these values:

    ```
    ['a', 'A', 'b', 'B', 'c']
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that the order of the elements in the resulting list is not important.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can use this list for this exercise.
    """)
    return


@app.cell
def _():
    l = ['AAPL', 'AAPL', 'Aapl', 'aapl', 'MSFT']
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
    Using the same data we saw in Question 1, the goal is to find all the unique values in a **case-insensitive** fashion.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, `AAPL`, `Aapl` and `aapl` should each be considered to be the same value.
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
    Given this data structure:
    """)
    return


@app.cell
def _():
    data = {
        'd1': {'a': 1, 'b': 2, 'c': 3},
        'd2': {'b': 20, 'c': 30, 'd': 40},
        'd3': {'d': 100, 'x': 200}
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Find all the unique keys in the sub-dictionaries.

    In this case above, your result should be:

    ```
    {'a', 'b', 'c', 'd', 'x'}
    ```

    Of course, the order in the result is irrelevant (there is no ordering in sets).
    """)
    return


if __name__ == "__main__":
    app.run()
