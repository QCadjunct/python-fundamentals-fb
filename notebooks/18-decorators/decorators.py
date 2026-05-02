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
    ### Decorators
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start with the pattern we have for creating decorators - it is pretty much the same, so you can re-use this pattern with any customizations you want:
    """)
    return


@app.function
def wrapper(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You'll notice that `inner` will call `func` with `*args` and `**kwargs` and nothing else.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It may not look very interesting, but notice that we can now wrap any function:
    """)
    return


@app.cell
def _():
    def add(a, b, c):
        return a + b + c

    def greet(name):
        return f'Hello {name}!'

    def join(data, *, item_sep=',', line_sep='\n'):
        return line_sep.join(
            [
                item_sep.join(str(item) for item in row) 
                for row in data
            ]
        )

    return add, greet, join


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can call those functions as they are:
    """)
    return


@app.cell
def _(add):
    add(1, 2, 3)
    return


@app.cell
def _(greet):
    greet('Python')
    return


@app.cell
def _(join):
    join([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But we can also create these wrapped functions:
    """)
    return


@app.cell
def _(add, greet, join):
    add_wrapped = wrapper(add)
    greet_wrapped = wrapper(greet)
    join_wrapped = wrapper(join)
    return add_wrapped, greet_wrapped, join_wrapped


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can call these "wrapped" functions just like we called the "non-wrapped" original versions:
    """)
    return


@app.cell
def _(add_wrapped):
    add_wrapped(1, 2, 3)
    return


@app.cell
def _(greet_wrapped):
    greet_wrapped('Python')
    return


@app.cell
def _(join_wrapped):
    join_wrapped([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, as it stands, that `wrapper` function does not do much - but it forms the basis for us to add functionality around our original function however we want.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's say we want a simple log of the call being made:
    """)
    return


@app.function
def log(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} called... result={result}')
        return result
    return inner


@app.cell
def _(add, greet, join):
    add_logged = log(add)
    greet_logged = log(greet)
    join_logged = log(join)
    return add_logged, greet_logged


@app.cell
def _(add_logged):
    add_logged(1, 2, 3)
    return


@app.cell
def _(greet_logged):
    greet_logged('Python')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we now have to remember to call `greet_logged` instead of `greet` everywhere in our code (assuming we want to log things everywhere).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Firstly, I really don't want to write code like `greet_logged`, `add_logged`, etc - I really just want to use `greet`, `add`, etc.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Secondly, I may already have thousands of lines of code that call `greet` `add`, etc - again, I really do not want to look for those calls and change each one to the `_logged` version.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, instead I'm going to name the wrapped version the same as the original version. The wrapped version is a closure that still maintains a link to the original function, but my symbol `add`, `greet`, etc now points to the new function (closure).
    """)
    return


@app.cell
def _():
    def log_1(func):

        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'{func.__name__} called... result={result}')
            return result
        return inner

    def add_1(a, b, c):
        return a + b + c
    add_1 = log_1(add_1)

    def greet_1(name):
        return f'Hello {name}!'
    greet_1 = log_1(greet_1)

    def join_1(data, *, item_sep=',', line_sep='\n'):
        return line_sep.join([item_sep.join((str(item) for item in row)) for row in data])
    join_1 = log_1(join_1)
    return (greet_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And now I can use the same symbol to call the logged version:
    """)
    return


@app.cell
def _(greet_1):
    greet_1('Python')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This pattern of defining the function `add` and then redefining the symbol using some decorator: `add = log(add)` is so common that there is a shorthand syntax for it:
    """)
    return


@app.cell
def _():
    def log_2(func):

        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'{func.__name__} called... result={result}')
            return result
        return inner

    @log_2
    def add_2(a, b, c):
        return a + b + c

    @log_2
    def greet_2(name):
        return f'Hello {name}!'

    @log_2
    def join_2(data, *, item_sep=',', line_sep='\n'):
        return line_sep.join([item_sep.join((str(item) for item in row)) for row in data])

    return (add_2,)


@app.cell
def _(add_2):
    add_2(1, 2, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now every time we call one of those decorated functions in our code, a log will be emitted.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And this means we now have a central, unique location where we can change what our log decorator does - and every function that is decorated with the `log` decorator will use that definition - no re-typing code in multiple places.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In fact, let's now write proper logs,using Python's logging system (we'll just log to the console, but it can be set up to log to file, and a variety of other places).
    """)
    return


@app.cell
def _():
    import logging

    return (logging,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll configure our logger (we only need to do this once per application):
    """)
    return


@app.cell
def _(logging):
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
    return


@app.cell
def _(logging):
    logger = logging.getLogger('Custom Log')
    return (logger,)


@app.cell
def _(logger):
    logger.debug('Information message')
    return


@app.cell
def _(logger):
    logger.error('Some error happened')
    return


@app.cell
def _(logger):
    logger.warning('Some warning')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    let's use that to write a better logging decorator, that will include the run time of the function as well:
    """)
    return


@app.cell
def _(logger):
    from time import perf_counter

    def log_3(func):

        def inner(*args, **kwargs):
            start = perf_counter()
            result = func(*args, **kwargs)
            end = perf_counter()
            logger.debug(f'called={func.__name__}, elapsed={end - start}')
            return result
        return inner

    return (log_3,)


@app.cell
def _(log_3):
    @log_3
    def add_3(a, b, c):
        return a + b + c

    @log_3
    def greet_3(name):
        return f'Hello {name}!'

    @log_3
    def join_3(data, *, item_sep=',', line_sep='\n'):
        return line_sep.join([item_sep.join((str(item) for item in row)) for row in data])

    return add_3, join_3


@app.cell
def _(add_3):
    add_3(10, 20, 30)
    return


@app.cell
def _(join_3):
    join_3([range(10) for _ in range(10)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll see other applications of decorators in the next set of videos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The main takeaway is that decorators are very handy for adding pre and post function call code that is reusable across multiple functions - in a way that is completely **transparent** to the user.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, you may inherit some piece of code that defines several functions, and calls them hundreds of times - you can now log each of these functions by simply decorating the function definition - all other calls will transparently use the decorated function witout further modifications.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    More often than not, you will probably end up using decorators that someone *else* has written in some library - but it is important to understand how they work if you want to use those effectively (and more importantly, understand what's going on!).
    """)
    return


if __name__ == "__main__":
    app.run()
