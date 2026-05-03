import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Strings")
    return


@app.cell
def _():
    a1 = "hello"
    b1 = "Python"
    type(a1), type(b1)
    return a1, b1


@app.cell
def _():
    s1 = "Python rocks!"
    s1[0], s1[-1], len(s1)
    return (s1,)


@app.cell
def _(s1):
    try:
        s1[0] = "x"
    except TypeError as e:
        print(f"TypeError: {e}")
    return


@app.cell
def _():
    s2 = str()
    type(s2), len(s2)
    return (s2,)


@app.cell
def _():
    t1 = 1, 2, 3
    s3 = str(t1)
    s3
    return s3, t1


@app.cell
def _():
    s4 = "Python"
    l1 = list(s4)
    l2 = list("abcdef")
    print(l1)
    print(l2)
    return l1, l2, s4


@app.cell
def _():
    s5 = "=" * 10
    s6 = "Python-" * 4
    print(s5)
    print(s6)
    return s5, s6


@app.cell
def _():
    l3 = [0] * 10
    l3
    return (l3,)


@app.cell
def _(mo):
    mo.md("Caveat: repeated mutable element is the SAME object. Use list comprehension instead:")
    return


@app.cell
def _():
    m_safe = [[0, 0, 0] for _ in range(3)]
    m_safe[0][0] = 99
    print(m_safe)
    return (m_safe,)


if __name__ == "__main__":
    app.run()
