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
    ### The `datetime` Module
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    https://docs.python.org/3/library/datetime.html
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `datetime` module contains several data types (classes) that make it easier to work with dates, times and datetimes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we saw with the `time` module, at a low level we can work with epoch times - but we have to keep trasck of whether we have an epoch time (a number), or a `time_struct`, and constantly convert between the two as needed. Also, although time zones are supported, it is entirely up to us to think and deal with time zones.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The major data types that we'll look at in the `datetime` module are:
    - `date`: used for dates (year, month, day)
    - `time`: used for times (hour, minute, second), independent of date
    - `datetime`: combines both `date` and `time` objects
    - `timedelta`: used for durations between two date/time objects
    - `timezone`: used to represent time zone information as a UTC offset
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We also have to distinguish between **aware** and **naive** date and time objects.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Objects that contain time zone information are called time zone **aware** (or simply *aware*) objects, while objects that have no time zone information attached are called time zone **naive** (or simply, *naive*) objects.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Working with time zone aware objects can get difficult and easily lead to bugs (problems with not only time zones, but also daylight savings).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What most Python developers do is always work with dates and times that are:
    1. always in UTC
    2. time zone naive
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This simplifies things quite a bit - the idea is that any dates and times we ingest are immediately converted to UTC time zone and made naive.

    Now, as we work with dates and times in our program, everything is in UTC, we do not have to worry about time zones and daylight savings, and we only convert to some other time zone when we want to display a date/time to our users in their local time zone - and usually that's up to the UI to do this.

    The same idea goes for storing data (in a database, file, etc) - we always store these dates in UTC (whether aware or naive will depend on your storage solution and particular circumstances).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, in this course we're only going to focus on working with naive dates and times - and only worry about converting incoming dates and times to UTC naive.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start by looking at the `date`, `time` and `datetime` objects:
    """)
    return


@app.cell
def _():
    import datetime

    return (datetime,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To create a date we can specify the `year`, `month` and `day`:
    """)
    return


@app.cell
def _(datetime):
    dt = datetime.date(2020, 5, 1)
    return (dt,)


@app.cell
def _(dt):
    dt
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also just get the current (local) date:
    """)
    return


@app.cell
def _(datetime):
    dt_1 = datetime.date.today()
    return (dt_1,)


@app.cell
def _(dt_1):
    dt_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or we can get it from an epoch time even:
    """)
    return


@app.cell
def _():
    import time

    return (time,)


@app.cell
def _(datetime, time):
    dt_2 = datetime.date.fromtimestamp(time.time())
    return (dt_2,)


@app.cell
def _(dt_2):
    dt_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also easily convert an ISO formatted date (`YYYY-MM-DD`) without resorting to parsing directives:
    """)
    return


@app.cell
def _(datetime):
    dt_3 = datetime.date.fromisoformat('2020-12-31')
    return (dt_3,)


@app.cell
def _(dt_3):
    dt_3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can do the reverse of this and produce an ISO formatted date string:
    """)
    return


@app.cell
def _(datetime):
    dt_4 = datetime.date(2020, 12, 1)
    return (dt_4,)


@app.cell
def _(dt_4):
    dt_4.isoformat()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And `date` objects have `year`, `month` and `day` properties:
    """)
    return


@app.cell
def _(dt_4):
    (dt_4.year, dt_4.month, dt_4.day)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `time` object is very similar, except we are working with times, isolated from dates:
    """)
    return


@app.cell
def _(datetime):
    t = datetime.time(15, 30, 45)
    return (t,)


@app.cell
def _(t):
    t
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `hour` argument should be specified using a 24-hour clock, where `0` represents midnight (not `24`):
    """)
    return


@app.cell
def _(datetime):
    t_1 = datetime.time(0, 0, 0)
    return (t_1,)


@app.cell
def _(t_1):
    t_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also include microseconds:
    """)
    return


@app.cell
def _(datetime):
    t_2 = datetime.time(2, 30, 45, 135)
    return (t_2,)


@app.cell
def _(t_2):
    t_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can convert to and from an ISO representation, just like with dates:
    """)
    return


@app.cell
def _(t_2):
    t_2.isoformat()
    return


@app.cell
def _(datetime):
    t_3 = datetime.time.fromisoformat('13:34:20.000123')
    return (t_3,)


@app.cell
def _(t_3):
    t_3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And this `time` object has properties for `hour`, `minute`, `second`, `microsecond`:
    """)
    return


@app.cell
def _(t_3):
    (t_3.hour, t_3.minute, t_3.second, t_3.microsecond)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next we have the `datetime` objects (yes, in the `datetime` module...):
    """)
    return


@app.cell
def _(datetime):
    dt_5 = datetime.datetime(2020, 3, 1, 13, 30, 45, 123)
    return (dt_5,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can see the ISO string representattion of this date/time:
    """)
    return


@app.cell
def _(dt_5):
    dt_5.isoformat()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    as well as convert an ISO datetime string to a `datetime` object:
    """)
    return


@app.cell
def _(datetime):
    dt_6 = datetime.datetime.fromisoformat('2020-02-15T04:30:15')
    return (dt_6,)


@app.cell
def _(dt_6):
    dt_6
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And, just like with `time` and `date` objects, we can retrieve the individual parts of the date time using properties:
    """)
    return


@app.cell
def _(dt_6):
    (dt_6.year, dt_6.month, dt_6.day)
    return


@app.cell
def _(dt_6):
    (dt_6.hour, dt_6.minute, dt_6.second, dt_6.microsecond)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also get the current (local) date and time, in UTC as follows:
    """)
    return


@app.cell
def _(datetime):
    dt_7 = datetime.datetime.utcnow()
    return (dt_7,)


@app.cell
def _(dt_7):
    dt_7
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice that the values here are not going to be the same as your local clock (unless your local time zone **is** UTC).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, we haven't mentioned time zones in the context of `time` and `datetime` objects (does not apply to `date` objects obviously).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In part, that's because we made the decision to always work with naive UTC `time` and `datetime` objects.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But we still have to know how to deal with those time zones, at least in order to convert them to naive objects.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, suppose we have this ISO date time:
    """)
    return


@app.cell
def _():
    s = "2020-04-02T18:30:30-07:00"
    return (s,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This contains time zone information, and if we use `fromisoformat()`:
    """)
    return


@app.cell
def _(datetime, s):
    dt_8 = datetime.datetime.fromisoformat(s)
    return (dt_8,)


@app.cell
def _(dt_8):
    dt_8
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can see that the above object is time zone **aware** - it contains a property called `tzinfo`, with a definition of the offset. The time is actually recorded as `18:30:30`, so it was not converted to UTC - it was kept as is, and the time zone offset recorded.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we want to convert this to a naive UTC datetime.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before we can do this, we have a few more data types to look at: `timedelta` and `timezone`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll cover those in the next few lectures.
    """)
    return


if __name__ == "__main__":
    app.run()
