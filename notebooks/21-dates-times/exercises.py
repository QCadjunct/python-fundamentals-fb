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
    Write a function that, given an epoch timestamp, returns a `datetime` object set to the beginning of that month (so midnight of the first day of the month).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, given the epoch time `12345678.9`, your function should return:
    ```
    datetime.datetime(1970, 5, 1, 0, 0)
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
    Write a function that returns the difference in hours between two dates provided as Python standard ISO formatted strings, rounded to the nearest hour. For simplicity, assume that these dates do not contain fractional seconds.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, given these two dates:
    ```
    2001-01-01T13:50:23
    ```

    and
    ```
    2001-06-12T14:23:50
    ```

    your result should be `3889` hours.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Question 3
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that can be used to consistently format `datetime` objects into strings with some default format, but allows the caller to override the default format.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, the default format could be `mm/dd/yyyy hh:mm:ss am/pm`, but your function allows itself to be called with some argument that can override that format.
    """)
    return


if __name__ == "__main__":
    app.run()
