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
    ### The `time` Module
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    https://docs.python.org/3/library/time.html
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `time` module is like the low level handling of dates and times in Python.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we understand it, we understand how dates and times are handled in Python - but we more often use higher level libraries that hide these details from us and make our programming life easier.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In addition to date and time handling, the `time` module also gives us some extra functions such as `perf_counter` and `sleep`.
    """)
    return


@app.cell
def _():
    from time import perf_counter, sleep

    return perf_counter, sleep


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `perf_counter` gives us the elapsed time (in fractional seconds) since the program started running - so we really use `perf_counter` to calculate elapsed times between two calls to it:
    """)
    return


@app.cell
def _(perf_counter):
    start = perf_counter()
    return (start,)


@app.cell
def _(start):
    start
    return


@app.cell
def _(perf_counter):
    end = perf_counter()
    return (end,)


@app.cell
def _(end):
    end
    return


@app.cell
def _(end, start):
    elapsed = end - start
    return (elapsed,)


@app.cell
def _(elapsed):
    elapsed
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This can be very useful for timing things, as we saw earlier with the timing decorator example we did.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We also have the `sleep()` function, which essentially pauses our program execution for the specified number of seconds (can be a float).
    """)
    return


@app.cell
def _(perf_counter, sleep):
    start_1 = perf_counter()
    sleep(3)
    end_1 = perf_counter()
    elapsed_1 = end_1 - start_1
    print(elapsed_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, execution was paused for **about** 3 seconds.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This can be useful when your program needs to wait for an external resource to become available.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Maybe you are trying to connect to a database, and the connection is down (maybe some temporary networking issue). Instead of killing the program, you might try to repeat the attempt at connecting, waiting a bit before each attempt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's turn our attention to dates and times now.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    At it's heart, Python uses an **epoch** based system. A specific point in time is measured relative to some base (`0`) point.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On Unix system, that base time, called the **epoch** is `1970-01-01 00:00:00 UTC` with no DST.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can convert an epoch time (a number of elapsed seconds), by using the `gmtime` function which will convert that epoch time into a `time_struct` object:
    """)
    return


@app.cell
def _():
    from time import gmtime

    return (gmtime,)


@app.cell
def _(gmtime):
    gmtime(1_000_000_000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To see what the epoch is on your system, you can use `gmtime` with `0` seconds:
    """)
    return


@app.cell
def _(gmtime):
    gmtime(0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, on my system (a Mac), my epoch is the standard Unix epoch. Modern versions of Windows should be the same.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For dates before 1970, we would use negative offsets:
    """)
    return


@app.cell
def _(gmtime):
    gmtime(-1_000_000_000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To get the current epoch time, we can use the `time()` function:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Yes, I know this can be confusing - a module named `time` and a function named `time`!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can use it in two different ways:
    """)
    return


@app.cell
def _():
    import time
    from time import time as time_fn

    return (time,)


@app.cell
def _(time):
    time.time()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or we can import the `time` function directly into our module:
    """)
    return


@app.cell
def _(time, time_fn):
    time_fn()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, this is an epoch time, and we can convert it into a `time_struct` using the `gmtime` function:
    """)
    return


@app.cell
def _(gmtime, time, time_fn):
    gmtime(time_fn())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that the current time we see here is in UTC, since the epoch is in UTC, and we calculated the number of elapsed seconds since that time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Also note that `gmtime` ignores the non-integer portion of the argument.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can access the individual fields of this `time_struct` structure, using either positional indexes, or the property names (this structure is something called a named tuple - a tuple of values, but where each element of the tuple can be accessed by name also).
    """)
    return


@app.cell
def _(gmtime, time, time_fn):
    current = gmtime(time_fn())
    return (current,)


@app.cell
def _(current):
    current[0], current.tm_year
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Generally we use the named variant.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can perform date calculations, such as adding 2 days to the current date:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since date/times are specified in seconds (epoch time), we just add or subtract these floats.
    """)
    return


@app.cell
def _(time, time_fn):
    now = time_fn()
    return (now,)


@app.cell
def _(now):
    tomorrow = now + (24 * 60 * 60)
    return (tomorrow,)


@app.cell
def _(now, tomorrow):
    now, tomorrow
    return


@app.cell
def _(gmtime, now):
    gmtime(now)
    return


@app.cell
def _(gmtime, tomorrow):
    gmtime(tomorrow)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can get the difference between two times as well:
    """)
    return


@app.cell
def _(now, tomorrow):
    tomorrow - now
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which is in seconds.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We saw how to convert an epoch time to a `time_struct` object - but we may want to also do the inverse operation - convert a `time_struct` object into an epoch time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To do this we can use the `timegm` function in the `calendar` module:
    """)
    return


@app.cell
def _():
    from calendar import timegm

    return (timegm,)


@app.cell
def _(time, time_fn):
    now_epoch = time_fn()
    return (now_epoch,)


@app.cell
def _(now_epoch):
    now_epoch
    return


@app.cell
def _(gmtime, now_epoch):
    now_struct = gmtime(now_epoch)
    return (now_struct,)


@app.cell
def _(now_struct):
    now_struct
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can convert it back to an epoch time:
    """)
    return


@app.cell
def _(now_struct, timegm):
    timegm(now_struct)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Which as you can see is the same as our original epoch time (minus the digits after the decimal point - remember that `gmtime` ignores fractional seconds).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Formatting a time_struct object
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Obviously, seeing an epoch time such as: 1587259290 is not very useful
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So we can convert it to a human readable format, using `strftime` and some formatting directives which we covered in the lecture.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But `strftime` does not work with an epoch time directly - it requires a `time_struct` object, so we'll need to convert our epoch time first:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's try to format our current time into various formats:
    """)
    return


@app.cell
def _(gmtime, time, time_fn):
    now_1 = gmtime(time_fn())
    return (now_1,)


@app.cell
def _(now_1):
    now_1
    return


@app.cell
def _():
    from time import strftime

    return (strftime,)


@app.cell
def _(now_1, strftime):
    strftime('%Y/%m/%d', now_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that the directives are the characters prefixed with a `%`. The remaining characters we can make whatever we want.
    """)
    return


@app.cell
def _(now_1, strftime):
    strftime('%A is the best day of the week!', now_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    (and if the day you see displayed here does not seem to match your current day, remember that the time is in UTC - so the weekday is in the UTC time zone too!)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For me, a late Saturday afternoon, is actual an early Sunday morning in UTC.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can find a list of all the supported formatting directives for dates and times here:

    https://docs.python.org/3/library/time.html#time.strftime
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There's actually some additional directives you can use, and they are listed here:

    https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So we can format a `time_struct` into human readable format.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But we can perform the reverse operation - parsing date and time information out of some string.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But Python cannot do that magically - we have to tell it precisely how that string has been formatted.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, we may have this date string:
    """)
    return


@app.cell
def _():
    d = "12/11/10"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Interesting, yes?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    is this Y/M/D, M/D/Y, D/M/Y, ...?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Just looking at this date, we have no idea. You will have to infer the format based on looking at additional data from your data source, or from some documentation telling you the date format.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And this, by the way, is why we have some standards for date and time string representations!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By contrast, this ISO 8601 formatted date, is a standard that we everyone can adhere to and follow (if only!):
    """)
    return


@app.cell
def _():
    d_1 = '2012-11-10'
    return (d_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So assuming we know the format, we can now parse these numbers to create a `time_struct`:
    """)
    return


@app.cell
def _():
    from time import strptime

    return (strptime,)


@app.cell
def _(d_1, strptime):
    strptime(d_1, '%Y-%m-%d')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, we can even parse crazy formats too - hopefully you don't encounter things like that too often in your data sources!
    """)
    return


@app.cell
def _():
    s = 'Monday, April 18, in the year 2020 CE'
    return (s,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To parse this, we simply have to identify the pieces in that string that can be described using a directive.
    """)
    return


@app.cell
def _():
    fmt = '%A, %B %d, in the year %Y CE'
    return (fmt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And now we can parse it using this (highly specific) format:
    """)
    return


@app.cell
def _(fmt, s, strptime):
    strptime(s, fmt)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course this same format string cannot handle a different date format:
    """)
    return


@app.cell
def _():
    s_1 = 'Monday, April 18, 2020'
    return (s_1,)


@app.cell
def _(fmt, s_1, strptime):
    try:
        strptime(s_1, fmt)
    except ValueError as ex:
        print('ValueError:', ex)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This means your code will have to be able to define (and somehow store) different formats based on the data you are ingesting. This can be a real pain, so later we'll look at a 3rd party library that can make this, and dealing with timezones, a whole lot easier!
    """)
    return


if __name__ == "__main__":
    app.run()
