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
    ### Reading CSV Files
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    https://docs.python.org/3/library/csv.html
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We often have to ingest data from CSV files.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    CSV data is essentially a representation of tabular data - rows (records) and columns (fields).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Earlier in this course, we saw how we could open a text file for reading, and use `split`, `srip` and a few other techniques to "parse" data from a file.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The problem is that the CSV format can get a little more complicated than the sample data we looked at. That data file was a valid CSV format, but there are variations that we need to account for.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Basically there is not a common standard for CSV formats.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In general there are a few things common to all CSV formats:

    1. the data is provided as a plain text file
    2. each row in the file is a single record
    3. fields are separated by some delimiter (usually a comma, but does not have to be)
    4. every record has the same sequence of fields
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In addition the following may apply:

    1. text fields may be delimited with some characters (usually single or double quotes), especially if they happen to contain the same character used as a field separator.
    2. the first row of the file may contain the field names
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see though, the basic premise is that:
    1. each row is a record
    2. first record may contain the field names
    3. each row (ending with a `\n` or `\r\n`) represents a single record
    4. fields can be separated by an arbitrary character or set of characters (but it is consistent for the entire file)
    5. text fields may themselves be delimited by some arbitrary delimiter (usually single or double quotes)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that we din't actually have to specify `delimiter=','` and `quotechar='"'` since those are the default settings.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You may have heard of tab separated files (TSV) - these are like CSV files, except that the field separator is a tab character (`\t`) instead of a comma (`,`).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here is an example of a slightly more complex CSV format:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```
    First Name,Last Name,DOB,Sketches
    John,Cleese,10/27/39,"The Cheese Shop, Ministry of Silly Walks, It's the Arts"
    Eric,Idle,3/29/43,"The Cheese Shop, Nudge Nudge, "\"Spam\"\"\"
    Peter,O'Toole,8/2/32,Lawrence of Arabia
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice that text fields are sometimes surrounded by quotes, and sometimes not.

    These delimiters are needed because the text fields happenb to contain commas (`,`) which are alsu used as field separators.

    Then notice that the word `"Spam"` in row 3, uses doubled double quotes - that's because the text field itself requires double quote delimiters because it contains commas - so the standard approach to embedding double quotes inside a string delimited by double quotes is to double them up.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same can be done in Python (although generally we just try to use different delimiters like single quotes if our string literal is going to contain double quotes, and vice versa - but that's not always possible, and we can do this by "escaping" the character:
    """)
    return


@app.cell
def _():
    s = "Doyle's first Holmes story was \"A Study in Scarlet\" published in 1887."
    return (s,)


@app.cell
def _(s):
    s
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This means that if we were to try and process such a CSV file ourselves it would be relatively difficult:
    """)
    return


@app.cell
def _():
    with open('actors.csv') as _f:
        for _row in _f:
            print(_row)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we try our naive approach of splitting on commas, we would get this:
    """)
    return


@app.cell
def _():
    with open('actors.csv') as _f:
        for _row in _f:
            _row = _row.strip()
            fields = _row.split(',')
            print(fields)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Fortunately, Python's standard library include a module for handling CSV files - and it is provides for a lot of different functionality. There are also 3rd party libraries that can do this, and provide even more functionality, such as Pandas, which we'll study towards the end of this course.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's import the `csv` module first:
    """)
    return


@app.cell
def _():
    import csv

    return (csv,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The primary function to read a CSV file, is the `reader` function, that returns an **iterator** that can be used to iterate over the rows (records) one by one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In general, we need to give this `reader`:
    - an open file to use
    - what `delimiter` is used for field separators
    - what character (`quotechar`) is used for delimiting text fields when necessary
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we could use it this way:
    """)
    return


@app.cell
def _(csv):
    with open('actors.csv') as _f:
        reader = csv.reader(_f, delimiter=',', quotechar='"')
        for _row in reader:
            print(_row)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, wasn't that easy!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are actually a lot more parameters that `reader` supports, such as:
    - `skipinitialspace` (in case a space is added after the delimiter - if `True` (the default), it just ignores it)
    - `doublequote` and `escapechar` - can control how `quotechar` characters inside a field should themselves be quoted or escaped
        - we'll come back to those in the context of writing CSV files
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Basically different variants of CSV files will require possibly different settings.
    """)
    return


if __name__ == "__main__":
    app.run()
