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
    ### LRU Cache
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We saw in the lecture what an LRU cache is.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Although Python provides us a decorator to apply an LRU caching mechanism to a function (called **memoization**), we are going to try doing it ourselves first as another excellent example of decorators.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We are not going to worry about cache size - for simplicity we'll allow our cache to always grow unbounded.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Another simplification we are going to make is that we are not going to handle caching functions that use keyword-only arguments.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python's LRU cache mechanism does not have these two simplifications.
    """)
    return


@app.function
def cache(func):

    def inner(*args):
        _result = func(*args)
        return _result
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is our standard pattern for creating a decorator (albeit only considering positional arguments).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We want to create a cache where we can store/recall the result of calling `func(*args)`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First thing we'll want to do is create a dictionary - but we don't want to create the dictionary inside `inner`, because that means every time we call `inner` (the decorated function), we would start with an empty cache dictionary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Instead, we're going to define the cache in the outer `cache` function, and access it as a free variable in `inner`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So `cache` gets created every time `cache` is called, but the returned `inner` function can use that same `cache` over and over again.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So next, we need to calculate a key to represent all the arguments that were passed to `inner` (that eventually calls `func`) - and that's simply the tuple `args`.

    Now, it does mean that the tuple `args` must be hashable - just like Python's own implementation of LRU cache.
    """)
    return


@app.function
def cache_1(func):
    print('initialize cache')
    cache = {}

    def inner(*args):
        key = args
        if key in cache:
            print('Cache hit')
            return cache[args]
        else:
            _result = func(*args)
            cache[args] = _result
            return _result
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And now we can start using it:
    """)
    return


@app.function
@cache_1
def my_func(a, b):
    print(f'evaluating my_func({a}, {b})...')
    return a + b


@app.cell
def _():
    my_func(1, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, the original `my_func` was called.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But if we use the same parameters a second time:
    """)
    return


@app.cell
def _():
    my_func(1, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, we get the result back without the function actually executing - the result was obtained from cache.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can decorate another function with the same decorator, and it will have it's own cache:
    """)
    return


@app.function
@cache_1
def add(a, b):
    return a + b


@app.cell
def _():
    add(1, 2)
    return


@app.cell
def _():
    add(1, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That's the basic idea behind the `lru_cache` decorator.

    Let's use that one instead:
    """)
    return


@app.cell
def _():
    from functools import lru_cache

    return (lru_cache,)


@app.cell
def _(lru_cache):
    @lru_cache(maxsize=2)
    def add_1(a, b):
        print(f'Calling add({a}, {b})...')
        return a + b

    return (add_1,)


@app.cell
def _(add_1):
    add_1(1, 1)
    return


@app.cell
def _(add_1):
    add_1(1, 1)
    return


@app.cell
def _(add_1):
    add_1(2, 2)
    return


@app.cell
def _(add_1):
    add_1(1, 1)
    return


@app.cell
def _(add_1):
    add_1(2, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But we made the cache size `2`, which means if we now call with a new set of args:
    """)
    return


@app.cell
def _(add_1):
    add_1(3, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Not only was the function evaluated (these args were not in the cache), but it also cleared out the oldest entry in the cache - (1, 1). (2, 2) is still there though.
    """)
    return


@app.cell
def _(add_1):
    add_1(2, 2)
    return


@app.cell
def _(add_1):
    add_1(1, 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When you have a function that takes a long time to run, and you often call it with the same arguments, don't forget an LRU cache - it can greatly speed up your code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's take a look at a very simple example to calculate the Fibonacci numbers:

    ```
    0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This sequence starts with `0` and `1`, and every element thereafter is the sum of the previous two - so there is a recursive relationship, and we could define a mamethematical function to produce the `n`th number (assuming we are indexing starting at `0`), this way:

    ```
    Fib(0) = 0
    Fib(1) = 1
    Fib(n) = Fib(n-1) + Fib(n-2), n > 1
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can express this same recursive definition using a Python function:
    """)
    return


@app.function
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This function may seem odd as it is calling itself - this is known as a recursive function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The way it works is that if we call `fib(0)` or `fib(1)` it just returns `0` and `1` respectively.

    If we call `fib(2)` it will call `fib(0)` and `fib(1)` which return  `0` and `1`.

    If we call `fib(3)` it will call `fib(1)` and `fib(2)` - `fib(1)` will just return `1`, but `fib(2)` calls `fib(0)` and `fib(1)`.

    If we call `fib(4)` it will call `fib(2)` and `fib(3)`, and the processing path for those two calls will follow what we just saw.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So recursion is a very simple approach to implement certain algorithms (like Fibonacci, factorials, etc).

    But they can often become computationally intensive.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's put a print statement to indicate when the `fib` function gets called, and see what happens:
    """)
    return


@app.function
def fib_1(n):
    print(f'fib({n}) called...')
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


@app.cell
def _():
    fib_1(0)
    return


@app.cell
def _():
    fib_1(1)
    return


@app.cell
def _():
    fib_1(2)
    return


@app.cell
def _():
    fib_1(3)
    return


@app.cell
def _():
    fib_1(4)
    return


@app.cell
def _():
    fib_1(5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And the higher we go the more function calls are made - in fact the number of calls grows so fast that the timing to calulate the `n`th Fibonacci number even for relatively small `n` is prohibitive:
    """)
    return


@app.cell
def _():
    from time import perf_counter

    return (perf_counter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's remove that `print` statement first:
    """)
    return


@app.function
def fib_2(n):
    if n <= 1:
        return n
    return fib_1(n - 1) + fib_1(n - 2)


@app.cell
def _(perf_counter):
    for n1 in range(30, 38):
        _start = perf_counter()
        _result = fib_2(n1)
        _end = perf_counter()
        print(f'fib({n1})={_result}, elapsed: {_end - _start}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The problem of course is that when we call `fib(37)` it calls `fib(35)` and `fib(36)`.
    In turn `fib(35)` calls `fib(34) and fib(33)` and `fib(36)` calls `fib(34)` and `fib(35)`, etc - so we end up calling the same `fib(n)` over and over again.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What if we could cache the results of calling `fib(n)` - then we could use the cache for a previous Fibonacci number without recalculating it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And that's precisely what the LRU cache can do for us:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's put that `print` statement back and see the call stack when we call `fib(6)`:
    """)
    return


@app.function
def fib_4(n):
    print(f'fib({n}) called...')
    if n <= 1:
        return n
    return fib_2(n - 1) + fib_2(n - 2)


@app.cell
def _():
    fib_4(6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's apply that LRU cache:
    """)
    return


@app.cell
def _(lru_cache):
    @lru_cache
    def fib_5(n):
        print(f'fib({n}) called...')
        if n <= 1:
            return n
        return fib_4(n - 1) + fib_4(n - 2)

    return (fib_5,)


@app.cell
def _(fib_5):
    fib_5(6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see the number of function calls greatly decreased, and we can redo our timings:
    """)
    return


@app.cell
def _(fib_5, lru_cache, perf_counter):
    @lru_cache
    def fib_6(n):
        if n <= 1:
            return n
        return fib_5(n - 1) + fib_5(n - 2)
    for n2 in range(30, 38):
        _start = perf_counter()
        _result = fib_6(n2)
        _end = perf_counter()
        print(f'fib({n2})={_result}, elapsed: {_end - _start}')
    return (fib_6,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Much faster, and even for larger `n`s:
    """)
    return


@app.cell
def _(fib_6, perf_counter):
    for n3 in range(100, 110):
        _start = perf_counter()
        _result = fib_6(n3)
        _end = perf_counter()
        print(f'fib({n3})={_result}, elapsed: {_end - _start}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In fact, we really only need to cache the results of the last three Fibonacci numbers to gain efficiencies:
    """)
    return


@app.cell
def _(fib_6, lru_cache, perf_counter):
    @lru_cache(maxsize=3)
    def fib_7(n):
        if n <= 1:
            return n
        return fib_6(n - 1) + fib_6(n - 2)
    for n4 in range(30, 38):
        _start = perf_counter()
        _result = fib_7(n4)
        _end = perf_counter()
        print(f'fib({n4})={_result}, elapsed: {_end - _start}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The efficiencies are not as great as an unbounded cache, but the efficiency gain is noetheless perfectly acceptable in view of the fact that we are not growing our cache unbounded as we calculate larger and larger Fibonacci numbers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's use `timeit` to see this:
    """)
    return


@app.cell
def _():
    from timeit import timeit

    return (timeit,)


@app.cell
def _(lru_cache):
    @lru_cache(maxsize=3)
    def fib_3(n):
        if n <= 1:
            return n
        return fib_3(n - 1) + fib_3(n - 2)

    return


@app.cell
def _(lru_cache):
    @lru_cache()
    def fib_unbounded(n):
        if n <= 1:
            return n
        return fib_unbounded(n - 1) + fib_unbounded(n - 2)

    return


@app.cell
def _(timeit):
    timeit(
        '[fib_3(n) for n in range(100, 200)]', 
        globals=globals(), 
        number=10_000
    )
    return


@app.cell
def _(timeit):
    timeit(
        '[fib_unbounded(n) for n in range(100, 200)]', 
        globals=globals(), 
        number=10_000
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So as is often the case, we need to balance performance against memory usage.
    """)
    return


if __name__ == "__main__":
    app.run()
