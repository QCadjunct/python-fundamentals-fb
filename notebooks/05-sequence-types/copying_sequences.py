import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from copy import deepcopy

    return deepcopy, mo


@app.cell
def _(mo):
    mo.md("""
    ### Copying Sequences
    """)
    return


@app.cell
def _():
    m1a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    m2a = m1a.copy()
    m1a.append("abc")
    print("m1a:", m1a)
    print("m2a:", m2a)
    return


@app.cell
def _():
    m1b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    m2b = m1b.copy()
    print("same nested?", m1b[0] is m2b[0])
    m1b[0].append(100)
    print("m1b:", m1b)
    print("m2b:", m2b)
    return


@app.cell
def _(deepcopy):
    m1c = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    m2c = deepcopy(m1c)
    print("same nested?", m1c[0] is m2c[0])
    m1c[0].append(100)
    print("m1c:", m1c)
    print("m2c:", m2c)
    return


@app.cell
def _():
    t1a = (10, [1, 2], "abc")
    t2a = t1a[:]
    print("t1a is t2a:", t1a is t2a)
    return


if __name__ == "__main__":
    app.run()
