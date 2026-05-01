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
    #### Exercise 1
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given a variable `a` (containing any value), re-assign the value `"N/A"` if `a` is `None`, and leave `a` unchanged otherwise. Use an `if...else...` statement.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Exercise 2
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Do the same thing as Question 1, but this time use a ternary operator.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Exercise 3
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given an credit score `score`, assign a string value to another variable `rating` based on the following scale:

    - [0, 580) --> Poor
    - [580, 670) --> Fair
    - [670, 740) --> Good
    - [740, 800) --> Very Good
    - [800, 850] --> Excellent
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Exercise 4
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given an `elapsed` time (in seconds), write code to set a variable `magnitude` based on the following conditions:

    - if elapsed time is less than 1 minute, `magnitude` --> `'seconds'`
    - if elapsed time is more than 1 minute, but less than 1 hour, `magnitude` --> `'minutes'`
    - if elapsed time is more than 1 hour, but less than 1 day, `magnitude` --> `'hours'`
    - if elapsed time is more than 1 day, but less than 1 week: `magnitude` --> `'days'`
    - if elapsed time is more than 1 week, `magnitude` --> '`weeks'`
    """)
    return


if __name__ == "__main__":
    app.run()
