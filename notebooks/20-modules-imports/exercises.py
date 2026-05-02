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


if __name__ == "__main__":
    app.run()
