import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Closures
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Recall from the lecture that a **closure** is basically a function together with an environment that contains some values (the captured, or **free** variables).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start with a very simple example.
    """)
    return


@app.function
def outer(a, b):
    sum_ = a + b
    def inner():
        prod = a * b
        print(a, b, sum_, prod)
        return "You just called a closure!"
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see calling `outer` will return a **function** that also "captures" `a`, `b` and `sum_` where `a` and `b` were arguments passed to the `outer` function and `sum_`was a variable created in the `outer` function. Since `a`, `b` and `sum_` were not created in `inner` but are referenced, they need to come from somewhere - and that somewhere is the outer scope.
    """)
    return


@app.cell
def _():
    func = outer(2, 3)
    return (func,)


@app.cell
def _(func):
    func
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see `func` is actually the returned function `inner` - but it is a closure with free variables `a`, `b` and `sum_` that are `2`, `3` and `5` respectively.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we can now **call** `func`:
    """)
    return


@app.cell
def _(func):
    prod = func()
    return (prod,)


@app.cell
def _(prod):
    prod
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So we are basically using `outer` like a function **factory** which returns not just a function, but a closure, in this case.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In fact, we can look at the `__closure__` property of that closure:
    """)
    return


@app.cell
def _(func):
    func.__closure__
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Those **cells** are actually the captured variables - three integers in this case.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the following case we do **not** have a closure returned:
    """)
    return


@app.function
def outer_1(a, b):

    def inner(c):
        return c ** 2
    return inner


@app.cell
def _():
    func_1 = outer_1(1, 2)
    return (func_1,)


@app.cell
def _(func_1):
    func_1.__closure__
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see there were no "captured" (free) variables here.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So `func` is still the `inner` function, but that is not a closure (there are no variables that were "captured" by `inner`).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Closures serve a critical role in creating Python decorators that we will study in an upcoming chapter.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We saw a simple application of closures in the lecture:
    """)
    return


@app.function
def power(n):
    def inner(x):
        return x ** n
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see the `inner` function that is returned by calling `power` is going to be a closure, since `n` is a free variable in `inner`:
    """)
    return


@app.cell
def _():
    square = power(2)
    cube = power(3)
    return cube, square


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So `square` is a closure that will return `x**n` where `n` is fixed to `2`, and `cube` will be a closure that also returns `x ** n` but with `n` fixed to `3`:
    """)
    return


@app.cell
def _(square):
    square(4)
    return


@app.cell
def _(cube):
    cube(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Free variables in a closure can be any object, including a function.

    Let's see a completely useless example that illustrates this as simply as possible first:
    """)
    return


@app.function
def execute(func):
    def inner(a, b):
        result = func(a, b)
        return result
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So here, `inner` contains the free variable `func` , which we are going to use to pass a function. `inner` will be returned by `execute`, and we can call `func` by calling `inner` with some arguments:
    """)
    return


@app.function
def add(a, b):
    print('running add...')
    return a + b


@app.cell
def _():
    add_executor = execute(add)
    return (add_executor,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So `inner`'s free variable `func` is the `add` function.
    """)
    return


@app.cell
def _(add_executor):
    add_executor(2, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, `inner` is restrictive as to what arguments can be passed to it: two mandatory positional arguments, which means that `func` must also be a function that takes two positional arguments.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can this a lot more generic, by using `*args` and `**kwargs`:
    """)
    return


@app.function
def execute_1(func):

    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner


@app.cell
def _():
    def add_1(a, b, c):
        print('add...')
        return a + b + c

    def say_hello(name, *, formal=True):
        print('say_hello...')
        if formal:
            return f'Pleased to meet you, {name}'
        else:
            return f'Hi, {name}!'

    return add_1, say_hello


@app.cell
def _(add_1, say_hello):
    exec_add = execute_1(add_1)
    exec_greet = execute_1(say_hello)
    return exec_add, exec_greet


@app.cell
def _(exec_add):
    exec_add(1, 2, 3)
    return


@app.cell
def _(exec_greet):
    exec_greet('Michael', formal=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So by using `*args` and `**kwargs` we can basically handle passing arguments to any `func` - of course we have to pass the appropriate parameters for whichever `func` is in the closure.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So why is this useful?

    We'll come back to this with decorators, but consider a situation where we want to time how long certain functions take to run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We might have these two functions:
    """)
    return


@app.function
def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod = prod * i
    return prod


@app.function
def diagonal_matrix(rows, cols, *, diagonal=1):
     return [
         [
             diagonal if row == col else 0 
             for col in range(cols)
         ] 
         for row in range(rows)
     ]


@app.cell
def _():
    factorial(4)
    return


@app.cell
def _():
    diagonal_matrix(3, 3, diagonal=-1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So if we now want to time these two functions, we might write code like this:
    """)
    return


@app.cell
def _():
    from time import perf_counter

    return (perf_counter,)


@app.cell
def _(perf_counter):
    _start = perf_counter()
    result = factorial(10000)
    _end = perf_counter()
    print(f'elapsed: {_end - _start}')
    print(f'result = {result}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And if we want to time `diagonal_matrix` we wold have to repeat essentially the same code, except which function (and arguments) to use:
    """)
    return


@app.cell
def _(perf_counter):
    _start = perf_counter()
    result_1 = diagonal_matrix(10, 10, diagonal=-1)
    _end = perf_counter()
    print(f'elapsed: {_end - _start}')
    print(f'result = {result_1}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We really don't want to be writing timing code like this every time we need to time a function - we may want to do this hundreds of times in our program.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our goal is to use another function to wrap the timing code around our own function, execute the function, returning the result, and printing the timing information out.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could start with something like this:
    """)
    return


@app.cell
def _(perf_counter):
    def time_it(func, *args, **kwargs):
        _start = perf_counter()
        result = func(*args, **kwargs)
        _end = perf_counter()
        print(f'elapsed: {_end - _start}')
        return result

    return (time_it,)


@app.cell
def _(time_it):
    result_2 = time_it(factorial, 10000)
    return (result_2,)


@app.cell
def _(result_2):
    result_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can use the exact same function to time the diagonal matrix generator:
    """)
    return


@app.cell
def _(time_it):
    result_3 = time_it(diagonal_matrix, 10, 10, diagonal=-1)
    return (result_3,)


@app.cell
def _(result_3):
    result_3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But one thing that is not very nice about this, is that we have to remember to call `time_it(func)` every time we want to use `func`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, instead, let's use a closure to make this whole process a little more natural, and easier to read:
    """)
    return


@app.cell
def _(perf_counter):
    def time_it_1(func):

        def inner(*args, **kwargs):
            _start = perf_counter()
            result = func(*args, **kwargs)
            _end = perf_counter()
            print(f'elapsed: {_end - _start}')
            return result
        return inner

    return (time_it_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So now, we can create new functions that are the timed versions of our original functions:
    """)
    return


@app.cell
def _(time_it_1):
    timed_fact = time_it_1(factorial)
    timed_diagonal = time_it_1(diagonal_matrix)
    return timed_diagonal, timed_fact


@app.cell
def _(timed_fact):
    result_4 = timed_fact(5)
    return


@app.cell
def _(timed_fact):
    result_5 = timed_fact(100000)
    return


@app.cell
def _(timed_diagonal):
    result_6 = timed_diagonal(10, 10, diagonal=-1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll actually come back to this very example (and others) when we study decorators. But the above application of closures is a very common one in Python.
    """)
    return


if __name__ == "__main__":
    app.run()
