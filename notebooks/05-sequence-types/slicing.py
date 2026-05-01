import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Slicing")
    return


@app.cell
def _():
    s1 = "Python"
    print(s1[0:3], s1[2:], s1[:3], s1[:], s1[::-1])
    return (s1,)


@app.cell
def _():
    l1 = [1, 2, 3, 4, 5]
    print(l1[1:3], l1[::2])
    return (l1,)


@app.cell
def _():
    l2a = [1, 2, 3, 4, 5]
    l2b = l2a[:]
    print(l2a is l2b)
    return l2a, l2b


@app.cell
def _():
    s2 = "abcdefghij"
    print(s2[::2], s2[1::2])
    return (s2,)


@app.cell
def _():
    l3 = [1, 2, 3, 4, 5]
    l3[1:3] = [20, 30]
    l3
    return (l3,)


@app.cell
def _():
    l4 = [1, 2, 3, 4, 5]
    del l4[1:3]
    l4
    return (l4,)


@app.cell
def _():
    a1 = [1, 2, 3, 4, 5]
    print(a1[::-1], a1[3:0:-1])
    return (a1,)


if __name__ == "__main__":
    app.run()
