import marimo

__generated_with = "0.23.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Passing and Returning Functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can pass functions as arguments to other functions.
    """)
    return


@app.function
def add(a, b):
    return a + b


@app.function
def greet(name):
    return f'Hello, {name}'


@app.function
def apply(func, *args):
    result = func(*args)
    return result


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice how the `apply` function takes in a variable numnber of arguments - this allows us to use `apply` to call `func` with whatever parameters we want to pass in. We pass those same argument straight into whatever `func` is.
    """)
    return


@app.cell
def _():
    apply(add, 2, 3)
    return


@app.cell
def _():
    apply(greet, 'Python')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can even use lambdas, not just functions defined using `def`:
    """)
    return


@app.cell
def _():
    apply(lambda a, b, c: a + b + c, 10, 20, 30)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also return functions from functions:
    """)
    return


@app.cell
def _():
    def mult(a, b):
        return a * b

    def power(a, b):
        return a ** b

    return mult, power


@app.cell
def _(mult, power):
    def choose_operator(name):
        if name == 'add':
            return add
        if name == 'mult':
            return mult
        if name == 'power':
            return power

    return (choose_operator,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here we are returning functions that were created in the module itself.
    """)
    return


@app.cell
def _(choose_operator):
    op = choose_operator('add')
    op(2, 3)
    return


@app.cell
def _(choose_operator):
    op_1 = choose_operator('mult')
    op_1(2, 3)
    return


@app.cell
def _(choose_operator):
    choose_operator('power')(2, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    More often, the function that we return from a function has been created inside the function itself.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So we could re-write our previous example as follows:
    """)
    return


@app.function
def choose_operator_1(name):

    def add(a, b):
        return a + b

    def mult(a, b):
        return a * b

    def power(a, b):
        return a ** b
    if name == 'add':
        return add
    if name == 'mult':
        return mult
    if name == 'power':
        return power


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And it would work the same way as before:
    """)
    return


@app.cell
def _():
    choose_operator_1('power')(2, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could also return lambdas:
    """)
    return


@app.function
def choose_operator_2(name):
    if name == 'add':
        return lambda a, b: a + b
    if name == 'mult':
        return lambda a, b: a * b
    if name == 'power':
        return lambda a, b: a ** b


@app.cell
def _():
    op_2 = choose_operator_2('mult')
    return (op_2,)


@app.cell
def _(op_2):
    op_2
    return


@app.cell
def _(op_2):
    op_2(2, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now all these examples have been very simplistic, just so we get used to passing functions to, and returning functions from, other functions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here's a somewhat more practical example.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We want to time how long a function call takes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's say we have the following functions:
    """)
    return


@app.function
def in_list(l, element):
    return element in l


@app.function
def in_tuple(t, element):
    return element in t


@app.function
def in_set(s, element):
    return element in s


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To time how long each one takes to run we could do this:
    """)
    return


@app.cell
def _():
    from time import perf_counter

    return (perf_counter,)


@app.cell
def _():
    n = 10_000_000
    l = list(range(n))
    t = tuple(range(n))
    s = set(range(n))
    return l, s, t


@app.cell
def _():
    x = 5_000_000
    return (x,)


@app.cell
def _(l, perf_counter, x):
    _start = perf_counter()
    in_list(l, x)
    _end = perf_counter()
    print(_end - _start)
    return


@app.cell
def _(perf_counter, t, x):
    _start = perf_counter()
    in_tuple(t, x)
    _end = perf_counter()
    print(_end - _start)
    return


@app.cell
def _(perf_counter, s, x):
    _start = perf_counter()
    in_set(s, x)
    _end = perf_counter()
    print(_end - _start)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But we had to repeat this timing code multiple times.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Instead, let's write a function to do all this for us:
    """)
    return


@app.cell
def _(perf_counter):
    def time_it(func, *args):
        _start = perf_counter()
        result = func(*args)
        _end = perf_counter()
        print(f'Elapsed: {_end - _start}')
        return result

    return (time_it,)


@app.cell
def _(l, time_it, x):
    time_it(in_list, l, x)
    return


@app.cell
def _(s, time_it, x):
    time_it(in_set, s, x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Essentially our `time_it` function *wrapped* some timing code around the function call we want to make.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This concept, and one more we'll study soon (closures), is going to form the basis of a concept called decorators.
    """)
    return


if __name__ == "__main__":
    app.run()
