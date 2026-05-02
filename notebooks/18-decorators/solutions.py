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
    ### Solutions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 1
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a decorator that can be used to print out how long a function takes to run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start with the "standard" skeleton for a decorator.
    """)
    return


@app.function
def logged(f):
    def inner(*args, **kwargs):
        result = f(*args, **kwargs)
        return result
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, we just need to time and print out the timing before returning the result of the function call.
    """)
    return


@app.cell
def _():
    from time import perf_counter

    def logged_1(f):

        def inner(*args, **kwargs):
            start = perf_counter()
            result = f(*args, **kwargs)
            end = perf_counter()
            print(f'elapsed: {end - start} secs')
            return result
        return inner

    return (logged_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And let's try it out on a few functions:
    """)
    return


@app.cell
def _(logged_1):
    import math

    @logged_1
    def norm(x, y):
        return math.sqrt(x ** 2 + y ** 2)

    @logged_1
    def find_index_min(seq):
        min_ = min(seq)
        return seq.index(min_)

    return find_index_min, norm


@app.cell
def _(norm):
    norm(3, 4)
    return


@app.cell
def _(find_index_min):
    find_index_min([3, 2, 1, 4, 5])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 2
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have several functions in our code that perform some calculations and return a numeric result, possibly `float`, `int` or even `Decimal`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We actually want to make sure that all results from each of these functions are rounded to some number of digits after the decimal point (precision), and always returned as a `float`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But every time our program runs, that precision could change. Also, we'd rather not have to change every function we have, since at some point in the future we may want to return `Decimal` objects, and not `floats` - so we want to minimize how much code we would have to change to accomodate all this.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, we might a variable in our code that defines the precision, and could be changed any time we run our code:
    """)
    return


@app.cell
def _():
    PRECISION = 2
    return (PRECISION,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Suppose we have the following functions already defined:
    """)
    return


@app.cell
def _():
    from decimal import Decimal

    def perc_diff(x, y):
        try:
            return (y-x) / x * 100
        except ZeroDivisionError:
            return 0
    
    def sum_squares(*args):
        return sum(x**2 for x in args)

    def avg(*args):
        if len(args) == 0:
            return 0
    
        numbers = [Decimal(x) for x in args]
        sum_ = sum(numbers)
        return sum_ / len(numbers)

    return (Decimal,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a decorator named `normalize` that can be used to decorate these functions to ensure that the result is always returned as a `float` with a precision defined by some global variable `PRECISION`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start with the "standard" decorator skeleton.
    """)
    return


@app.function
def normalize(fn):
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next, we want to intercept the `result`, convert it to a float, and round it to `PRECISION`.
    """)
    return


@app.cell
def _(PRECISION):
    def normalize_1(fn):

        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            result = round(float(result), PRECISION)
            return result
        return inner

    return (normalize_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can apply this decorator our functions:
    """)
    return


@app.cell
def _(Decimal, normalize_1):
    PRECISION_1 = 2

    @normalize_1
    def perc_diff_1(x, y):
        try:
            return (y - x) / x * 100
        except ZeroDivisionError:
            return 0

    @normalize_1
    def sum_squares_1(*args):
        return sum((x ** 2 for x in args))

    @normalize_1
    def avg_1(*args):
        if len(args) == 0:
            return 0
        numbers = [Decimal(x) for x in args]
        sum_ = sum(numbers)
        return sum_ / len(numbers)

    return avg_1, perc_diff_1, sum_squares_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And let's try them out:
    """)
    return


@app.cell
def _(perc_diff_1):
    perc_diff_1(13, 16)
    return


@app.cell
def _(sum_squares_1):
    sum_squares_1(0.1, 0.2, 0.3)
    return


@app.cell
def _(avg_1):
    avg_1(1.1, 3.14, 42)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The nice thing about that approach, is that we can easily change the precision before running our code without changing any of our code except the value of `PRECISION`:
    """)
    return


@app.cell
def _(Decimal, normalize_1):
    PRECISION_2 = 6

    @normalize_1
    def perc_diff_2(x, y):
        try:
            return (y - x) / x * 100
        except ZeroDivisionError:
            return 0

    @normalize_1
    def sum_squares_2(*args):
        return sum((x ** 2 for x in args))

    @normalize_1
    def avg_2(*args):
        if len(args) == 0:
            return 0
        numbers = [Decimal(x) for x in args]
        sum_ = sum(numbers)
        return sum_ / len(numbers)
    print(perc_diff_2(13, 16))
    print(sum_squares_2(0.1, 0.2, 0.3))
    print(avg_2(1.1, 3.14, 42))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 3
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sometimes we have functions that get called often with the same argument values but take a long time to run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If those functions are deterministic (i.e. passing the same arguments will always result in the same return value), then we can get a huge performance benefit by implementing a caching mechanism.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This function simulates a long running function:
    """)
    return


@app.cell
def _():
    from time import sleep

    def _add(x, y):
        sleep(2)
        return x + y

    return (sleep,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see the function is deterministic - the result will always be the same for the same arguments.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use Python's LRU caching decorator to help improve performance when this function is called multiple times with the same arguments.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then use `timeit` to test how performance is affected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll use the `lru_cache` decorator that is in the `functools` module:
    """)
    return


@app.cell
def _():
    from functools import lru_cache

    return (lru_cache,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see how our function runs before we use the cache:
    """)
    return


@app.cell
def _(lru_cache, sleep):
    from timeit import timeit
    def add_no_cache(x, y):
        sleep(2)
        return x + y
    result_no_cache = timeit(lambda: add_no_cache(2, 2), number=3)
    return (add_no_cache, result_no_cache, timeit)

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As expected, this took 20 seconds to run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's decorate that `add` function:
    """)
    return


@app.cell
def _(lru_cache, sleep):
    @lru_cache
    def _add(x, y):
        sleep(2)
        return x + y

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And let's run the timings again:
    """)
    return


@app.cell
def _(add_no_cache, lru_cache, timeit):
    add_cached = lru_cache(maxsize=None)(add_no_cache)
    result_cached = timeit(lambda: add_cached(2, 2), number=3)
    return (result_cached,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 4
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is kind of a "bonus" exercise. It's a follow-up to Question 2.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It's also complicated, so don't worry if you are unable to do this one!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In Question 2, we created a decorator that used a global variable for the precision.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here, we would rather define a decorator that can take that precision as an argument, i.e. we could do something like this:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```
    @normalize(2)
    def perc_diff(x, y):
        try:
            return (y-x) / x * 100
        except ZeroDivisionError:
            return 0

    @normalize(4)
    def sum_squares(*args):
        return sum(x**2 for x in args)

    @normalize(8)
    def avg(*args):
        if len(args) == 0:
            return 0

        numbers = [Decimal(x) for x in args]
        sum_ = sum(numbers)
        return sum_ / len(numbers)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As a hint, remember how we created "partial" functions in a previous exercise?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What we'll want to do here is not write a decorator function directly, but instead write a function that will **create** a decorator function, with the precision captured in the decorator function (which will itself then, be a closure).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Something like this:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```
    def normalize(precision):
        def decorator(fn):
            def inner(*args, **kwargs):
                # precision passed to normalize is available here
                return result
            return inner
        return decorator
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Looking at that skeleton above, you'll notice that when `normalize(precision` is called, it actually returns... a decorator. The difference here is that that decorator also has access to `precision` - i.e. a closure.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's implement this:
    """)
    return


@app.function
def normalize_2(precision):

    def decorator(fn):

        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            return round(float(result), precision)
        return inner
    return decorator


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's call `normalize` and see what we get - remember that the return value is a function that is a decorator.
    """)
    return


@app.cell
def _():
    dec_normalize_2 = normalize_2(2)
    dec_normalize_10 = normalize_2(10)
    return dec_normalize_10, dec_normalize_2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can inspect these closures to see what the free variables are in each:
    """)
    return


@app.cell
def _(dec_normalize_2):
    dec_normalize_2.__closure__
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That integer is actually the integer `2`:
    """)
    return


@app.cell
def _():
    hex(id(2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And the same with `dec_normalize_10`:
    """)
    return


@app.cell
def _(dec_normalize_10):
    dec_normalize_10.__closure__
    return


@app.cell
def _():
    hex(id(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And now we can decorate our functions using this decorator "factory":
    """)
    return


@app.cell
def _(Decimal):
    @normalize_2(2)
    def perc_diff_3(x, y):
        try:
            return (y - x) / x * 100
        except ZeroDivisionError:
            return 0

    @normalize_2(4)
    def sum_squares_3(*args):
        return sum((x ** 2 for x in args))

    @normalize_2(8)
    def avg_3(*args):
        if len(args) == 0:
            return 0
        numbers = [Decimal(x) for x in args]
        sum_ = sum(numbers)
        return sum_ / len(numbers)

    return avg_3, perc_diff_3, sum_squares_3


@app.cell
def _(perc_diff_3):
    perc_diff_3(13, 42)
    return


@app.cell
def _(sum_squares_3):
    sum_squares_3(0.01, 0.02, 0.03)
    return


@app.cell
def _(avg_3):
    avg_3(1.1, 2.2, 3.14)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And this is how "parametrized" decorators can be created in general - we are basically creating and returning generators from a "factory" function.
    """)
    return


if __name__ == "__main__":
    app.run()
