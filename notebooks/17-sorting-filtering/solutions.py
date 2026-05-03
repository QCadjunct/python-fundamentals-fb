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
    Given a list of tuples containing two numerical values, write a function that returns a list of the same tuples, sorted by the absolute value of the difference between the two numbers, in descending order.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, if the input is:
    """)
    return


@app.cell
def _():
    l = [
        (1, 2),
        (-4, -5.5),
        (10, -10),
        (-2, 2)
    ]
    return (l,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then the return value of the function should be:

    ```
    [
      (10, -10)
      (-2, 2),
      (-4, -5.5),
      (1, 2)
    ]
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
    We'll use the `sorted` function with a custom `key` function that will calculate the absolute value of the difference between the two elements of each tuple.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's write that `key` function first as a regular function:
    """)
    return


@app.function
def sort_key(t):
    return abs(t[0] - t[1])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's test it out on a few inputs:
    """)
    return


@app.cell
def _():
    data = [(-2, 2), (-1, 1), (10, 13)]
    return (data,)


@app.cell
def _(data):
    for t in data:
        print(t[0], t[1], sort_key(t))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's define our sorting function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It needs to take a list of tuples (or more generally a sequence of sequences, each of which contains two elements (at least)), and return a sorted list using our key function, in descending order.
    """)
    return


@app.function
def sort_by_abs_diff(l):
    return sorted(l, key=sort_key)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's try it out and see how that works:
    """)
    return


@app.cell
def _(data):
    sort_by_abs_diff(data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Looking good, but we want the list to be sorted in descending order - currently it is sorting in ascending order (from smallest absolute diff to largest) - let's reverse the sort direction, and while we're at it we'll use a lambda function since that key function is simple enough that we don't need to use a `def`:
    """)
    return


@app.function
def sort_by_abs_diff_1(l):
    return sorted(l, key=lambda t: abs(t[0] - t[1]), reverse=True)


@app.cell
def _(data):
    sort_by_abs_diff_1(data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's try it out with the example given in the question:
    """)
    return


@app.cell
def _(l):
    sort_by_abs_diff_1(l)
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
    Given the following data:
    """)
    return


@app.cell
def _():
    suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
    ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']
    return ranks, suits


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that given those two inputs, returns a list with all 52 cards, i.e.

    ```
    [
      ['2s', '3s', ..., 'Ks', 'As'],
      ['2h', '3h', ..., 'Kh', 'Ah'],
      ...
    ]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then, enhance this function so that an optional argument can be used to specify whether the cards in each suit should be sorted in ascending or descending rank order (assume `A` has the highest rank in its suit).
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
    We've already seen this exercise before - when we created the deck of cards (but as tuples).

    Here we want to create a card as a single string wirh rank and suit - but the approach for creating the deck is similar.
    """)
    return


@app.function
def deck(suits, ranks):
    deck = [
        [r + s for r in ranks]
        for s in suits
    ]
    return deck


@app.cell
def _(ranks, suits):
    print(deck(suits, ranks))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we need to turn our attention to sorting the ranks.
    """)
    return


@app.cell
def _(ranks):
    ranks
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we just try sorting by the natural sort order, what do we get?
    """)
    return


@app.cell
def _(ranks):
    sorted(ranks)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we'll definitely need to specify a key.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The problem is that we are dealing with strings - some of which contain digits (`2-10`) and some of which contain face cards (`J, Q, K, A`).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we need to somehow define the sort order of each of the cards. An easy way to do this would be to create an associative array that can be used to map the rank symbol (`2, 3, ..., 10, J, Q, K, A`) to a rank number (`1, 2, 3, ..., 10, 11, 12, 13`).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are different ways we could do this, maybe a dictionary with the rank symbols as keys, and the rank number as the corresponding value. That would work just fine - let's try it out:
    """)
    return


@app.cell
def _():
    rank_order = {
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        '10': 9,
        'J': 10,
        'Q': 11,
        'K': 12,
        'A': 13
    }
    return (rank_order,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To sort the `ranks` using this mapping, we could do this:
    """)
    return


@app.cell
def _(rank_order, ranks):
    sorted(ranks, key=lambda rank: rank_order[rank])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And for descending order:
    """)
    return


@app.cell
def _(rank_order, ranks):
    sorted(ranks, key=lambda rank: rank_order[rank], reverse=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can then use this in our function:
    """)
    return


@app.cell
def _(rank_order):
    def deck_1(suits, ranks, *, reverse=False):
        deck = [[r + s for r in sorted(ranks, key=lambda rank: rank_order[rank], reverse=reverse)] for s in suits]
        return deck

    return (deck_1,)


@app.cell
def _(deck_1, ranks, suits):
    print(deck_1(suits, ranks))
    return


@app.cell
def _(deck_1, ranks, suits):
    print(deck_1(suits, ranks, reverse=True))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see this approach works well.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But I didn't particularly enjoy writing that dictionary by hand!!!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, another way to do this is to create another list with the rank numbers, and zip that up with the ranks themselves:
    """)
    return


@app.cell
def _(ranks):
    ranks
    return


@app.cell
def _():
    rank_numbers = list(range(1, 14))
    rank_numbers
    return (rank_numbers,)


@app.cell
def _(rank_numbers, ranks):
    rank_orders = list(zip(ranks, rank_numbers))
    rank_orders
    return (rank_orders,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can then sort these ranks this way:
    """)
    return


@app.cell
def _(rank_orders):
    sorted(rank_orders, key=lambda t: t[1])
    return


@app.cell
def _(rank_orders):
    sorted(rank_orders, key=lambda t: t[1], reverse=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, we're only interested in the sorted symbols, not the attached rank number:
    """)
    return


@app.cell
def _(rank_orders):
    [rank for rank, rank_number in sorted(rank_orders, key=lambda t: t[1], reverse=True)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So now let's re-write our function to use this approach:
    """)
    return


@app.function
def deck_2(suits, ranks, *, reverse=False):
    ordered_ranks = [rank for rank, rank_number in sorted(list(zip(ranks, range(1, 14))), key=lambda t: t[1], reverse=reverse)]
    return [[r + s for r in ordered_ranks] for s in suits]


@app.cell
def _(ranks, suits):
    print(deck_2(suits, ranks, reverse=True))
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
    Suppose we are given some data consisting of symbols (the keys in the dictionary) and values being a tuple containing Open/High/Low/Close values for that symbol.

    For example:
    """)
    return


@app.cell
def _():
    data_1 = {'S1': (100, 200, 80, 180), 'S2': (10, 20, 8, 18), 'S3': (50, 150, 50, 150)}
    return (data_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that given this data as input, returns the symbol whose `high - low` is smallest.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Expand on your function so that it will either return the symbol with smallest or largest high/low difference, based on an extra argument passed to the function.
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
    We know that we can also specify a `key` argument for `min` and `max`, similar to the `sorted` function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can use this key to compute `high - low` and base our minimum on that.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But what are we "sorting"? The keys of the dictionary...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So we want to find the "smallest" key in the dictionary with an order based `high - low` for each key, which is in fact `data[key][1] - data[key][2]`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's just see this with a single key first:
    """)
    return


@app.cell
def _():
    k = 'S1'
    return (k,)


@app.cell
def _(data_1, k):
    data_1[k]
    return


@app.cell
def _(data_1, k):
    high = data_1[k][1]
    low = data_1[k][2]
    return high, low


@app.cell
def _(high, low):
    high, low
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's apply `min` to the dictionary keys:
    """)
    return


@app.cell
def _(data_1):
    min(data_1.keys())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    or even just:
    """)
    return


@app.cell
def _(data_1):
    min(data_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    since by default, the keys are iterated when we iterate a dictionary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But of course, the `min` function here based the sort order on the natural order of the keys - instead we want to sort based on the `high - low` difference.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Question is, what value will the `key` function receive?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since we are iterating over the **keys** of the dictionary, that's what the key function will receive - the keys of the dictionary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, our key function needs to use that key, to then calculate `high-low` for that specific key.
    """)
    return


@app.cell
def _(data_1):
    key_func = lambda key: data_1[key][1] - data_1[key][2]
    return (key_func,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's try it out:
    """)
    return


@app.cell
def _(data_1, key_func):
    print(data_1['S1'])
    print(key_func('S1'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And now we can find the minimum based on that sort order:
    """)
    return


@app.cell
def _(data_1):
    min(data_1, key=lambda key: data_1[key][1] - data_1[key][2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can now write our function to encapsulate this:
    """)
    return


@app.function
def find_min(d):
    return min(d, key=lambda key: d[key][1] - d[key][2])


@app.cell
def _(data_1):
    find_min(data_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We also want to the ability to find the max.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One way to do this is to pass in an argument to indicate whether we are looking foir the min or the max:
    """)
    return


@app.function
def find_extreme(d, *, is_min=True):
    if is_min:
        return min(d, key=lambda key: d[key][1] - d[key][2])
    else:
        return max(d, key=lambda key: d[key][1] - d[key][2])


@app.cell
def _(data_1):
    find_extreme(data_1)
    return


@app.cell
def _(data_1):
    find_extreme(data_1, is_min=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But, if you think about it, we could just as easily find the max by using the `min` function, but "reversing" the sort order by multiplying the differences by `-1`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, if we find the minimum based on these ordering values `[1, 2, 3]`, we would get the first element (associated with `1`).

    And if we find the minimum based on these ordering values `[-1, -2, -3]`, then we would get the last element (associated with `-3`). Basically the same as if we had founnd the maximum of the elements associated with `[1, 2, 3]`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we could also write our function this way:
    """)
    return


@app.function
def find_extreme_1(d, *, is_min=True):
    mult = 1 if is_min else -1
    return min(d, key=lambda key: mult * (d[key][1] - d[key][2]))


@app.cell
def _(data_1):
    (find_extreme_1(data_1), find_extreme_1(data_1, is_min=False))
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
    Given data that might look like this:
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
    where each tuple consists of the following data:
    ```
    (symbol, open, high, low, close, volume)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use the `filter` function to generate a list of rows where the `close` value is more than `10%` away from the `high` value.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Once you have done this succesfully, modify your code so that we can use any value for the percentage instead of this fixed 10%.
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
    First, let's look at a single record and see how we might calculate the percentage difference between `close` and `high` (as a percentage of `high`).
    """)
    return


@app.cell
def _():
    row = ('ADGF', 4.31, 4.55, 4.31, 4.54, 10200)
    return (row,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can extract the `close` and `high` values:
    """)
    return


@app.cell
def _(row):
    close = row[4]
    high_1 = row[2]
    return close, high_1


@app.cell
def _(close, high_1):
    (close, high_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can calculate the percentage this way:
    """)
    return


@app.cell
def _(close, high_1):
    abs(close - high_1) / high_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And then we'll want to find only those rows where that percentage is > 0.1 (10%).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll use the `filter` function which will be applied to `quotes` - a list of these tuples. So the predicate function in `filter` will receive the tuple as its argument, and our predicate function needs to return `True` if the difference is more than 10%, and `False` otherwise.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's write the predicate function first as a regular function:
    """)
    return


@app.function
def is_more_than_10(t):
    close = t[4]
    high = t[2]
    diff = abs(close - high) / high
    return diff > 0.1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can test it on a few rows:
    """)
    return


@app.cell
def _():
    is_more_than_10(('ADGF', 4.31, 4.55, 4.31, 4.54, 10200))
    return


@app.cell
def _():
    is_more_than_10(('ABCO', 48.75, 50.41, 46.9, 50.37, 66300))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's fudge the numbers to make sure `True` is returned when appropriate:
    """)
    return


@app.cell
def _():
    is_more_than_10(('ABCO', 48.75, 100, 46.9, 50.37, 66300))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can use this predicate with a filter:
    """)
    return


@app.cell
def _(quotes):
    list(filter(is_more_than_10, quotes))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can simplify our predicate function:
    """)
    return


@app.function
def is_more_than_10_1(t):
    return abs(t[4] - t[2]) / t[2] > 0.1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could also use a lambda in this case:
    """)
    return


@app.cell
def _(quotes):
    list(filter(lambda t: abs(t[4] - t[2]) / t[2] > 0.1, quotes))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But I want to use the `def` version of the predicate, because now we want the ability to specify any value for the threshold (hardcoded to 10% at the moment).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The problem is that the predicate function in `filter` will only receive the tuple - we cannot additional pass in the threshold value.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could certainly write different predicate functions:
    """)
    return


@app.cell
def _():
    def is_more_than_5(t):
        return abs(t[4] - t[2]) / t[2] > 0.05

    def is_more_than_1(t):
        return abs(t[4] - t[2]) / t[2] > 0.01

    return is_more_than_1, is_more_than_5


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And then use them for filtering:
    """)
    return


@app.cell
def _(is_more_than_5, quotes):
    list(filter(is_more_than_5, quotes))
    return


@app.cell
def _(is_more_than_1, quotes):
    list(filter(is_more_than_1, quotes))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But this is very repetitive code, and we can do much better by using... a closure! Remember the partial example we did just now? We can use a similar approach here, to generate predicate functions with the desired threshold values.
    """)
    return


@app.function
def more_than(threshold):
    def predicate(t):
        return abs(t[4] - t[2]) / t[2] > threshold
    return predicate


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, when we call `more_than(0.1)` we'll end up with a predicate function where the `threshold` will be set to `0.1`:
    """)
    return


@app.cell
def _():
    pred = more_than(0.1)
    return (pred,)


@app.cell
def _(pred):
    pred(('ABCO', 48.75, 100, 46.9, 50.37, 66300))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly, we can create a predicate function with a threshold of `0.05`:
    """)
    return


@app.cell
def _():
    pred_1 = more_than(0.05)
    return (pred_1,)


@app.cell
def _(pred_1):
    pred_1(('ABCW', 0.52, 0.61, 0.52, 0.53, 83000))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So now, we can easily filter based on any particular threshold this way:
    """)
    return


@app.cell
def _(quotes):
    list(filter(more_than(0.1), quotes))
    return


@app.cell
def _(quotes):
    list(filter(more_than(0.05), quotes))
    return


@app.cell
def _(quotes):
    list(filter(more_than(0.01), quotes))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 5
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given an arbitrary list of numbers, write an expression that returns the smallest value in the list based on the absolute values of ech number.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, given the list:
    """)
    return


@app.cell
def _():
    l_1 = [5, 6, -4, 8]
    return (l_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your expression should return `-4`.
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
    Let's recall that the `min` function, like the `sorted` (and `max`) functions can take a key function to specify a custom ordering.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In this case, we want to order the numbers based on the absolute value of each one, and then find the minimum value based on that ordering.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We don't even need to write the key function, it already exists: `abs`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we can use it directly with the `min` function:
    """)
    return


@app.cell
def _(l_1):
    min(l_1, key=abs)
    return


if __name__ == "__main__":
    app.run()
