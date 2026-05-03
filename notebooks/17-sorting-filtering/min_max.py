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
    ### min and max
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When we use `sorted` we can specify a **key** function to use for the sort keys.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same thing happens with `min` and `max` - the min and max is relative to some sort, and as we just saw we can specify the sort keys (via a key function) to customize the sort.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see a simple example first:
    """)
    return


@app.cell
def _():
    data = [1, -2, 3, -4, 5, -6]
    return (data,)


@app.cell
def _(data):
    min(data), max(data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This `min` and `max` worked using a natural sort (i.e. sorting by the numbers themselves).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But what if we wanted to find the min (or max) for an iterable using a custom sort key?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can just give `min` (or `max`) that sort key function:
    """)
    return


@app.cell
def _(data):
    min(data, key=abs)
    return


@app.cell
def _(data):
    max(data, key=abs)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here we could use `abs` directly since it is a function, but we ciould use a lambda expression, or a full fledged `def` function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's go back to one of the examples we had when we studied sorting:
    """)
    return


@app.cell
def _():
    data_1 = [{'date': '2020-04-09', 'symbol': 'AAPL', 'open': 268.7, 'high': 270.04, 'low': 264.7, 'close': 267.99}, {'date': '2020-04-09', 'symbol': 'MSFT', 'open': 166.36, 'high': 167.37, 'low': 163.33, 'close': 165.14}, {'date': '2020-04-09', 'symbol': 'AMZN', 'open': 2044.3, 'high': 2053.0, 'low': 2017.66, 'close': 2042.76}, {'date': '2020-04-09', 'symbol': 'FB', 'open': 175.9, 'high': 177.08, 'low': 171.57, 'close': 175.19}]
    return (data_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we want to find the "smallest" element in our data, with ordering key defined by the `low` of each item:
    """)
    return


@app.cell
def _(data_1):
    min(data_1, key=lambda d: d['low'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So this is basically identical to how we used a key function for `sorted`.
    """)
    return


if __name__ == "__main__":
    app.run()
