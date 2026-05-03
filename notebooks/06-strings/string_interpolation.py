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
    ### String Interpolation
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Often we want to "interpolate" values into strings.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here I'll show you two mechanisms, the `format()` method and **formatted strings**, so called **f-strings**.
    """)
    return


@app.cell
def _():
    open_, high, low, close = 98, 100, 95, 99
    return close, high, low, open_


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: I use `open_` instead `open` as a symbol because `open` is actually a built-in function in Python. Although we can redefine it, if we do so we won't be able to open files later :-)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, we want to generate a string that contains these values - maybe for display to our users, or maybe to save into a CSV file we are creating.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can use the `format()` method this way:
    """)
    return


@app.cell
def _(close, high, low, open_):
    'open: {}, high: {}, low: {}, close: {}'.format(open_, high, low, close)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The only thing is that we need to make sure we list the arguments in the same order as we are interpolating them into the string.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now this may at times be prone to errors - in that case, there is a variant where we can name the argument in the string, and used named arguments in the `format` method (we'll get to named arguments later in this course):
    """)
    return


@app.cell
def _():
    bid = 1.5760
    ask = 1.5763
    return ask, bid


@app.cell
def _(ask, bid):
    'bid: {bid}, ask: {ask}, spread: {spread}'.format(bid=bid, ask=ask, spread=(ask - bid))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is sometimes easier than remembering the order of the variables, because this works just as well:
    """)
    return


@app.cell
def _(ask, bid):
    'bid: {bid}, ask: {ask}, spread: {spread}'.format(spread=(ask - bid), bid=bid, ask=ask)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You'll notice that the displayed value for the spread is a little too much (plus it's not exact, as we already know when dealing with floats). We can specify a format Python should use to display the float:
    """)
    return


@app.cell
def _(ask, bid):
    'bid: {bid:.4f}, ask: {ask:.4f}, spread: {spread:.4f}'.format(spread=(ask - bid), bid=bid, ask=ask)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The other advantage of used named variables is that they can be used more than once in the same string:
    """)
    return


@app.cell
def _():
    '{a} + {b} = {b} + {a}'.format(a=10, b=20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we had wanted to use just positional arguments, we would have to do this:
    """)
    return


@app.cell
def _():
    '{} + {} = {} + {}'.format(10, 20, 20, 10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Starting in Python 3.6, there is another way to do the same thing - f-strings.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    These f-strings directly interpolate existing symbols into our string - this means they must exist before we define the f-string:
    """)
    return


@app.cell
def _():
    a = 10
    b = 20
    return a, b


@app.cell
def _(a, b):
    f'{a} + {b} = {b} + {a}'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In fact, we can even include expressions, not just symbols in the interpolation:
    """)
    return


@app.cell
def _(a, b):
    f'{a} + {b} = {a + b}'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's go back to our open-high-low-close example:
    """)
    return


@app.cell
def _(close, high, low, open_):
    f'open: {open_}, high: {high}, low: {low}, close: {close}'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And our spread example:
    """)
    return


@app.cell
def _(ask, bid):
    f'ask: {ask}, bid: {bid}, spread: {ask - bid}'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see we also have that visual representation issue, so we rectify it using the same approach as before:
    """)
    return


@app.cell
def _(ask, bid):
    f'ask: {ask:.4f}, bid: {bid:.4f}, spread: {(ask - bid):.4f}'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Technically we don't even need the parentheses in the last interpolated expression:
    """)
    return


@app.cell
def _(ask, bid):
    f'ask: {ask:.4f}, bid: {bid:.4f}, spread: {ask - bid:.4f}'
    return


if __name__ == "__main__":
    app.run()
