import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from timeit import timeit

    return mo, timeit


@app.cell
def _(mo):
    mo.md("""
    ### Generator Expressions
    """)
    return


@app.cell
def _():
    squares_1 = (i ** 2 for i in range(5))
    for v1 in squares_1:
        print(v1)
    return (squares_1,)


@app.cell
def _(squares_1):
    for v2 in squares_1:
        print("iterating again...")
    print("(nothing - exhausted)")
    return


@app.cell
def _(mo):
    mo.md("""
    List comprehension IS re-usable:
    """)
    return


@app.cell
def _():
    l = [v ** 2 for v in range(5)]
    for v3 in l:
        print(v3)
    for v4 in l:
        print(v4)
    return


@app.cell
def _():
    squares_2 = (i ** 2 for i in range(5))
    print(list(squares_2))
    print(list(squares_2))
    return


@app.cell
def _():
    squares_3 = (i ** 2 for i in range(5))
    print(iter(squares_3) is squares_3)
    try:
        while True:
            print(next(squares_3))
    except StopIteration:
        print("finished")
    return


@app.cell
def _():
    squares_4 = (i ** 2 for i in range(5))
    print(3 in squares_4)
    print(list(squares_4))
    return


@app.cell
def _(timeit):
    t_list = timeit("[i**2 for i in range(1_000_000)]", number=1)
    t_gen = timeit("(i**2 for i in range(1_000_000))", number=1)
    print(f"list: {t_list:.4f}s  gen: {t_gen:.6f}s")
    return


if __name__ == "__main__":
    app.run()
