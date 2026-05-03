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
    ### Solutions
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
    Your code uses a few functions in the `math` module here and there, but you also tend to use the `sin`, `cos` and `tan` functions and the `pi` constant very frequently.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write some import statements that you think would be helpful in this scenario.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First we'll import the `math` module itself, so we can use functions in there by prefixing the module name:
    """)
    return


@app.cell
def _():
    import math

    return (math,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So now we can access functions such as `sin` or `gcd` this way:
    """)
    return


@app.cell
def _(math):
    math.sin(math.pi)
    return


@app.cell
def _(math):
    math.gcd(10, 5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But since we use `pi`, `sin`, `cos`, and `tan` very frequently it might be nice not to have to always use the module name prefix - so, we'll import those symbols explicitly as well:
    """)
    return


@app.cell
def _():
    from math import pi, sin, cos, tan

    return pi, sin


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And now we can use those symbols directly:
    """)
    return


@app.cell
def _(pi, sin):
    sin(pi)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As well as retain the ability to reach into the `math` module for other functions:
    """)
    return


@app.cell
def _(math):
    math.asin(1)
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
    There is a library that we installed for our course called `matplotlib`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can certainly import that library using its full name, but whenever we need to reach into that module we need to type out `matplotlib.som_func` - since we use this library quite often, typing out `matplotlib` every time gets tiring.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write an import function that allows you to reference that module using the name `mpl` instead of the full name `matplotlib`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For this, we simply need to alias the module when we import it:
    """)
    return


@app.cell
def _():
    import matplotlib as mpl

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And now we can use the name `mpl` instead of the full original `matplotlib` name.
    """)
    return


if __name__ == "__main__":
    app.run()
