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
    ### Filtering
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we think about filtering an iterable, we want to keep or discard values in the iterable based on whether some condition holds True or not.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we could approach filtering this way.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Suppose we want to filter the following list based on whether the value is even (discarding odd numbers).
    """)
    return


@app.cell
def _():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We might write a function that takes any number and returns `True` if the number is even, and `False` if it is odd.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Functions that return `True` or `False` based on one or more arguments, are called **predicate** functions.
    """)
    return


@app.function
def is_even(n):
    return n % 2 == 0


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can now use this predicate function to generate a new list containing only those elements where the predicate function is `True`:
    """)
    return


@app.cell
def _(data):
    evens = [n for n in data if is_even(n)]

    print(evens)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So this was quite straightforward, and works very well - for smaller iterables!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice that we have to create a new list, and perform all calculations and store in memory the entire result set, even if we end up not needing all the data in there. (We may only be interested in knowing if there are any even values in the data).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Instead we may want to use a generator object to achieve the same thing, but resulting in a lazy iterator:
    """)
    return


@app.cell
def _(data):
    evens_1 = (n for n in data if is_even(n))
    return (evens_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can now iterate through evens, but of course only once!
    """)
    return


@app.cell
def _(evens_1):
    list(evens_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python's `filter` function can also be used to filter data, and the syntax is slightly simpler than a comprehension.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We need an **iterable**, and a **predicate** function, and Python will do the rest:
    """)
    return


@app.cell
def _(data):
    filtered = filter(is_even, data)
    return (filtered,)


@app.cell
def _(filtered):
    filtered
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, the returned value from `filter` is not a list or a tuple, it is in fact a "lazy" iterator.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can iterate through it by putting it into a list:
    """)
    return


@app.cell
def _(filtered):
    list(filtered)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And in fact, we don't even need to use `def` to define our predicate function, since it is a simple function, we can simply use a lambda:
    """)
    return


@app.cell
def _(data):
    filtered_1 = filter(lambda x: x % 2 == 0, data)
    return (filtered_1,)


@app.cell
def _(filtered_1):
    list(filtered_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's look at another example.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Suppose we have a list of tuples representing some daily stock quotes, structured as

    ```
    (symbol, open, high, low, close, volume)
    ```
    """)
    return


@app.cell
def _():
    quotes = [
        ('AACC', 6.05, 6.07, 6.03, 6.05, 65800),
        ('AAME', 1.7, 1.82, 1.7, 1.82, 4300),
        ('AAON', 24.98, 25.07, 24.9, 24.94, 28200),
        ('AAPL', 317.99, 319.57, 316.75, 317.13, 12901800),
        ('AATI', 3.82, 3.82, 3.74, 3.79, 194600),
        ('AAWW', 60.89, 61.44, 60.5, 61.19, 272800),
        ('AAXJ', 65.4, 65.71, 65.28, 65.56, 390300),
        ('ABAT', 4.01, 4.01, 3.95, 3.99, 656300),
        ('ABAX', 25.26, 25.49, 25.04, 25.42, 73700),
        ('ABBC', 11.75, 11.88, 11.48, 11.53, 29700),
        ('ABCB', 9.3, 9.3, 9.06, 9.14, 42600),
        ('ABCD', 3.25, 3.25, 3.11, 3.22, 122800),
        ('ABCO', 48.75, 50.41, 46.9, 50.37, 66300),
        ('ABCW', 0.52, 0.61, 0.52, 0.53, 83000),
        ('ABFS', 25.98, 26.27, 25.41, 25.5, 384900),
        ('ABIO', 3.96, 4, 3.88, 4, 38500),
        ('ABMD', 11.94, 12, 11.69, 11.87, 122600),
        ('ABTL', 0.82, 0.84, 0.82, 0.83, 28700),
        ('ABVA', 3.09, 3.25, 3.09, 3.25, 6200),
        ('ACAD', 0.76, 0.76, 0.7, 0.74, 341500),
        ('ACAS', 7.52, 7.72, 7.52, 7.66, 5199800),
        ('ACAT', 14.44, 14.44, 14.04, 14.2, 51700),
        ('ACCL', 8.11, 8.21, 7.94, 8.1, 456100),
        ('ACET', 8.01, 8.04, 7.13, 7.73, 575600),
        ('ACFC', 1.69, 1.7, 1.5, 1.6, 12300),
        ('ACFN', 3.82, 4, 3.82, 3.98, 53700),
        ('ACGL', 89.76, 90.14, 89.39, 89.92, 240900),
        ('ACGY', 22.41, 22.56, 22.25, 22.46, 86800),
        ('ACHN', 3.12, 3.2, 3.07, 3.16, 113700),
        ('ACIW', 26.96, 27.03, 26.63, 26.8, 157000),
        ('ACLI', 33.65, 33.77, 33.45, 33.63, 28700),
        ('ACLS', 2.47, 2.63, 2.46, 2.53, 1818800),
        ('ACMR', 2.69, 2.84, 2.37, 2.71, 158600),
        ('ACOM', 25.2, 26.6, 24.9, 26.56, 265300),
        ('ACOR', 26.67, 27.07, 26.38, 27.04, 1415000),
        ('ACPW', 1.84, 1.89, 1.77, 1.85, 565500),
        ('ACTG', 27.2, 27.43, 26.86, 27.18, 228800),
        ('ACTI', 3.25, 3.26, 3.25, 3.26, 148500),
        ('ACTS', 2.08, 2.09, 2.07, 2.07, 130500),
        ('ACUR', 2.6, 2.64, 2.51, 2.6, 16000),
        ('ACWI', 46.53, 46.7, 46.32, 46.51, 286200),
        ('ACWX', 44.49, 44.66, 44.36, 44.6, 55500),
        ('ACXM', 18, 18.07, 17.81, 18.01, 289800),
        ('ADAM', 7.34, 7.49, 7.33, 7.44, 81700),
        ('ADAT', 0.6, 0.68, 0.59, 0.66, 86400),
        ('ADBE', 29.43, 29.71, 29.07, 29.14, 7585300),
        ('ADCT', 12.68, 12.69, 12.66, 12.68, 1660500),
        ('ADEP', 6.14, 6.14, 4.95, 5.61, 71000),
        ('ADES', 6.2, 6.22, 6, 6.19, 4800),
        ('ADGF', 4.31, 4.55, 4.31, 4.54, 10200)
    ]
    return (quotes,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our aim is to filter out records which closed higher than their open.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's look at an individual record and see how we are going to define our predicate:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```('ADGF', 4.31, 4.55, 4.31, 4.54, 10200)```
    """)
    return


@app.function
def closed_higher(rec):
    open_ = rec[1]
    close = rec[4]
    return close > open_


@app.cell
def _():
    closed_higher(('ADGF', 4.31, 4.55, 4.31, 4.54, 10200))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But on the other hand:
    """)
    return


@app.cell
def _():
    closed_higher(('ACWI', 46.53, 46.7, 46.32, 46.51, 286200))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can simplify the predicate a bit:
    """)
    return


@app.function
def closed_higher_1(rec):
    return rec[4] > rec[1]


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can filter our data this way:
    """)
    return


@app.cell
def _(quotes):
    filtered_2 = filter(closed_higher_1, quotes)
    return (filtered_2,)


@app.cell
def _(filtered_2):
    list(filtered_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, we don't even need to define our predicate as a separate function, we can inline a lambda expression to do the same thing:
    """)
    return


@app.cell
def _(quotes):
    filtered_3 = filter(lambda rec: rec[4] > rec[1], quotes)
    return (filtered_3,)


@app.cell
def _(filtered_3):
    list(filtered_3)
    return


if __name__ == "__main__":
    app.run()
