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
    ### Selecting Data
    """)
    return


@app.cell
def _():
    import numpy as np
    import pandas as pd

    return np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's build a data frame up:
    """)
    return


@app.cell
def _(np, pd):
    arr = np.arange(9).reshape(3, 3)
    df = pd.DataFrame(
        arr, 
        columns=['c1', 'c2', 'c3'], 
        index=['r1', 'r2', 'r3'])
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can think of this a Series of Series objects (`c1`, `c2`, `c3`).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And the index for `df` (an index on the columns) is:
    """)
    return


@app.cell
def _(df):
    df.index
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We know we can retrieve elements from a Series object using the explicit index:
    """)
    return


@app.cell
def _(df):
    df['c2']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, we get the second column back, and the row index is preserved.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that `[]` will not use the implicit index:
    """)
    return


@app.cell
def _(df):
    try:
        df[0]
    except KeyError as ex:
        print('KeyError:', ex)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now that we have a single column, a `Series` essentially, we can easily get to a specific element of the column by using either the explicit or the implicit index.
    """)
    return


@app.cell
def _(df):
    df['c2'][1]
    return


@app.cell
def _(df):
    df['c2']['r2']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But just like we saw with `Series` objects, the preferred way to access data in a `DataFrame` is by using the `loc` and `iloc` attributes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The difference is that we are now using NumPy array accessing (in a sense), and recall that with NumPy 2-D arrays we access data using `[row, index]`:
    """)
    return


@app.cell
def _(df):
    df.values[1, 2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When we use `iloc` on a data frame, we are essentially following the same `row, column` pattern:
    """)
    return


@app.cell
def _(df):
    df.iloc[1, 2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And, in fact, the same holds even if we use the explicit index:
    """)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.loc['r2', 'c3']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see this is very different than when we used the `[]` - in that case we are looking at the data frame as if it were a series of series - not a NumPy 2-D array. I recommend, just like I did with `Series` objects, that you stay away from the `[]` notation, and instead rely on `loc` and `iloc`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Slicing and fancy indexing works the same way using `loc` and `iloc`:
    """)
    return


@app.cell
def _(df):
    print(df)
    df.loc['r1': 'r2', 'c2': 'c3']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And just like Series slicing, note that the endpoint of the slice is **included** in the result, unlike slicing with the implicit (positional) index:
    """)
    return


@app.cell
def _(df):
    print(df)
    df.iloc[0:1, 1:2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we want to slice the columns and include all the rows, we just specify `:` for the row slice:
    """)
    return


@app.cell
def _(df):
    df.iloc[:, 1:2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we want all the columns for a specific slice of rows we can use `:` for the column slice:
    """)
    return


@app.cell
def _(df):
    df.iloc[0:2, :]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But in this case, we can actually omit the column slice altogether:
    """)
    return


@app.cell
def _(df):
    df.iloc[0:2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Fancy indexing works as expected:
    """)
    return


@app.cell
def _(df):
    df.loc[:, ['c1', 'c3']]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And with the implicit index:
    """)
    return


@app.cell
def _(df):
    df.iloc[:, [0, 2]]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, what if you want to index/slice using an implicit index in one axis and an explicit index in the other?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can use a two step process.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, suppose we want the first two rows, with columns `c1` and `c3`:
    """)
    return


@app.cell
def _(df):
    print(df)
    tmp = df.iloc[0:2, :]
    tmp
    return (tmp,)


@app.cell
def _(tmp):
    tmp.loc[:, ['c1', 'c3']]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But of course, we could do all this in one step:
    """)
    return


@app.cell
def _(df):
    df.iloc[0:2, :].loc[:, ['c1', 'c3']]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, you can replace values in the data frame using an assignment operation, just like we saw with `Series` and NumPy arrays:
    """)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.iloc[0, 0] = -10
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or even with a slice - as long as the slice is being replaced with an array (or dataframe) of the same shape, or one that can be broadcast to that shape.
    """)
    return


@app.cell
def _(df):
    df.loc['r1': 'r2', 'c1': 'c2']
    return


@app.cell
def _(df, np):
    df.loc['r1': 'r2', 'c1': 'c2'] = np.array([10, 20, 30, 40]).reshape(2, 2)
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With broadcasting we could assign a scalar value:
    """)
    return


@app.cell
def _(df):
    df.loc['r1': 'r2', 'c1': 'c2'] = -100
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or even broadcasting from a 1-D array with 2 elements (or even just a Python list):
    """)
    return


@app.cell
def _(df):
    df.loc['r1': 'r2', 'c1': 'c2'] = [100, 200]
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also replace with another Pandas `DataFrame` or `Series`, but when we do we have to be careful because of the explicit indexes!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Consider this series:
    """)
    return


@app.cell
def _(pd):
    ser = pd.Series([-10, -20], index=['n1', 'n2'])
    ser
    return (ser,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's replace a slice of the same shape in `df`:
    """)
    return


@app.cell
def _(df):
    df.iloc[0:2, 0:2]
    return


@app.cell
def _(df, ser):
    df.iloc[0:2, 0:2] = ser
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You'll notice the missing values (`NaN` which we'll cover in some more detail soon).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The reason for this is that the index on the series `ser` did not match any index in `df`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we truly want to just replace the values without worrying about the index on `ser`, we can do it this way:
    """)
    return


@app.cell
def _(df, ser):
    df.iloc[0:2, 0:2] = ser.values
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also use boolean masking to select elements, but we'll come back to that later.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pandas data selection can get more complicated.

    If you're interested in reading up more on it, you can look at the Pandas docs:

    https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
    """)
    return


if __name__ == "__main__":
    app.run()
