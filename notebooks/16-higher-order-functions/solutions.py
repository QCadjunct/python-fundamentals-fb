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
    We want to write a function that can find an approximate maximum or minimum of some given function over some given range.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, given some function:

    ```
    f(x) = x**2 - 1
    ```

    our function should return an approximate minimum (or maximum) of `f` over some given range, say `[-5, 5]`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll do this by essentially splitting our intervals into `n` points (what I'll call the `resolution`), evaluating the function at each of these points, and returning either the min or the max.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We want this function to be generic, so it should have the following parameters:
    - a function of one variable
    - a range of values defined by start/end values
    - a value indicating the "resolution"
    - a value indicating whether we want the min or the max
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
    Let's start by writing a few single-variable functions:
    """)
    return


@app.cell
def _():
    import math

    f1 = lambda x: x ** 2 - 1
    f2 = lambda x: abs(x-2)
    f3 = lambda x: math.sin(x)
    return f1, f2, f3, math


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's figure out what parameters we want to define for our function that will determine an approximate min or max:

    - `f`: the function used to evaluate approx min/max
    - `start`: the left end of the interval - default to `-10`
    - `end`: the right end of the interval - default to `10`
    - `resolution`: indicates how many times we'll evaluate the function `func` over the interval `[start, end)` - default to `1_000`
    - `is_min`: if `True` returns the minimum, otherwise returns the maximum - default to `True`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's define the function first, and we'll come back to it's implementation later:
    """)
    return


@app.function
def find_extreme(f, start=-10, end=10, resolution=1_000, is_min=True):
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our first task will be to calculate the list of values we want to evaluate the function at:
    """)
    return


@app.function
def find_extreme_1(f, start=-10, end=10, resolution=1000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = [start + i * delta for i in range(resolution)]
    return data


@app.cell
def _():
    find_extreme_1(None, start=1, end=6, resolution=8)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ok, so this is starting to look good. Next we need to evaluate the function at each of those points:
    """)
    return


@app.function
def find_extreme_2(f, start=-10, end=10, resolution=1000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = [start + i * delta for i in range(resolution)]
    f_values = [f(x) for x in data]
    return f_values


@app.cell
def _(f1):
    find_extreme_2(f1, -2, 2, 10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next we'll need to find the minimum of these values:
    """)
    return


@app.function
def find_extreme_3(f, start=-10, end=10, resolution=1000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = [start + i * delta for i in range(resolution)]
    f_values = [f(x) for x in data]
    _result = min(f_values)
    return _result


@app.cell
def _(f1):
    find_extreme_3(f1, -2, 2, 10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, the higher our resolution, the better our approximation should be:
    """)
    return


@app.cell
def _(f1):
    find_extreme_3(f1, -2, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's handle the `is_min` argument:
    """)
    return


@app.function
def find_extreme_4(f, start=-10, end=10, resolution=1000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = [start + i * delta for i in range(resolution)]
    f_values = [f(x) for x in data]
    if is_min:
        _result = min(f_values)
    else:
        _result = max(f_values)
    return _result


@app.cell
def _(f1):
    (find_extreme_4(f1, -2, 2), find_extreme_4(f1, -2, 2, is_min=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can try out our other functions too:
    """)
    return


@app.cell
def _(f2):
    (find_extreme_4(f2, -10, 10), find_extreme_4(f2, -10, 10, is_min=False))
    return


@app.cell
def _(f3):
    (find_extreme_4(f3, -10, 10), find_extreme_4(f3, -10, 10, is_min=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's loook at our function and see if we can simplify our code:
    """)
    return


@app.function
def find_extreme_5(f, start=-10, end=10, resolution=1000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = [start + i * delta for i in range(resolution)]
    f_values = [f(x) for x in data]
    if is_min:
        _result = min(f_values)
    else:
        _result = max(f_values)
    return _result


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The first thing to note is that we are creating these lists (`data` and `f_values`) - that seems uncessary - we could use generator expressions instead since we will only need to iterate through them once:
    """)
    return


@app.function
def find_extreme_6(f, start=-10, end=10, resolution=1000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = (start + i * delta for i in range(resolution))
    f_values = (f(x) for x in data)
    if is_min:
        _result = min(f_values)
    else:
        _result = max(f_values)
    return _result


@app.cell
def _(f3):
    find_extreme_6(f3, -10, 10, is_min=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Another thing too, is that we using a comprehension to apply the function `func` to every value in `data` - this is fine, but we could also just use the `map` function:
    """)
    return


@app.function
def find_extreme_7(f, start=-10, end=10, resolution=1000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = (start + i * delta for i in range(resolution))
    f_values = map(f, data)
    if is_min:
        _result = min(f_values)
    else:
        _result = max(f_values)
    return _result


@app.cell
def _(f3):
    find_extreme_7(f3, -10, 10, is_min=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Additionally, we could use a ternary operator to pick whether we should use `min` or `max`:
    """)
    return


@app.function
def find_extreme_8(f, start=-10, end=10, resolution=1000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = (start + i * delta for i in range(resolution))
    f_values = map(f, data)
    min_max = min if is_min else max
    _result = min_max(f_values)
    return _result


@app.cell
def _(f3):
    (find_extreme_8(f3, -10, 10), find_extreme_8(f3, -10, 10, is_min=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can then clean up the code this way:
    """)
    return


@app.function
def find_extreme_9(f, start=-10, end=10, resolution=1000, is_min=True):
    delta = (end - start) / (resolution - 1)
    data = (start + i * delta for i in range(resolution))
    min_max = min if is_min else max
    return min_max(map(f, data))


@app.cell
def _(f3):
    (find_extreme_9(f3, -10, 10), find_extreme_9(f3, -10, 10, is_min=False))
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
    You are given a function of two variables, and a list of tuples containing the values for the two variables.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create a list that is the result of calling the function on each values in the list, using three different techniques:
    - a `for` loop
    - a list comprehension
    - the `map` function

    Use the `timeit` function to time each approach.

    Hint: write a function that implements each approach, and then time calling those functions using the `timeit` function (`from timeit import timeit` - we've used it before). Also you will want to specify `number=10` or something like that when you run `timeit` - unless you want to sit there watvhing your screen for quite a while :-)
    """)
    return


@app.cell
def _(math):
    def func(point):
        x, y = point
        return math.hypot(x, y)
    points = [(0, 0), (1, 1), (10, 20), (math.pi, math.e)]  # expect point to be a sequence of two values  # hypot is a function that calculates sqrt(x**2 + y**2), given a sequence (x, y)
    return func, points


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your result for `points` should be:

    ```
    [0.0, 1.4142135623730951, 22.360679774997898, 4.154354402313314]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For timing purposes, use a larger set of points, like this one:
    """)
    return


@app.cell
def _(math):
    points_large = [(math.sin(x), math.cos(x)) for x in range(1, 1_000_000)]
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
    A `for` loop approach could be something like:
    """)
    return


@app.cell
def _(func, points):
    _results = []
    for point in points:
        _results.append(func(point))
    _results
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But whenever we see code that creates an empty list and a loop that just appends to that list with relatively simple code in the loop body, we should consider a comprehension instead.
    """)
    return


@app.cell
def _(func, points):
    _results = [func(point) for point in points]
    _results
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But we can also just use the `map` function:
    """)
    return


@app.cell
def _(func, points):
    _results = list(map(func, points))
    _results
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: the `map` function returns a generator, so we pass that to `list()` to actually generate a list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's write some functions to encapsulate each technique so we can easily use them for timing things:
    """)
    return


@app.function
def calc_loop(f, pts):
    _results = []
    for pt in pts:
        _results.append(f(pt))
    return _results


@app.function
def calc_comp(f, pts):
    return [f(pt) for pt in pts]


@app.function
def calc_map(f, pts):
    return list(map(f, pts))


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's make sure the functions work as expected:
    """)
    return


@app.cell
def _(func, points):
    calc_loop(func, points)
    return


@app.cell
def _(func, points):
    calc_comp(func, points)
    return


@app.cell
def _(func, points):
    calc_map(func, points)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's run some timings, using `points_large` for our arguments:
    """)
    return


@app.cell
def _():
    from timeit import timeit

    return (timeit,)


@app.cell
def _(timeit):
    timeit('calc_loop(func, points_large)', globals=globals(), number=10)
    return


@app.cell
def _(timeit):
    timeit('calc_comp(func, points_large)', globals=globals(), number=10)
    return


@app.cell
def _(timeit):
    timeit('calc_map(func, points_large)', globals=globals(), number=10)
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
    Write a function that returns a function with all arguments, except the first one, prefilled with certain values provided to the outer function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    (This is sometimes called a partial function).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, we may have some functions such as:
    """)
    return


@app.function
def power(x, n):
    return x ** n


@app.cell
def _(math):
    def dist(pt1, pt2):
        return math.sqrt(sum(coord_1 - coord_2 for coord_1, coord_2 in zip(pt1, pt2)))

    return (dist,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or even functions already defined, such as:

    ```
    math.gcd(a, b)
    ```
    or
    ```
    math.log(x, base)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We want to to be able to generate new functions, based on these ones (`power`, `dist`, `gcd`, `log`) but with all the values except the first one prefilled, for example, assuming our function is named `partial`, we can use it to define new functions this way:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```
    squares = partial(power, 2)
    dist_from_origin = partial(dist, (0, 0))
    gcd_13 = partial(math.gcd, 13)
    log_2 = partial(math.log, 2)
    log_10 = partial(math.log, 10)
    log_16 = partial(math.log, 16)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then when we call our new functions, we just pass in the value for the first argument, i.e.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```
    squares(3) --> 9
    squares(4) --> 16
    dist_from_origin((1, 1)) --> 1.414
    log_2(10) --> 3.3219
    log_10(10) --> 1.0
    log_16(10) --> 0.8304
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
    For this we'll use a function that defines and returns a nested function, and captures the function whatever arguments need to be passed to it (aside from the first argument).
    """)
    return


@app.function
def partial(f, *args, **kwargs):
    def inner(first_arg):
        print('func', f.__name__)
        print('first_arg', first_arg)
        print('args', args)
        print('kwargs', kwargs)
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see how this behaves:
    """)
    return


@app.cell
def _():
    f = partial(power, 2)
    return (f,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This function is a closure, and knows about both `power` and `2`. We can see it this way:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can call this closure:
    """)
    return


@app.cell
def _(f):
    f(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, the closure captured the `power` function and the value `2` (in `args`) - and of course `kwargs` is empty. If we had a function that requires keyword only arguments, we could pass those in too:
    """)
    return


@app.cell
def _():
    f_1 = partial(lambda x, y, *, k1: (x, y, k1), 10, k1=100)
    return (f_1,)


@app.cell
def _(f_1):
    f_1(1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we have the basic skeleton for our solution. What we now need to do is actually call the function, inserting `first_arg`, and return the result of that.
    """)
    return


@app.function
def partial_1(f, *args, **kwargs):

    def inner(first_arg):
        _result = f(first_arg, *args, **kwargs)
        return _result
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We don't actually need to store the `result` and then return it, we can just return it directly:
    """)
    return


@app.function
def partial_2(f, *args, **kwargs):

    def inner(first_arg):
        return f(first_arg, *args, **kwargs)
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can use this to generate some new functions with pre-filled arguments:
    """)
    return


@app.cell
def _(dist, math):
    squares = partial_2(power, 2)
    dist_from_origin = partial_2(dist, (0, 0))
    gcd_13 = partial_2(math.gcd, 13)
    log_2 = partial_2(math.log, 2)
    log_10 = partial_2(math.log, 10)
    log_16 = partial_2(math.log, 16)
    return dist_from_origin, gcd_13, log_10, log_16, log_2, squares


@app.cell
def _(squares):
    squares(4)
    return


@app.cell
def _(dist_from_origin):
    dist_from_origin((1, 1))
    return


@app.cell
def _(gcd_13):
    gcd_13(169)
    return


@app.cell
def _(log_2):
    log_2(10)
    return


@app.cell
def _(log_10):
    log_10(10)
    return


@app.cell
def _(log_16):
    log_16(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 4
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that can be used to not only execute another function with specified arguments, but print a "log" (basically just print to the console", of how long it took to execute the function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, given some functions like this:
    """)
    return


@app.cell
def _(math):
    def norm(x, y):
        return math.sqrt(x**2 + y**2)

    def find_index_min(seq):
        min_ = min(seq)
        return seq.index(min_)

    return find_index_min, norm


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then assuming your logging function is called `logged`, you could create logged functions this way:
    """)
    return


@app.function
def logged(f):
    # implement this
    pass


@app.cell
def _(find_index_min, norm):
    norm_logged = logged(norm)
    find_index_min_logged = logged(find_index_min)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You would then be able to call `norm_logged` with some arguments, or `find_index_min_logged` with some arguments, and not only get the actual result back, but also see an output to the console that tells you how long the function took to run.
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
    To solve this, we'll use a closure with nested functions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The outer function will take a single argument, the function `f`.
    """)
    return


@app.function
def logged_1(f):
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then we'll create a nested function that will receive whatever arguments `f` needs to be called, and we'll return that new inner function (that will be the closure):
    """)
    return


@app.function
def logged_2(f):

    def inner(*args, **kwargs):
        _result = f(*args, **kwargs)
        return _result
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You'll notice that when we call `logged(norm)` we'll actually get a function back - that `inner` function whose `f` value is actually `norm` - let's try it out:
    """)
    return


@app.cell
def _(norm):
    logged_norm = logged_2(norm)
    return (logged_norm,)


@app.cell
def _(logged_norm):
    logged_norm
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As expected `logged_norm` is a function - but it is a special function - it knows that `f` (in it's body) is actually `norm`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can actually see it this way:
    """)
    return


@app.cell
def _(logged_norm):
    logged_norm.__closure__
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice how there is this "cell", which is a function object at some memory address - that memory address is actually the memory address of `norm`:
    """)
    return


@app.cell
def _(norm):
    hex(id(norm))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could also create a logged function for `find_index_min`:
    """)
    return


@app.cell
def _(find_index_min):
    find_index_min_logged_1 = logged_2(find_index_min)
    return (find_index_min_logged_1,)


@app.cell
def _(find_index_min_logged_1):
    find_index_min_logged_1.__closure__
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And the function in that closure is actually the `find_index_min` function:
    """)
    return


@app.cell
def _(find_index_min):
    hex(id(find_index_min))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's finish off our `logged` function - we still need to time things and print that out:
    """)
    return


@app.cell
def _():
    from time import perf_counter

    def logged_3(f):

        def inner(*args, **kwargs):
            start = perf_counter()
            _result = f(*args, **kwargs)
            end = perf_counter()
            print(f'elapsed: {end - start} secs')
            return _result
        return inner

    return (logged_3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And let's try it out:
    """)
    return


@app.cell
def _(find_index_min, logged_3, norm):
    logged_norm_1 = logged_3(norm)
    find_index_min_logged_2 = logged_3(find_index_min)
    return find_index_min_logged_2, logged_norm_1


@app.cell
def _(logged_norm_1):
    _result = logged_norm_1(1, 1)
    print(f'result: {_result}')
    return


@app.cell
def _(find_index_min_logged_2):
    _result = find_index_min_logged_2([10, 5, 3, -2, -10, 100])
    print(f'result: {_result}')
    return


if __name__ == "__main__":
    app.run()
