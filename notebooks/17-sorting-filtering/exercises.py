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
    ### Exercises
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
    _l = [(1, 2), (-4, -5.5), (10, -10), (-2, 2)]
    return


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
    return


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
    data = {
        'S1': (100, 200, 80, 180),
        'S2': (10, 20, 8, 18),
        'S3': (50, 150, 50, 150)
    }
    return


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
    return


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
    _l = [5, 6, -4, 8]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your expression should return `-4`.
    """)
    return


if __name__ == "__main__":
    app.run()
