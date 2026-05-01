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
    Alongside this note book, four CSV files are specified (one is in fact a TSV file).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For each file, load it using the CSV module, and find the smallest and largest numbers in the data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All these files contain just lists of numbers - with the exception of a possible header row
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
    Given this data structure consisting of a list of dictionaries, write a function that will write this data out to a file, where the column headers (in the first row) are based on the dictionary keys, and the values are flattened out to one row per dictionary (under the corresponding column header).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that not all dictionaries contain all the same keys, nor are the keys necessarily in the same order when present.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For "missing" values, your function should just write an empty string.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, given this `data`:
    """)
    return


@app.cell
def _():
    data = [
        {'a': '1_a', 'b': '1_b', 'c': '1_c'},
        {'c': '2_c', 'd': '2_d'},
        {'a': '3_a', 'c': '3_c', 'e': '3_e'}
    ]
    return


app._unparsable_cell(
    r"""
    Your output file should look like this:
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```
    a,b,c,d,e
    1_a,1_b,1_c,,,
    ,,2_c,2_d,
    3_a,,3_c,,3_e
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The order of the columns and rows is not important - as long as they match up with respective column headers.
    """)
    return


if __name__ == "__main__":
    app.run()
