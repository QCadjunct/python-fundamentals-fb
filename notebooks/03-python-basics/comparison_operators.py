import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    ### Comparison Operators
    """)
    return


@app.cell
def _():
    a1 = 10
    b1 = 10
    a1 == b1
    return (a1,)


@app.cell
def _():
    c1 = 10.0
    return (c1,)


@app.cell
def _(a1, c1):
    a1 == c1
    return


@app.cell
def _(a1, c1):
    a1 is c1
    return


@app.cell
def _():
    a2 = 10
    b2 = 10.0
    a2 == b2
    return a2, b2


@app.cell
def _(a2, b2):
    a2 is b2
    return


@app.cell
def _(a2, b2):
    id(a2), id(b2)
    return


@app.cell
def _():
    10 != 12
    return


@app.cell
def _():
    10.5 != 10.5
    return


@app.cell
def _():
    10 >= 5
    return


@app.cell
def _():
    10.5 < 100.2
    return


@app.cell
def _():
    10 <= 12.5
    return


@app.cell
def _():
    a3 = 1 + 1j
    b3 = 1 + 1j
    c3 = 2 + 2j
    a3 == b3
    return a3, b3


@app.cell
def _(a3, b3):
    a3 is b3, id(a3), id(b3)
    return


@app.cell
def _(mo):
    mo.md("""
    Complex numbers do not support ordering -- a < c raises TypeError
    """)
    return


@app.cell
def _():
    0.1 * 3 == 0.3
    return


@app.cell
def _():
    format(0.1 * 3, ".25f")
    return


@app.cell
def _():
    format(0.3, ".25f")
    return


@app.cell
def _():
    tol = 0.000_000_001
    a4 = 0.1 * 3
    b4 = 0.3
    print(format(a4, ".25f"))
    print(format(b4, ".25f"))
    print(abs(a4 - b4) < tol)
    return


@app.cell
def _():
    class VectorV1:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __add__(self, other):
            if isinstance(other, VectorV1):
                return VectorV1(self.x + other.x, self.y + other.y)
        def __repr__(self):
            return f"Vector({self.x}, {self.y})"

    v1a = VectorV1(1, 1)
    v2a = VectorV1(1, 1)
    v3a = VectorV1(2, 3)
    id(v1a), id(v2a), id(v3a)
    return v1a, v2a


@app.cell
def _(v1a, v2a):
    v1a is v2a
    return


@app.cell
def _(v1a, v2a):
    v1a == v2a
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
        def __eq__(self, other):
            if isinstance(other, VectorV2):
                return self.x == other.x and self.y == other.y
            return NotImplemented
        def __repr__(self):
            return f"Vector({self.x}, {self.y})"

    v1b = VectorV2(1, 1)
    v2b = VectorV2(1, 1)
    v3b = VectorV2(2, 3)
    return v1b, v2b, v3b


@app.cell
def _(v1b, v2b):
    v1b is v2b
    return


@app.cell
def _(v1b, v2b):
    v1b == v2b
    return


@app.cell
def _(v1b, v3b):
    v1b == v3b
    return


@app.cell
def _():
    class VectorV3:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __add__(self, other):
            if isinstance(other, VectorV3):
                return VectorV3(self.x + other.x, self.y + other.y)
        def __eq__(self, other):
            if isinstance(other, VectorV3):
                return self.x == other.x and self.y == other.y
            return NotImplemented
        def __lt__(self, other):
            if isinstance(other, VectorV3):
                return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
            raise TypeError(f"Cannot compare Vector with {type(other)}")
        def __repr__(self):
            return f"Vector({self.x}, {self.y})"

    v1c = VectorV3(1, 1)
    v2c = VectorV3(1, 1)
    v3c = VectorV3(2, 3)
    return v2c, v3c


@app.cell
def _(v2c, v3c):
    v2c < v3c
    return


@app.cell
def _():
    s = {1, 2, 3.14, 5, True}
    s
    return (s,)


@app.cell
def _(s):
    1 in s
    return


@app.cell
def _(s):
    100 not in s
    return


if __name__ == "__main__":
    app.run()
