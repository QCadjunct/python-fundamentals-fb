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
    ### Naive and Aware Times
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We decided early on that we would only work with naive times in UTC.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But we still need the ability to transform aware times into naive UTC times, and vice versa.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If no other reason that we will be ingesting datetime data that may contain timezone information.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll come back to a 3rd party library that can help us substantially with this, but for now, let's use plain Python to understand its basic timezone functionality.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When we parsed a `datetime` object from an ISO string, we saw that we could end up with a time zone aware `datetime`:
    """)
    return


@app.cell
def _():
    s = "2020-03-15T13:30:00-07:00"
    return (s,)


@app.cell
def _():
    from datetime import datetime

    return (datetime,)


@app.cell
def _(datetime, s):
    datetime.fromisoformat(s)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, that `datetime` object has a `tzinfo` property that is not `None` - it is a `timezone` object, so it is timezone aware.
    """)
    return


@app.cell
def _(datetime, s):
    dt = datetime.fromisoformat(s)
    return (dt,)


@app.cell
def _(dt):
    dt.tzinfo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we can see, the time zone was expressed as a UTC offset - an offset is nothing more than a duration, and the timezone offset definition is actually expressed using a `timedelta` object.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's look at `timezone` objects.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A Python `timezone` object is nothing more than a `name` associated with a `timedelta` object that represents the UTC offset.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The idea is that if we have an aware datetime with a timezone, we simply add the timezone's `timedelta` object to a naive version of the datetime, and this gives us a naive UTC timestamp.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, if I am located in New York, and we are in DST, our time zone is EDT (as opposed to EST if we are not in DST).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, I could create a timezone named `EDT`, with an offset from UTC of -4 hours:
    """)
    return


@app.cell
def _():
    from datetime import timezone, timedelta

    return timedelta, timezone


@app.cell
def _(timedelta, timezone):
    tz_EDT = timezone(timedelta(hours=-4), 'EDT')
    return (tz_EDT,)


@app.cell
def _(tz_EDT):
    tz_EDT
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `timezone` class also has a UTC timezone pre-defined:
    """)
    return


@app.cell
def _(timezone):
    timezone.utc
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's define another time zone, Central Daylight Time (CDT) this time - it has a -5 hour offset from UTC:
    """)
    return


@app.cell
def _(timedelta, timezone):
    tz_CDT = timezone(timedelta(hours=-5), 'CDT')
    return (tz_CDT,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's start with an aware datetime in EDT:
    """)
    return


@app.cell
def _(datetime, tz_EDT):
    dt_1 = datetime(year=2020, month=5, day=15, hour=22, minute=30, tzinfo=tz_EDT)
    return (dt_1,)


@app.cell
def _(dt_1):
    dt_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We want to "convert" this datetime into the equivalent datetime but in CDT time zone.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can use the `.astimezone()` method that `datetime` objects have:
    """)
    return


@app.cell
def _(dt_1, tz_CDT):
    dt_1.astimezone(tz_CDT)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice how we end up with an aware datetime, but with a CDT time zone - and notice how the new time reflects the time zone change (one hour earlier than EDT).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly, we can convert an aware datetime of any time zone into an aware datetime in UTC:
    """)
    return


@app.cell
def _(dt_1, timezone):
    dt_utc = dt_1.astimezone(timezone.utc)
    return (dt_utc,)


@app.cell
def _(dt_utc):
    dt_utc
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Again notice how the time zone now shows UTC, and the date/time was adjusted accordingly.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So now we are able to convert an aware datetime from one time zone to another.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But now that we have that datetime in UTC, how do we make it naive?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Remember that a datetime is naive if it has no time zone information, i.e. `tzinfo` is `None`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can use the `replace` method on our `dt_utc` object, that creates a new `datetime` object, copying all the values over, except the ones we specify as a replacement.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In this case, we want to copy everything into a new `datetime` except the timezone, which we want to make `None`:
    """)
    return


@app.cell
def _(dt_utc):
    dt_naive = dt_utc.replace(tzinfo=None)
    return (dt_naive,)


@app.cell
def _(dt_naive):
    dt_naive
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So now we've seen how to take an aware datetime with some timezone, and convert it to a naive datetime in UTC - let's recap:
    """)
    return


@app.cell
def _(datetime, timezone):
    s_1 = '2020-05-15T13:30:00-04:00'
    dt_aware = datetime.fromisoformat(s_1)
    dt_utc_1 = dt_aware.astimezone(timezone.utc)
    dt_naive_1 = dt_utc_1.replace(tzinfo=None)
    print(dt_naive_1.isoformat())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we want to do the opposite - convert a naive UTC datetime into an aware datetime in some other time zone. The process is basically the same:
    """)
    return


@app.cell
def _(datetime):
    dt_naive_2 = datetime.fromisoformat('2020-05-15T17:30:00')
    return (dt_naive_2,)


@app.cell
def _(dt_naive_2, timezone):
    dt_aware_1 = dt_naive_2.replace(tzinfo=timezone.utc)
    return (dt_aware_1,)


@app.cell
def _(dt_aware_1):
    dt_aware_1
    return


@app.cell
def _(timedelta, timezone):
    tz_EDT_1 = timezone(timedelta(hours=-4), 'EDT')
    tz_CDT_1 = timezone(timedelta(hours=-5), 'CDT')
    return tz_CDT_1, tz_EDT_1


@app.cell
def _(dt_aware_1, tz_EDT_1):
    dt_aware_1.astimezone(tz_EDT_1)
    return


@app.cell
def _(dt_aware_1, tz_CDT_1):
    dt_aware_1.astimezone(tz_CDT_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One thing in all this, is that we never had to deal with DST - we simply defined our timezone as a UTC offset, and applied the particular time zone - here I used EDT and CDT (instead of EST and CST) because I **knew** the particular date we were looking at was during DST. In general, you don't know that though - and this adds another level of complexity - when converting a UTC datetime to Eastern, should you pick EST or EDT? What about all the other timezones in the world? Not everyone changes over DST on the same day - and some don't even change, ever (like Phoenix Arizona for example). Not only that, but DST changes are not always constant - they can, and have, varied historically, for the same time zone - so a history needs to be maintained, and of course things will change in the future.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dealing with timezones is bad enough, but DST is 10x worse!

    Anyone interested in starting a worldwide petition to drop daylight savings times??!! :-)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For that reason, there is a standarized database that captures all this information - time zone names, UTC offsets, DST rules, etc, called the Olson Database (named after the original creator) - also known as the IANA timezone database: https://en.wikipedia.org/wiki/Tz_database
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll look at some 3rd party libraries later in this course that will simplify our life a lot!
    """)
    return


if __name__ == "__main__":
    app.run()
