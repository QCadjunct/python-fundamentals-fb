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
    ### map
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `map()` function creates an iterator that applies a given function to an iterable, element by element.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see a simple example of this:
    """)
    return


@app.cell
def _():
    data = ['a', 'ab', 'abc', 'abcd']
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Suppose we want to get the length of each string in `data`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could certainly do it this way:
    """)
    return


@app.cell
def _(data):
    lengths = [len(element) for element in data]
    return (lengths,)


@app.cell
def _(lengths):
    lengths
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One disadvantage here is that we created a list.

    If we don't need to iterate over this multiple times (or it's small and computationally cheap), we could use a generator expression instead:
    """)
    return


@app.cell
def _(data):
    lengths_1 = (len(element) for element in data)
    return (lengths_1,)


@app.cell
def _(lengths_1):
    list(lengths_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But we could also use the `map` function, which offers a slightly cleaner syntax:
    """)
    return


@app.cell
def _(data):
    lengths_2 = map(len, data)
    return (lengths_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now the result of `map` is not a list, or a tuple, but an iterator.
    """)
    return


@app.cell
def _(lengths_2):
    lengths_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can iterate through it:
    """)
    return


@app.cell
def _(lengths_2):
    list(lengths_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But of course, the iterator is now exhausted (this is similar to the `zip` function):
    """)
    return


@app.cell
def _(lengths_2):
    list(lengths_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It's important to understand that these kinds of iterators/generators are far more efficient than building a list like we did with the comprehension just now.
    """)
    return


if __name__ == "__main__":
    app.run()
