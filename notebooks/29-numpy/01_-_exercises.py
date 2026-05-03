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
    The accompanying file `data.csv` contains information for the value `x` of something observed at time `t`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given this data, we want to calculate the rate of change of this value over time - we'll do this by taking two consecutive observations, say $x(t_i)$ and $x(t_{i+1})$ and approximate the rate of change using this formula:

    $$
    v(t_{i+1}) = \frac{x(t_{i+1}) - x(t_i)}{t_{i+1} - t_i}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, if the data looks like this:

    ```
    t     x
    0.1   10
    0.2   12
    0.4   14
    0.5   15
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then the first row of data would be considered $t_0$, the second row $t_1$, etc
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can start approximating the rate of change starting at $v_1$ which would be calculated as:

    $$
    v_1 = \frac{12 - 10}{0.2 - 0.1} = 20.0
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly, $v_2$ would be calculated as:

    $$
    v_2 = \frac{14 - 12}{0.4 - 0.2} = 10.0
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use NumPy arrays to create an array that holds the calculated rates of change and determine the minimum, maximum, average and standard deviation of the rate of change.
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
    In linear regression we try to find the coefficients `m` (slope) and `c` (y-intercept) of a straight line

    $$
    y = mx + c
    $$

    that provides the "best" fit given some `x` and `y` data. This formula then allows to predict `y` values for given `x` values.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given an array of `n` `(x, y)` data pairs, these coefficients can be calculated very simply.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A bit of terminology first:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Let `X` mean the column of `X` values.
    - Let `Y` mean the column of `Y` values.
    - Let `XX` mean a column calculated by multiplying each `x` in the `X` column by itself
    - Let `XY` mean a column calculated by multiplying the `x` and `y` values from the `X` and `Y` columns
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then, given some column (say `X`), this symbol: $\sum{X}$ means the sum of all the elements in the column.

    Similarly, the symbol $\sum{XY}$ means the sum of the values obtained by multiplying (pairwise) the values in `X` and `Y`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given those definitions, the formulas for calculating the "best" values of `m` and `c` are given by:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$
    m = \frac{n\sum{XY} - \sum{X}\sum{Y}}{n\sum{XX} - (\sum{X})^2}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$
    c = \frac{\sum{Y}\sum{XX} - \sum{X}\sum{XY}}{n\sum{XX} - (\sum{X})^2}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    (where `n` is the number of `(x,y)` pairs in our data set.)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Using the same data we saw in Question 1, calculate the values for `m` and `c` for that data set given the formulas above.

    You can think of the `t` column in the data as the `X` column, and the `x` values in the data as the `Y` column - we are trying to predict the value of `x` given a value of `t`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This will result in a straight line that "best" fits through the data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Compare the slope of this regression line to the average rate of change you calculated in Question 1.
    """)
    return


if __name__ == "__main__":
    app.run()
