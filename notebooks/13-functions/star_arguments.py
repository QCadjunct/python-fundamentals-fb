import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### *args and **kwargs")
    return


@app.cell
def _():
    def my_func(*args):
        print(type(args), args)
    my_func(1)
    my_func(1, 2, 3)
    my_func()
    return (my_func,)


@app.cell
def _():
    def average(*values):
        try:
            return sum(values) / len(values)
        except ZeroDivisionError:
            return 0
    print(average(1, 2, 3))
    print(average())
    return (average,)


@app.cell
def _():
    def product(*values):
        prod = 1
        for value in values:
            prod *= value
        return prod
    print(product(1, 2, 3))
    print(product(1, 2, 3, 4))
    return (product,)


@app.cell
def _(average, product):
    l = [1, 2, 3, 4]
    print(average(*l))
    print(product(*l))
    return (l,)


@app.cell
def _():
    def func_kw(**kwargs):
        return kwargs["a"] + kwargs["b"]
    print(func_kw(a=1, b=2))
    return (func_kw,)


if __name__ == "__main__":
    app.run()
