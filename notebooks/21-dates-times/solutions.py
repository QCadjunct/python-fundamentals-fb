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
    ##### Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First we'll need to import the `datetime` object:
    """)
    return


@app.cell
def _():
    from datetime import datetime

    return (datetime,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can easily convert an epoch timestamp to a `datetime` object by using the `fromtimestamp` method.
    """)
    return


@app.cell
def _(datetime):
    dt = datetime.fromtimestamp(12345678.9)
    return (dt,)


@app.cell
def _(dt):
    dt
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next, we could replace the day, hour, minutes, and seconds with `1` or `0` as needed, or we could create a new `datetime` object just picking up the year and month from this one:
    """)
    return


@app.cell
def _(dt):
    dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    or alternatively:
    """)
    return


@app.cell
def _(datetime, dt):
    datetime(year=dt.year, month=dt.month, day=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's package this up into a function:
    """)
    return


@app.cell
def _(datetime):
    def month_start(epoch):
        dt = datetime.fromtimestamp(epoch)
        return datetime(year=dt.year, month=dt.month, day=1)

    return (month_start,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And let's call it:
    """)
    return


@app.cell
def _(month_start):
    month_start(12345678)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's test it out with the current (UTC) date as well:
    """)
    return


@app.cell
def _():
    import time

    return (time,)


@app.cell
def _(month_start, time):
    month_start(time.time())
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
    ##### Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start with two dates:
    """)
    return


@app.cell
def _(datetime):
    dt1 = datetime.fromisoformat('2001-01-01T13:50:23')
    dt2 = datetime.fromisoformat('2001-06-12T14:23:50')
    return dt1, dt2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To find the difference between the two objects:
    """)
    return


@app.cell
def _(dt1, dt2):
    delta = dt2 - dt1
    return (delta,)


@app.cell
def _(delta):
    delta
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also get the total delta in seconds:
    """)
    return


@app.cell
def _(delta):
    delta.total_seconds()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We want to round this to the closest hour.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An hour is `60 * 60` seconds:
    """)
    return


@app.cell
def _():
    seconds_in_hour = 60 * 60
    return (seconds_in_hour,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we want to round to the closest multiple of `seconds_in_hour`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are probably many different approaches to this, here I'll explain how I thought about the problem.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First thing is we'll want to make the total number of seconds into an integer (we are assuming no fractional seconds).
    """)
    return


@app.cell
def _(delta):
    delta_seconds = int(delta.total_seconds())
    return (delta_seconds,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next, we'll calculate the number of whole hours in that:
    """)
    return


@app.cell
def _(delta_seconds, seconds_in_hour):
    complete_hours = delta_seconds // seconds_in_hour
    complete_hours
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And the remaining number of seconds is:
    """)
    return


@app.cell
def _(delta_seconds, seconds_in_hour):
    remaining_seconds = delta_seconds % seconds_in_hour
    remaining_seconds
    return (remaining_seconds,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The number of (fractional) hours in these seconds is:
    """)
    return


@app.cell
def _(remaining_seconds, seconds_in_hour):
    remaining_seconds / seconds_in_hour
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can simply `round` this number to determine whether we are closer to `0` or `1` for the farctional hour:
    """)
    return


@app.cell
def _(remaining_seconds, seconds_in_hour):
    round(remaining_seconds / seconds_in_hour)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's package this up into a function:
    """)
    return


@app.cell
def _(datetime):
    def num_hours(dt1, dt2):
        seconds_in_hour = 60 * 60
        dt1 = datetime.fromisoformat(dt1)
        dt2 = datetime.fromisoformat(dt2)
        delta_seconds = int((dt2 - dt1).total_seconds())
        complete_hours = delta_seconds // seconds_in_hour
        remaining_seconds = delta_seconds % seconds_in_hour
        return complete_hours + round(remaining_seconds / seconds_in_hour)

    return (num_hours,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can call this function with a few values:
    """)
    return


@app.cell
def _(num_hours):
    num_hours('2001-01-01T13:50:23', '2001-06-12T14:23:50')
    return


@app.cell
def _(num_hours):
    num_hours('2001-01-01T00:00:00', '2001-01-01T01:00:00')
    return


@app.cell
def _(num_hours):
    num_hours('2001-01-01T00:00:00', '2001-01-02T01:50:00')
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's write the function definition first:
    """)
    return


@app.function
def dt_to_string(dt, fmt='%m/%d/%y %I:%M:%S%p'):
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice how I set the default format string in the parameter definition itself - this way if the function is called without that argument, then the default will be used.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For these types of parameters though, I prefer to force the function to specify that `fmt` argument as a keyword argument, so I can force that this way:
    """)
    return


@app.function
def dt_to_string_1(dt, *, fmt='%m/%d/%y %I:%M:%S%p'):
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's implement the function itself:
    """)
    return


@app.function
def dt_to_string_2(dt, *, fmt='%m/%d/%y %I:%M:%S%p'):
    return dt.strftime(fmt)


@app.cell
def _(datetime):
    dt_to_string_2(datetime(2020, 2, 1, 13, 34, 5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But, we can always specify an alternate format if we want to:
    """)
    return


@app.cell
def _(datetime):
    dt_to_string_2(datetime(2020, 2, 1, 13, 34, 5), fmt='%B %d, %Y')
    return


if __name__ == "__main__":
    app.run()
