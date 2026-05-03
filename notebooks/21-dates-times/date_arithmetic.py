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
    ### Date Arithmetic
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `timedelta` object is used to represent the difference (or duration) between two dates/times.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we have two dates/times, we can actually *subtract* one from the other - this will give us a `timedelta` object:
    """)
    return


@app.cell
def _():
    import datetime

    return (datetime,)


@app.cell
def _(datetime):
    dt1 = datetime.datetime.utcnow()
    dt2 = datetime.datetime.fromisoformat('2020-01-01T00:00:00')
    return dt1, dt2


@app.cell
def _(dt1, dt2):
    td = dt1 - dt2
    return (td,)


@app.cell
def _(td):
    td
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see the `timedelta` object has the elapsed time between those two datetimes with properties `days`, `seconds`, and `microseconds`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can easily calculate the total number of seconds for that duration:
    """)
    return


@app.cell
def _(td):
    td.days * 24 * 60 * 60 + td.seconds + td.microseconds / (10 ** 6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    but we can also just use the `total_seconds()` method:
    """)
    return


@app.cell
def _(td):
    td.total_seconds()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also construct our own `timedelta` object, and although we have arguments such as `days`, `seconds`, `microseconds`, we also can specify arguments for `minutes`, `hours`, `weeks` and `milliseconds` - those values will simply be all added together and converted to `days`, `seconds` and `microseconds` - these arguments are available just to make our life easier.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's create a `timedelta` object representing 2.5 hours:
    """)
    return


@app.cell
def _(datetime):
    td_1 = datetime.timedelta(hours=2, minutes=30)
    return (td_1,)


@app.cell
def _(td_1):
    td_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The nice thing now is that we can easily add or subtract `timedelta` objects from a `datetime` object for example:
    """)
    return


@app.cell
def _(datetime):
    dt = datetime.datetime.utcnow()
    return (dt,)


@app.cell
def _(dt):
    dt
    return


@app.cell
def _(dt, td_1):
    dt + td_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So `timedelta` objects can be used to perform date arithmetic, or can be the result of date arithemtic.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As an example, let's come up with a way to determine the first and last day of the month of a specified date or datetime object.
    """)
    return


@app.cell
def _():
    s = "2020-02-15T13:35:00"
    return (s,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First we'll convert this to a `datetime` object:
    """)
    return


@app.cell
def _(datetime, s):
    dt_1 = datetime.datetime.fromisoformat(s)
    return (dt_1,)


@app.cell
def _(dt_1):
    dt_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finding the first day of the month in that datetime is easy - it is always going to be the same year and month, but with day set to 1.
    """)
    return


@app.cell
def _(datetime, dt_1):
    start = datetime.datetime(year=dt_1.year, month=dt_1.month, day=1)
    return (start,)


@app.cell
def _(start):
    start
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now you'll notice that we have some time information attached to this, and that's because we created a `datetime` object - but in this case we're really not interested in the time, just the date.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So we probably should have created a `date` object, not a `datetime` object:
    """)
    return


@app.cell
def _(datetime, dt_1):
    start_1 = datetime.date(year=dt_1.year, month=dt_1.month, day=1)
    return (start_1,)


@app.cell
def _(start_1):
    start_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What happens if we add a `timedelta` object to a `date` object?
    """)
    return


@app.cell
def _(datetime):
    delta = datetime.timedelta(hours=50, minutes=30)
    return (delta,)


@app.cell
def _(delta, start_1):
    start_1 + delta
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ah, we just keep the `date` portion, but the year/month/day is calculated correctly - it basically just "truncates" the time information.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So how can we find the last day of the month?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Unlike the first day of the month, we can't speficy a hardcoded number, some months have 30 days, 31 days, and February could be 28 or 29 (depending on leap year).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One easy way to do this, is to start with the first day of the month, and add one month to it.

    This will give us the first day of the next month.

    Then we subtract one day to get the last day of the previous month.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, `timedelta` does not have a month argument - and that makes sense, since months can have different numbers of days in them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we're going to have to do this the hard way - we're going to create a new date, advancing the month by 1, but keeping an eye out in case the `month` is `12`, in which case we need to advance the `year` by `1`, and set the new `month` to `1`:
    """)
    return


@app.cell
def _(start_1):
    if start_1.month == 12:
        new_year = start_1.year + 1
        new_month = 1
    else:
        new_year = start_1.year
        new_month = start_1.month + 1
    return new_month, new_year


@app.cell
def _(new_month, new_year, start_1):
    (start_1, new_year, new_month)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can start building up our `end` date:
    """)
    return


@app.cell
def _(datetime, new_month, new_year):
    end = datetime.date(year=new_year, month=new_month, day=1)
    return (end,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is still not quite what we want, we actually need the previous day (so the last day of the previous month):
    """)
    return


@app.cell
def _(datetime, end):
    end_1 = end - datetime.timedelta(days=1)
    return (end_1,)


@app.cell
def _(end_1):
    end_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And there we have it. So now, let's package that up into a function that will return a tuple of `date` objects, for first and last day of the month specified by the input date/datetime.
    """)
    return


@app.cell
def _(datetime):
    def get_first_last(dt):
        # note that dt can be either a date or a datetime - this function works either way
        start = datetime.date(year=dt.year, month=dt.month, day=1)
    
        if start.month == 12:
            new_year = start.year + 1
            new_month = 1
        else:
            new_year = start.year
            new_month = start.month + 1
        
        end = datetime.date(new_year, new_month, 1) + datetime.timedelta(days=-1)
    
        return start, end

    return (get_first_last,)


@app.cell
def _(s):
    s
    return


@app.cell
def _(datetime, get_first_last, s):
    get_first_last(datetime.datetime.fromisoformat(s))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can test this out for a range of dates:
    """)
    return


@app.cell
def _(datetime, get_first_last):
    for year in (2020, 2021):
        for month in range(12):
            dt_2 = datetime.date(year=year, month=month + 1, day=15)
            print(dt_2, *get_first_last(dt_2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dates, times and datetimes can also be compared to each other, using `==`, `!=`, `<`, etc.
    """)
    return


@app.cell
def _(datetime):
    t1 = datetime.time(9, 30, 0)
    t2 = datetime.time(11, 0, 0)
    return t1, t2


@app.cell
def _(t1, t2):
    t1 <= t2
    return


@app.cell
def _(datetime):
    d1 = datetime.date(2020, 3, 8)
    d2 = datetime.date(2020, 5, 1)
    return d1, d2


@app.cell
def _(d1, d2):
    d2 > d1
    return


@app.cell
def _(datetime):
    dt1_1 = datetime.datetime(2020, 3, 8, 13, 30, 0)
    dt2_1 = datetime.datetime(2020, 3, 8, 13, 45, 0)
    return dt1_1, dt2_1


@app.cell
def _(dt1_1, dt2_1):
    dt1_1 < dt2_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have to be careful with comparing between the different types though - as we might expect, comparing a date without a time to a time without a date, or to a date with time, does not make much sense.
    """)
    return


@app.cell
def _(d1, t1):
    try:
        print(t1 < d1)
    except TypeError as ex:
        print(ex)
    return


@app.cell
def _(d1, dt1_1):
    try:
        print(d1 < dt1_1)
    except TypeError as ex:
        print(ex)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When you perform comparisons, make sure you are using the same data types.
    """)
    return


if __name__ == "__main__":
    app.run()
