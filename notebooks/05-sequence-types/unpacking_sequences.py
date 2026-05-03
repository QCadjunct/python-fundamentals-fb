import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Unpacking Sequences")
    return


@app.cell
def _():
    l1 = [1, 2, 3]
    a1, b1, c1 = l1
    print(a1, b1, c1)
    return a1, b1, c1, l1


@app.cell
def _():
    l2 = [1, 2, 3, 4, 5]
    a2, *b2, c2 = l2
    print(a2, b2, c2)
    return a2, b2, c2, l2


@app.cell
def _():
    a3 = 10
    b3 = 20
    a3, b3 = b3, a3
    print(a3, b3)
    return a3, b3


@app.cell
def _():
    data = [(1, 2), (3, 4), (5, 6)]
    for a4, b4 in data:
        print(a4, b4)
    return a4, b4, data


if __name__ == "__main__":
    app.run()
