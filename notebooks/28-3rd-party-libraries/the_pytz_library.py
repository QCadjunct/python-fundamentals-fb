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
    ### The pytz Library
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    https://pythonhosted.org/pytz/
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This library basically allows us to deal with timezones in a simpler way, using named time zones, with automatic DST selection/detection.

    It uses the Olson timezone database, and makes our life much much easier!
    """)
    return


@app.cell
def _():
    import pytz
    from datetime import datetime, timezone

    return datetime, pytz, timezone


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can list all defined (named) timezones available in `pytz`:
    """)
    return


@app.cell
def _(pytz):
    for tz in pytz.all_timezones:
        print(tz)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    These timezones are just strings (names), but they can be used to get the corresponding timezone object (`DstTzInfo`) implemented by `pytz` (it is not the same as the `tzinfo` object implemented by Python), this type (class) is specific to `pytz`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example:
    """)
    return


@app.cell
def _(pytz):
    tz_chicago = pytz.timezone('America/Chicago')
    return (tz_chicago,)


@app.cell
def _(tz_chicago):
    tz_chicago
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can even get the `UTC` "timezone" this way:
    """)
    return


@app.cell
def _(pytz):
    tz_utc = pytz.timezone('UTC')
    return (tz_utc,)


@app.cell
def _(tz_utc):
    tz_utc
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see this object is a bit different - remember that UTC is technically not a timezone, and does not observe DST - and in `pytz` it is its own special data type.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In fact we can get that object directly from `pytz`:
    """)
    return


@app.cell
def _(pytz):
    pytz.UTC
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given a `pytz` timezone we can use the `zone` attribute to get the (string) name of the timezone:
    """)
    return


@app.cell
def _(tz_utc):
    tz_utc.zone
    return


@app.cell
def _(tz_chicago):
    tz_chicago.zone
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This `DstTzInfo` type is compatible with Python's native `datetime` and can be used instead of the standard `tzinfo` type:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start with a naive datetime:
    """)
    return


@app.cell
def _(datetime):
    dt_naive = datetime(2020, 5, 15, 10, 0, 0)
    return (dt_naive,)


@app.cell
def _(dt_naive):
    dt_naive
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can attach the `tz_chicago` timezone to this naive datetime by using the timezone's `localize` method:
    """)
    return


@app.cell
def _(dt_naive, tz_chicago):
    dt_chicago = tz_chicago.localize(dt_naive)
    return (dt_chicago,)


@app.cell
def _(dt_chicago):
    dt_chicago
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice how the timezone was automatically set to CDT - i.e. Central **daylight** time!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we had chosen a date/time that is not under daylight savings:
    """)
    return


@app.cell
def _(datetime, tz_chicago):
    tz_chicago.localize(datetime(2019, 12, 31, 10, 0, 0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice here how `pytz` automatically recognized the timezone as being Central **standard** time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: very important to realize here that the timezone is attached to the datetime - there is no timezone conversion that takes place.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Once we have an aware datetime, we can easily use `pytz` to convert it to any other timezone:
    """)
    return


@app.cell
def _(pytz):
    tz_melbourne = pytz.timezone('Australia/Melbourne')
    return (tz_melbourne,)


@app.cell
def _(dt_chicago):
    dt_chicago
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `pytz` timezones are compatible with Python's own `tzinfo` so we can use `datetime`'s `astimezone()` method using `pytz` timezone objects:
    """)
    return


@app.cell
def _(dt_chicago, tz_melbourne):
    dt_chicago.astimezone(tz_melbourne)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    (Notice how pytz was able to correctly handle the DST/STD times between Chicago and Melbourne - while Chicago was under DST, Melbourne was not)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And of course we can use the same technique to convert an aware datetime to UTC:
    """)
    return


@app.cell
def _(dt_chicago, pytz):
    dt_chicago.astimezone(pytz.UTC)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could start with a datetime in utc:
    """)
    return


@app.cell
def _(datetime):
    datetime.utcnow()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But before we can convert this to another timezone, we need to make it aware.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could just use the `replace` method on the `datetime` instance:
    """)
    return


@app.cell
def _(datetime, pytz):
    datetime.utcnow().replace(tzinfo=pytz.UTC)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could also use use Python's UTC timezone:
    """)
    return


@app.cell
def _(datetime, timezone):
    datetime.utcnow().replace(tzinfo=timezone.utc)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or we can use the `localize` method from `pytz` time zone objects:
    """)
    return


@app.cell
def _(datetime, pytz):
    pytz.utc.localize(datetime.utcnow())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since we are dealing with UTC, there is no DST to worry about, hence using either the `datetime`'s `replace` method or `pytz`'s `localize` method will work just fine.
    """)
    return


@app.cell
def _(datetime, pytz):
    now_utc = pytz.utc.localize(datetime.utcnow())
    return (now_utc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And now we can convert this to any other timezone:
    """)
    return


@app.cell
def _(now_utc, tz_melbourne):
    now_utc.astimezone(tz_melbourne)
    return


@app.cell
def _(now_utc, tz_chicago):
    now_utc.astimezone(tz_chicago)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the special case where we are converting a UTC aware datetime to another timezone, we can use a slightly more efficient method in `pytz`, the `fromutc` available in `pytz` time zone objects:
    """)
    return


@app.cell
def _(datetime, tz_chicago):
    tz_chicago.fromutc(datetime.utcnow())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This saves us having to localize the naive datetime first.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, this library is useful for dealing with timezones, DST and conversions between any timezones as well as UTC.
    """)
    return


if __name__ == "__main__":
    app.run()
