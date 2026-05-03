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
    ### The `range` Function
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `range()` function is a built-in Python function that we can use to create ranges of integer values.
    """)
    return


@app.cell
def _():
    range(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The return value is not a list or a tuple, it is a special `range` object:
    """)
    return


@app.cell
def _():
    type(range(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This range object is **iterable** - i.e. we can iterate over it's elements, and we'll see how iteration works in this chapter.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For now, we can see the integers that would be returned during iteration by converting that range object to a list or a tuple:
    """)
    return


@app.cell
def _():
    tuple(range(10))
    return


@app.cell
def _():
    list(range(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Essentially the `list()` / `tuple()` functions iterated over the range object and made a list/tuple out of those integers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `range` function has three flavors.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we only specify a single argument, then Python takes it to mean the end (exclusive), starting with `0`:
    """)
    return


@app.cell
def _():
    list(range(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we specify two arguments, then Python interprets that as the `start` and `end` (exclusive) values:
    """)
    return


@app.cell
def _():
    list(range(2, 6))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You'll note that the length of the iterable is `end - start`:
    """)
    return


@app.cell
def _():
    len(range(100, 105))
    return


@app.cell
def _():
    len(range(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we specify three values, then Python interprets that as the `start`, `end` and `step`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, to create a range of even numbers starting at `2`, and ending at `10` (exclusive), we would do this:
    """)
    return


@app.cell
def _():
    list(range(2, 10, 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we wanted to include `10`, we'd just have to remember to go `1` beyond the value `10`:
    """)
    return


@app.cell
def _():
    list(range(2, 11, 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also specify negative step sizes, but in this case we have to make our start/end values appropriate (i.e. end <= start):
    """)
    return


@app.cell
def _():
    list(range(10, 2, -2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And again, the end value, `2` in this case, is exclusive.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The range function is extremely useful for repeating code a set number of times, and knowing at each iteration which iteration number we are in. We'll see this in the next videos.
    """)
    return


if __name__ == "__main__":
    app.run()
