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
    Given these two lists:
    """)
    return


@app.cell
def _():
    widgets = [f'w{i}' for i in range(1, 21)]
    skus = [f'sku{i}' for i in range(1, len(widgets) + 1)]
    return skus, widgets


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that uses the `zip` function to generate a dictionary with keys from the `widgets`, and values from the `skus`, i.e.:

    ```
    {
      'w1': 'sku1',
      'w2': 'sku2',
      ...
      'w20': 'sku20'
    }
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
    Let's see what's contained in `widgets` and `skus`:
    """)
    return


@app.cell
def _(widgets):
    print(widgets)
    return


@app.cell
def _(skus):
    print(skus)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can use the `zip` function to create tuples with the widgets and their corresponding skus:
    """)
    return


@app.cell
def _(skus, widgets):
    print(list(zip(widgets, skus)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What we really want though is a dictionary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could use a dictionary comprehension to do this:
    """)
    return


@app.cell
def _(skus, widgets):
    {widget: sku for widget, sku in zip(widgets, skus)}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But, recall that the `dict` object is capable of handling a sequence of 2-element sequences:
    """)
    return


@app.cell
def _():
    dict([('a', 10), ('b', 20)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we can actually use this instead of a comprehension:
    """)
    return


@app.cell
def _(skus, widgets):
    dict(zip(widgets, skus))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's finally write our function:
    """)
    return


@app.function
def widget_skus(widgets, skus):
    return dict(zip(widgets, skus))


@app.cell
def _(skus, widgets):
    print(widget_skus(widgets, skus))
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
    Write a function that given those two inputs, returns a list with all 52 cards, consisting of tuples `(rank, suit)`, i.e.

    ```
    [
      [('2', 's'), ('3', 's'), ..., ('K', 's'), ('A', 's')],
      [('2', 'h'), ('3', 'h'), ..., ('K', 'h'), ('A', 'h')],
      ...
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
    Let's first see what suits and ranks contain:
    """)
    return


@app.cell
def _(suits):
    suits
    return


@app.cell
def _(ranks):
    ranks
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start writing our function to generate the deck of cards:
    """)
    return


@app.function
def deck(suits, ranks):
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    return deck


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And let's see what we get:
    """)
    return


@app.cell
def _(ranks, suits):
    deck(suits, ranks)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So that's not quite what we want, we want each suit to be a separate list - let's fix that:
    """)
    return


@app.function
def deck_1(suits, ranks):
    deck = []
    for suit in suits:
        cards = []
        for rank in ranks:
            cards.append((rank, suit))
        deck.append(cards)
    return deck


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And let's try that now:
    """)
    return


@app.cell
def _(ranks, suits):
    print(deck_1(suits, ranks))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    OK, so this works, but notice how we implemented our code - we started by creating empty lists, and then appending things to them - when we see things like that, and assuming the code is not too complicated, we really should look at comprehensions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, let's re-write our function to use comprehensions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First, for the individual suits, we could generate the cards in the suit this way:
    """)
    return


@app.cell
def _(ranks):
    s = 'h'
    [(r, s) for r in ranks]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And then we would nest this inside another comprehension that loops through each suit:
    """)
    return


@app.cell
def _(ranks, suits):
    [
        [(r, s) for r in ranks]
        for s in suits
    ]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So let's now use that inside our function:
    """)
    return


@app.function
def deck_2(suits, ranks):
    deck = [[(r, s) for r in ranks] for s in suits]
    return deck


@app.cell
def _(ranks, suits):
    print(deck_2(suits, ranks))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So this works fine, but we can use the `zip` function to make this even simpler.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course we cannot just zip `suits` and `ranks` since `suits` only contains 4 characters:
    """)
    return


@app.cell
def _(ranks, suits):
    list(zip(suits, ranks))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But, what we could do is repeat each character in `suits` thirteen times, and zip each of those with the ranks.
    """)
    return


@app.cell
def _(suits):
    suits[0]
    return


@app.cell
def _(suits):
    suits[0] * 13
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can zip that instead:
    """)
    return


@app.cell
def _(ranks, suits):
    print(list(zip(ranks, suits[0] * 13)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now all we need to do is repeat this for each suit:
    """)
    return


@app.cell
def _(ranks, suits):
    print([list(zip(ranks, suit * 13)) for suit in suits])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So we can rewrite our function this way:
    """)
    return


@app.function
def deck_3(suits, ranks):
    return [list(zip(ranks, suit * 13)) for suit in suits]


@app.cell
def _(ranks, suits):
    print(deck_3(suits, ranks))
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
    Write a function that receives two arguments:
    - a list of numbers
    - a keyword-only argument `reverse` that defaults to `False` and indicates an ascending sort, but a value of `True` indicates a descending sort
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your function should return three values:
    - a list of the numbers, but sorted (ascending/descending depending on value of `reverse`)
    - the minimum value in the list (this is not affected by the value of `reverse`)
    - the maximum value in the list (this is not affected by the value of `reverse`)
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
    Let's create some sample data first:
    """)
    return


@app.cell
def _():
    data = [10, 3, -5, 3.14, 100, 1]
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    we can sort this data using the `sorted` function, as well as specify whether the order shoudl be ascending or descending:
    """)
    return


@app.cell
def _(data):
    sorted(data)
    return


@app.cell
def _(data):
    sorted(data, reverse=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can find the minimum using the `min` function:
    """)
    return


@app.cell
def _(data):
    min(data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And the maximum using the `max` function:
    """)
    return


@app.cell
def _(data):
    max(data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, let's just package this up into a function:
    """)
    return


@app.function
def list_info(data, *, reverse=False):
    sorted_data = sorted(data, reverse=reverse)
    minimum = min(data)
    maximum = max(data)
    return sorted_data, minimum, maximum


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And let's try it out with our data:
    """)
    return


@app.cell
def _(data):
    list_info(data)
    return


@app.cell
def _(data):
    list_info(data, reverse=True)
    return


if __name__ == "__main__":
    app.run()
