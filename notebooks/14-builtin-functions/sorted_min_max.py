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
    ### Sorted, min and max
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In this video we are only going to look at numbers and strings, using the natural ordering that exists for those two types.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll come back to `sorted`, `min` and `max` again later.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start with an iterable of numbers - it could be a tuple, a list, or even a set:
    """)
    return


@app.cell
def _():
    l = [1, 10, 2, 9, 3, 8]
    t = (1, 10, 2, 9, 3, 8)
    return l, t


@app.cell
def _(l):
    sorted(l)
    return


@app.cell
def _(t):
    sorted(t)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You'll notice that in each case we get a `list` back.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note also that this is not an in-place sort - in the sense that the original iterable was not modified in any way:
    """)
    return


@app.cell
def _(l):
    l
    return


@app.cell
def _(t):
    t
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The default sort order is ascending (from smallest to largest), but we can change this to descending by specifying a key-word-only argument:
    """)
    return


@app.cell
def _(l):
    sorted(l, reverse=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Strings also have a natural ordering, based on the character code of each character in the string. But this means string sorts are case sensitive:
    """)
    return


@app.cell
def _():
    sorted(('a', 'z', 'b', 'y', 'c', 'x'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But this may seem odd:
    """)
    return


@app.cell
def _():
    sorted({'a', 'A', 'b', 'B', 'x', 'X'})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is because the character code for `A` is smaller than the character code for `a`:
    """)
    return


@app.cell
def _():
    'A' < 'a'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and in fact:
    """)
    return


@app.cell
def _():
    'Z' < 'a'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So,
    """)
    return


@app.cell
def _():
    sorted(['atom', 'apple', 'Zebra'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll come back to sorting later and see how we can change this default behavior.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `min` and `max` functions are very much related to sorting.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To find the smallest element in a list of numbers we could do this:
    """)
    return


@app.cell
def _():
    l_1 = [1, 10, 2, 9, 3, 8]
    return (l_1,)


@app.cell
def _(l_1):
    sorted_ascending = sorted(l_1)
    return (sorted_ascending,)


@app.cell
def _(sorted_ascending):
    smallest_element = sorted_ascending[0]
    return (smallest_element,)


@app.cell
def _(smallest_element):
    smallest_element
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Instead of doing this, we can use `min`:
    """)
    return


@app.cell
def _(l_1):
    min(l_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we pas an empty iterable to the `min` or `max` functions, we will get an exception - it is not possible to find the smallest element of an empty collection after all!
    """)
    return


@app.cell
def _():
    try:
        min([])
    except ValueError as ex:
        print('ValueError:', ex)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we want, we can specify a `default` value, a keyword-only argument to use as the min/max if the iterable is empty:
    """)
    return


@app.cell
def _():
    min([], default=0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `min` function takes a single iterable as a positional argument, but it can also handle *multiple* positional arguments instead:
    """)
    return


@app.cell
def _():
    min(1, 10, 2, 9, 3, 8)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, using this variant means that using a `default` makes no sense:
    """)
    return


@app.cell
def _():
    min(1, 10, default=0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `max` works exactly the same way.
    """)
    return


if __name__ == "__main__":
    app.run()
