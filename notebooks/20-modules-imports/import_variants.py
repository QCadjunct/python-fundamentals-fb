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
    ### Import Variants
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So far we have seen two variants of the import statement:
    """)
    return


@app.cell
def _():
    import math

    return (math,)


@app.cell
def _():
    import random as rnd

    return (rnd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This not only loaded the `math` and `random` modules into memory (as objects), but also create variables in our local namespace with the module name or the alias if we specified one:
    """)
    return


@app.cell
def _(math):
    math
    return


@app.cell
def _(rnd):
    rnd
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can then use attributes inside those modules (objects) by using standard dot notation:
    """)
    return


@app.cell
def _(math):
    math.sqrt(2)
    return


@app.cell
def _(rnd):
    rnd.randint(1, 6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But what if we are only interested in a few attributes inside those modules?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If that's the case we can import just those attributes, and avoid having to use dot notation everywhere.
    """)
    return


@app.cell
def _():
    from math import sqrt

    return (sqrt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So this loaded `math` (which was actually already loaded because we imported it earlier), and took `sqrt` from that module and created a variable of that same name pointing to it.
    """)
    return


@app.cell
def _(sqrt):
    sqrt(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is actually almost the same as if we have done this:
    """)
    return


@app.cell
def _(math):
    sqrt_1 = math.sqrt
    return (sqrt_1,)


@app.cell
def _(sqrt_1):
    sqrt_1(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The main difference when we write:
    """)
    return


@app.cell
def _():
    from fractions import Fraction
    import fractions

    return (Fraction, fractions)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    is that `fractions` was loaded, a symbol named `Fraction` was created in our namespace that points to that attribute inside `fractions`, but `fractions` was not assigned to a symbol in our local namespace:
    """)
    return


@app.cell
def _(Fraction):
    Fraction(1, 2)
    return


@app.cell
def _(fractions):
    fractions.Fraction(1, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In fact, we can combine those two variants as follows:
    """)
    return


@app.cell
def _():
    from math import pi

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That way, if we use `sqrt` and `pi` very often in our code, we can do so without using `math.sqrt` or `math.pi` every time, just `sqrt` and `pi`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But for when we need to use say the `gcd` function once in a while, we can call it using dot notation:
    """)
    return


@app.cell
def _(math):
    math.gcd(15, 25)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, if all we need is `sqrt` and `pi`, then we just import those and don't do `import math` at all.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But in either case, the `math` module, as a whole, is loaded from file into memory.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When we write:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    the **entire** `math` module is **still** loaded - it's just what variables are put into our namespace that change.
    """)
    return


if __name__ == "__main__":
    app.run()
