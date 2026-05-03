import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Tuples")
    return


@app.cell
def _():
    t1 = (1, 2, 3)
    type(t1)
    return (t1,)


@app.cell
def _():
    t2 = (1,)
    type(t2)
    return (t2,)


@app.cell
def _():
    t3 = 1, 2, 3
    type(t3)
    return (t3,)


@app.cell
def _():
    t4 = (1, 2, 3)
    try:
        t4[0] = 100
    except TypeError as e:
        print(f"TypeError: {e}")
    return (t4,)


@app.cell
def _():
    t5 = ([1, 2], [3, 4])
    t5[0].append(99)
    t5
    return (t5,)


@app.cell
def _():
    t6 = (1, 2, 3)
    a6, b6, c6 = t6
    print(a6, b6, c6)
    return a6, b6, c6, t6


@app.cell
def _():
    a7 = 10
    b7 = 20
    a7, b7 = b7, a7
    print(a7, b7)
    return a7, b7


if __name__ == "__main__":
    app.run()
