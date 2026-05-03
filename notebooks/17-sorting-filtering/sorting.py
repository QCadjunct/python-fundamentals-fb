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
    ### Sorting
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have already seen how numbers and strings can be sorted using `sorted()`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When we call `sorted` this way:
    """)
    return


@app.cell
def _():
    sorted([10,8,5,1,3,7])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python uses the default (natural) sort ordering for numbers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We saw that when we sort strings, Python uses the unicode code points of the characters to sort strings.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we saw in the lecture, we always sort **by something**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For numbers, we may sort by their natural sort order.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But we may want to sort by other things too, maybe by the absolute value of the number, or sort a list of objects by one the properties on the object, etc.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To do this, we basically define a **key** function that, for each element of an iterable, calculates some value. The sort can be be made based on that **key** function's return value for each element.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, if we want to sort this list of data by absolute value, we would want to first define a function that returns the absolute value for any given number:
    """)
    return


@app.function
def key_func(x):
    return abs(x)


@app.cell
def _():
    data = [-10, -6, 0, 3, 6]
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we just sort this:
    """)
    return


@app.cell
def _(data):
    sorted(data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    but now let's use that `key_func` we just defined:
    """)
    return


@app.cell
def _(data):
    sorted(data, key=key_func)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see the data was sorted by the absolute value.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One thing you should notice here, is that both `-6` and `6` have the same key value (`6`) - so which one comes first in the sorted elements? That will depend on the relative positioning of those original elements in the iterable, and since `-6` occurred before `6` in the original `data`, we end up with the relative positioning in the sorted list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Not all sorts behave this way - those that do, and Python's `sorted` sort algorithm does, are called **stable sorts**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Just to make it even clearer:
    """)
    return


@app.cell
def _():
    data_1 = [2, -2, 1, -1]
    return (data_1,)


@app.cell
def _(data_1):
    sorted(data_1, key=key_func)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Often we can just use a lambda to define the key function. For the example above we could also write:
    """)
    return


@app.cell
def _():
    data_2 = [6, -5, 4, -3, 2, -1]
    sorted(data_2, key=lambda x: abs(x))
    return (data_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In fact, `abs` **is** a function, so we can also just use it directly as our key function in this case:
    """)
    return


@app.cell
def _(data_2):
    sorted(data_2, key=abs)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see a few more examples of sorting using sorting keys.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's say we have a collection of dictionaries that contain some stock information:
    """)
    return


@app.cell
def _():
    data_3 = [{'date': '2020-04-09', 'symbol': 'AAPL', 'open': 268.7, 'high': 270.04, 'low': 264.7, 'close': 267.99}, {'date': '2020-04-09', 'symbol': 'MSFT', 'open': 166.36, 'high': 167.37, 'low': 163.33, 'close': 165.14}, {'date': '2020-04-09', 'symbol': 'AMZN', 'open': 2044.3, 'high': 2053.0, 'low': 2017.66, 'close': 2042.76}, {'date': '2020-04-09', 'symbol': 'FB', 'open': 175.9, 'high': 177.08, 'low': 171.57, 'close': 175.19}]
    return (data_3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Maybe we want to sort this data list by the symbol:
    """)
    return


@app.cell
def _(data_3):
    sorted(data_3, key=lambda item: item['symbol'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But we may also want to sort this data by closing price, from highest to lowest:
    """)
    return


@app.cell
def _(data_3):
    sorted(data_3, key=lambda item: item['close'], reverse=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or maybe we want to sort based on the percentage increase/decrease from opening price:
    """)
    return


@app.cell
def _(data_3):
    sorted(data_3, key=lambda item: (item['close'] - item['open']) / item['open'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's recall how we sorted strings, and noticed that the sort was case sensitive (since the unicode values for `a` and `A` for example, are different.
    """)
    return


@app.cell
def _():
    data_4 = ['Z', 'a', 'A', 'z', 'x', 'X']
    return (data_4,)


@app.cell
def _(data_4):
    sorted(data_4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But suppose we do not want to have a case-sensitive sort - in that case we should casefold each element and use that as a sorting key:
    """)
    return


@app.cell
def _():
    'a'.casefold(), 'A'.casefold()
    return


@app.cell
def _(data_4):
    sorted(data_4, key=lambda s: s.casefold())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    (Note the stable sort, where `a` preceded `A` but `Z` preceded `z` in the original list)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, we can do other things too - we could sort based on the length of the string:
    """)
    return


@app.cell
def _():
    data_5 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    return (data_5,)


@app.cell
def _(data_5):
    sorted(data_5, key=lambda s: len(s))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Again note the stable sort, the elements `one` `two`, `six`, and `ten` were all three characters long, so they ended up at the beginning of the sorted result, but their relative oredering to each other was maintained.
    """)
    return


if __name__ == "__main__":
    app.run()
