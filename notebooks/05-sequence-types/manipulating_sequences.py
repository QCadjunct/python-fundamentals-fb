import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Manipulating Sequences")
    return


@app.cell
def _():
    l1 = [1, 2, 3]
    l1 + [4, 5, 6]
    return (l1,)


@app.cell
def _():
    l2 = [1, 2, 3]
    l2.append(4)
    l2
    return (l2,)


@app.cell
def _():
    l3 = [1, 2, 3]
    l3.insert(1, 100)
    l3
    return (l3,)


@app.cell
def _():
    l4 = [1, 2, 3]
    l4.extend([4, 5, 6])
    l4
    return (l4,)


@app.cell
def _():
    l5 = [1, 2, 3, 2, 4]
    l5.remove(2)
    l5
    return (l5,)


@app.cell
def _():
    l6 = [1, 2, 3, 4, 5]
    popped = l6.pop()
    print(popped, l6)
    return l6, popped


@app.cell
def _():
    l7 = [1, 2, 3, 4, 5]
    del l7[2]
    l7
    return (l7,)


@app.cell
def _():
    l8 = [3, 1, 4, 1, 5, 9]
    l8.sort()
    l8
    return (l8,)


@app.cell
def _():
    l9 = [3, 1, 4, 1, 5, 9]
    l9.reverse()
    l9
    return (l9,)


@app.cell
def _():
    l10 = [1, 2, 2, 3, 2, 4]
    l10.count(2)
    return (l10,)


if __name__ == "__main__":
    app.run()
