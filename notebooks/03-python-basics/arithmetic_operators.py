import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    ### Arithmetic Operators
    """)
    return


@app.cell
def _():
    1 + 0.5
    return


@app.cell
def _():
    1.0 + 0.5
    return


@app.cell
def _():
    2 * 1.125
    return


@app.cell
def _():
    18 / 4
    return


@app.cell
def _():
    2 ** 8
    return


@app.cell
def _():
    2 ** (-8)
    return


@app.cell
def _():
    4.0 ** 0.5
    return


@app.cell
def _():
    (-4) ** 0.5
    return


@app.cell
def _():
    c = (-4) ** 0.5
    c
    return (c,)


@app.cell
def _(c):
    c.real
    return


@app.cell
def _(c):
    c.imag
    return


@app.cell
def _(mo):
    mo.md("""
    Data types define operator behavior via dunder methods: __add__ for +, __mul__ for *, etc.
    """)
    return


@app.cell
def _():
    1 + 2
    return


@app.cell
def _():
    a = 1
    a.__add__(2)
    return


@app.cell
def _(mo):
    mo.md("""
    Vector class WITHOUT __add__ -- addition will raise TypeError:
    """)
    return


@app.cell
def _():
    class VectorV1:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __repr__(self):
            return f"Vector({self.x}, {self.y})"

    v1a = VectorV1(1, 1)
    v2a = VectorV1(2, 3)
    return


@app.cell
def _(mo):
    mo.md("""
    Without __add__, attempting v1 + v2 raises TypeError.
    Now we define __add__ to enable vector addition:
    """)
    return


@app.cell
def _():
    class VectorV2:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __add__(self, other):
            if isinstance(other, VectorV2):
                return VectorV2(self.x + other.x, self.y + other.y)
        def __repr__(self):
            return f"Vector({self.x}, {self.y})"

    v1b = VectorV2(1, 1)
    v2b = VectorV2(2, 3)
    return v1b, v2b


@app.cell
def _(v1b, v2b):
    v1b + v2b
    return


if __name__ == "__main__":
    app.run()
