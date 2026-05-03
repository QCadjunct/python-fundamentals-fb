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
    ### Custom Representations
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There is nothing actually new in this section, we've already seen this before.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We saw that we could customize `time_struct` string representation using special directives (`%Y`, `%m`, `%d`, etc), and the `strftime` method.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same applies with `date`, `time` and `datetime` objects too.
    """)
    return


@app.cell
def _():
    from datetime import time, date, datetime

    return date, datetime, time


@app.cell
def _(time):
    t = time(22, 30, 45)
    return (t,)


@app.cell
def _(t):
    t.strftime('The time is: %I hours, %M minutes, and %S seconds, %p')
    return


@app.cell
def _(date):
    d = date(2020, 5, 15)
    return (d,)


@app.cell
def _(d):
    d.strftime('%B %d, %Y')
    return


@app.cell
def _(datetime):
    dt = datetime(2020, 5, 15, 22, 30, 45)
    return (dt,)


@app.cell
def _(dt):
    dt.strftime('%I:%M %p on %B %d, %Y')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `date` and `time` classes do not have the reverse `strptime` function, but `datetime` does.
    """)
    return


@app.cell
def _(datetime):
    dt_1 = datetime.strptime('10:30 PM on May 15, 2020', '%I:%M %p on %B %d, %Y')
    return (dt_1,)


@app.cell
def _(dt_1):
    dt_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We also have the `fromisoformat` and `isoformat` methods, but be aware that `fromisoformat` only works with the specific ISO format used by Python (there are slight variants that the ISO format allows - and those will **not** be handled automatically by Python's `fromisoformat`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see an example of this:
    """)
    return


@app.cell
def _(dt_1):
    dt_1
    return


@app.cell
def _(dt_1):
    dt_1.isoformat()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can take that string and pass it back into `fromisoformat`:
    """)
    return


@app.cell
def _(datetime):
    datetime.fromisoformat('2020-05-15T22:30:00')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That works just fine, but now let's do this with a time zone aware timestamp:
    """)
    return


@app.cell
def _(datetime):
    datetime.fromisoformat('2020-05-15T22:30:00-05:00')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So that worked just fine, but recall that the `:` in the time zone offset is actually **optional** in the ISO 8601 specification, so this is actually valid too:

    ```
    '2020-05-15T22:30:00-0500'
    ```

    as well as this:

    ```
    '2020-05-15T22:30:00-05'
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's try these formats and see what happens:
    """)
    return


@app.cell
def _(datetime):
    try:
        datetime.fromisoformat('2020-05-15T22:30:00-0500')
    except ValueError as ex:
        print(ex)
    return


@app.cell
def _(datetime):
    try:
        datetime.fromisoformat('2020-05-15T22:30:00-05')
    except ValueError as ex:
        print(ex)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we would have to provide a custom formatter to parse these variants on the ISO 8601 standard.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll come back to this problem, when we look at the `dateutil` 3rd party library which will make these problems go away - like magic!
    """)
    return


if __name__ == "__main__":
    app.run()
