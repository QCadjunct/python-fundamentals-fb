import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Lists")
    return


@app.cell
def _():
    l1 = [10, 20, 30, 40, 50]
    type(l1)
    return (l1,)


@app.cell
def _(l1):
    l1[0]
    return


@app.cell
def _(l1):
    l1[-1]
    return


@app.cell
def _(l1):
    len(l1)
    return


@app.cell
def _():
    l2 = [1, 2, 3]
    l2[-1]
    return (l2,)


@app.cell
def _():
    l3 = [1, 2, 3, 4, 5, 6]
    l3[-1]
    return (l3,)


@app.cell
def _():
    l_mut = [1, 2, 30, 4, 5]
    l_mut[2] = 3
    l_mut[-2] = 40
    l_mut
    return (l_mut,)


if __name__ == "__main__":
    app.run()
