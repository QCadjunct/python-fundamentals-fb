import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Lambda Functions")
    return


@app.cell
def _():
    f_add = lambda a, b: a + b
    print(f_add(2, 3))
    return (f_add,)


@app.cell
def _():
    f_max_1 = lambda a, b, c: max(a, b, c)
    def f_max_2(a, b, c):
        return max(a, b, c)
    print(f_max_1(1, 2, 3), f_max_2(1, 2, 3))
    return f_max_1, f_max_2


@app.cell
def _():
    f_matrix = lambda rows, cols: [
        [1 if row == col else 0 for col in range(cols)]
        for row in range(rows)
    ]
    print(f_matrix(3, 3))
    return (f_matrix,)


@app.cell
def _():
    f_default = lambda a=0, b=2: a * b
    print(f_default(10))
    print(f_default("a"))
    return (f_default,)


@app.cell
def _():
    f_star = lambda a, *args: a * max(args)
    print(f_star(10, 1, 2, -1))
    return (f_star,)


if __name__ == "__main__":
    app.run()
