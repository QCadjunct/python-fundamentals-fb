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
    ### The zip() Function
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see some simple examples first.
    """)
    return


@app.cell
def _():
    l = [1, 2, 3, 4, 5]
    t = (10, 20, 30)
    return l, t


@app.cell
def _(l, t):
    result = zip(l, t)
    return (result,)


@app.cell
def _(result):
    result
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, what gets returned is a `zip` object - which is an **iterator**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This means we can call `next()` on it:
    """)
    return


@app.cell
def _(result):
    next(result)
    return


@app.cell
def _(result):
    next(result)
    return


@app.cell
def _(result):
    next(result)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And now of course, there are no more elements in that iterator (the shortest sequence `t` had 3 elements), so if we call `next()` again we shoudl get a `StopIteration` exception:
    """)
    return


@app.cell
def _(result):
    try:
        next(result)
    except StopIteration:
        print('StopIteration')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, just like any iterator, if we want to re-iterate over that result, we have to **re-create** the iterator:
    """)
    return


@app.cell
def _(l, t):
    for e in zip(l, t):
        print(e)
    return


@app.cell
def _(l, t):
    combo = list(zip(l, t))
    return (combo,)


@app.cell
def _(combo):
    combo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now `combo` is a list, so an iterable, and we can iterate over that multiple times.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But creating a `zip` object has almost zero cost associated with it since the sequence of tuples is not actually created - they are produced one at a time when we iterate through the zip object.
    """)
    return


@app.cell
def _():
    from time import perf_counter

    return (perf_counter,)


@app.cell
def _(perf_counter):
    _start = perf_counter()
    _l1 = range(100000000000)
    _l2 = range(100000000000)
    combo_1 = zip(_l1, _l2)
    _end = perf_counter()
    print(f'elapsed: {_end - _start}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, even though our range objects are huge, they do not create the values ahead of time (they yield them one by one), and zip does the same - so the creation time for all three was extremely fast.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we were to convert this zip to a list on the other hand, things would be very different. First we would have to iterate over the entire sequence of tuples, and then create a list out of that:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I don't want to be sitting here the entire day, so I'm going to cut back on those numbers a bit:
    """)
    return


@app.cell
def _(perf_counter):
    _start = perf_counter()
    _l1 = range(10000000)
    _l2 = range(10000000)
    combo_2 = list(zip(_l1, _l2))
    _end = perf_counter()
    print(f'elapsed: {_end - _start}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, that took one second - and it will get worse as those number increase:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll run across `zip()` frequently in this course, but let's see at least one practical example right now.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `zip()` basically provides us an easy mechanism for iterating through two or more iterables in parallel.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Remember how we could create dictionaries using the `dict()` function and passing an iterable containing tuples of `(key, value)` to it?
    """)
    return


@app.cell
def _():
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    return (d,)


@app.cell
def _(d):
    d
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Suppose we have some service somewhere that provides us data in tuple format:
    """)
    return


@app.cell
def _():
    data = [
        ('item1', 10, 100.0),
        ('item2', 5, 25.0),
        ('item3', 100, 0.25)
    ]
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And suppose that the **schema** of this data is
    """)
    return


@app.cell
def _():
    schema = ('widget', 'num_sold', 'unit_price')
    return (schema,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now our goal is to turn this `data` and `schema` into a dictionary whose keys are the `widget` names, and corresponding values are themselves dictionaries containing keys for `num_sold` and `unit_price`, so something like this:
    """)
    return


@app.cell
def _():
    d_1 = {'item1': {'num_sold': 10, 'unit_price': 100.0}, 'item2': {'num_sold': 10, 'unit_price': 25.0}, 'item3': {'num_sold': 100, 'unit_price': 0.25}}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Suppose furthermore that over time this schema may change, the only constant we have is that the first item in the tuple is guaranteed to be the widget's name.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, 3 months from now, we may be getting this schema instead:
    """)
    return


@app.cell
def _():
    ('widget', 'manufacturer', 'num_sold', 'unit_price', 'discount')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So we can't "hardcode" our schema and do it this way:
    """)
    return


@app.cell
def _(data):
    d_2 = {}
    for item in data:
        d_2[item[0]] = {'num_sold': item[1], 'unit_price': item[2]}
    print(d_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Although this works, if the schema changes we will have to change our code - not a good design.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Instead we are going to leverage the `schema`, and only modify this if it ever changes, and let our code handle the rest automatically, without changes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To do this, we are going to `zip` each row with the schema:
    """)
    return


@app.cell
def _(data, schema):
    for _row in data:
        print(list(zip(schema, _row)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see we now know what each value in the data represents, based on the schema.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since we are guaranteed that the first element of each row is the item name, we're not really interested in zipping that one up:
    """)
    return


@app.cell
def _(data, schema):
    for _row in data:
        _widget_name = _row[0]
        remaining = zip(schema[1:], _row[1:])
        print(_widget_name, list(remaining))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's make the items in that zip into a dictionary:
    """)
    return


@app.cell
def _(data, schema):
    for _row in data:
        _widget_name = _row[0]
        _sub_dict = dict(zip(schema[1:], _row[1:]))
        print(_widget_name, _sub_dict)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So now we are ready to actually populate a dictionary, starting with an empty one, and adding each `widget_name` as a key, with the remaining values transformed into a dictionary (again all based on the `schema` and `data` which may change over time):
    """)
    return


@app.cell
def _(data, schema):
    data_dict = {}
    for _row in data:
        _widget_name = _row[0]
        _sub_dict = dict(zip(schema[1:], _row[1:]))
        data_dict[_widget_name] = _sub_dict
    print(data_dict)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, we can simplify this by not using temporary variables for `widget_name` and `sub_dict`:
    """)
    return


@app.cell
def _(data, schema):
    data_dict_1 = {}
    for _row in data:
        data_dict_1[_row[0]] = dict(zip(schema[1:], _row[1:]))
    print(data_dict_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And you should realize that we can actually use a dictionary comprehension for this!
    """)
    return


@app.cell
def _(data, schema):
    data_dict_2 = {_row[0]: dict(zip(schema[1:], _row[1:])) for _row in data}
    print(data_dict_2)
    return (data_dict_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There is a "pretty-printing" function available in Python that can print this dictionary in a more human-readable format:
    """)
    return


@app.cell
def _():
    from pprint import pprint

    return (pprint,)


@app.cell
def _(data_dict_2, pprint):
    pprint(data_dict_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So the nice thing about our solution is that it is extensible in that if the data (and the corresponding schema) changes, we can still handle it with no code changes except for updating the schema:
    """)
    return


@app.cell
def _():
    data_1 = [('item1', 'manuf-1', 10, 100.0, 0.2), ('item2', 'manuf-2', 5, 25.0, 0), ('item3', 'manuf-3', 100, 0.25, 0.025)]
    return (data_1,)


@app.cell
def _():
    schema_1 = ('widget', 'manufacturer', 'num_sold', 'unit_price', 'discount')
    return (schema_1,)


@app.cell
def _(data_1, schema_1):
    data_dict_3 = {_row[0]: dict(zip(schema_1[1:], _row[1:])) for _row in data_1}
    return (data_dict_3,)


@app.cell
def _(data_dict_3, pprint):
    pprint(data_dict_3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see our code was able to handle the new schema with no code changes.
    """)
    return


if __name__ == "__main__":
    app.run()
