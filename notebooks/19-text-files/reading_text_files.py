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
    ### Reading Text Files
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In order to read a text file we have to **open** the file.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    After a file has been opened, we can read and/or write to that file.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When we are done using the file, we need to remember to **close** the file - this releases the file, or more generically stated, releases the **resource** (a file in this case).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It is important to remember to close files - although the files will close automatically when your program terminates, there are other issues that can come up if you don't close your files explicitly.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Apart from a limit to the number of files that can be opened at the same time, one main issue is that often writes to files are not immediately written out to disk - instead, things are hanging around until the file is closed. Far better to explicitly decide when you want that to happen, rather than hoping Python does it for you at some point... maybe... if nothing crashes in the meantime... so maybe never...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You get the idea :-)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we have to open and close files.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When we open a file we specify our intentions - do we want to read-only from the file, write to the file (by replacing an existing file, or by appending to the file), or do both.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    These characteristics are specified using some string characters:

    1. `r` - read-only
    2. `w` - write-only, replace existing file (if any)
    3. `a` - append (write-only) - appends to existing file (if any)
    4. `r+` - both read and write

    Be careful with using both read and write operations on a file at the same time - it can get quite tricky...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's look at opening, reading and closing files.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There is a file `DEXUSEU.csv` that is available in the course materials. Please make sure you copy that file to the same location as the Jupyter notebook you are using (if not, you'll have to tweak the code we are writing here to use the correct path to the file).

    In this video, I'm going to assume that the file is located in the same directory as the Jupyter notebook.
    """)
    return


@app.cell
def _():
    file_name = 'DEXUSEU.csv'
    return (file_name,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First we are going to open the file for read-only:
    """)
    return


@app.cell
def _(file_name):
    file = open(file_name, 'r')
    return (file,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now this file is open, and we can look at some of the properties of the file:
    """)
    return


@app.cell
def _(file):
    file.name
    return


@app.cell
def _(file):
    file.readable()
    return


@app.cell
def _(file):
    file.writable()
    return


@app.cell
def _(file):
    file.mode
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also find out if the file has been closed:
    """)
    return


@app.cell
def _(file):
    file.closed
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we can close the file:
    """)
    return


@app.cell
def _(file):
    file.close()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can see that the file is closed:
    """)
    return


@app.cell
def _(file):
    file.closed
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's try reading some data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can read data from a text file in many different ways, the two most common being the entire file at a time, or line by line.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If you are dealing with massive data files, reading the entire file into memory and then processing it might not always be the best approach - always try to avoid calculating or creating objects until absolutely necessary (think of lazy iterators).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, let's first look at reading the entire file at once:
    """)
    return


@app.cell
def _(file_name):
    f = open(file_name)  # r is the default
    data = f.readlines()
    f.close()
    return (data,)


@app.cell
def _(data):
    data
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, `readlines()` will create a list of strings, one list item for each row in the file.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we do not want to read the entire file at once, and we are in a situation where we can just do what we need by reading the file one line at a time, we can do so by **iterating** over the file.

    In other words, the object returned by `open` is an iterable:
    """)
    return


@app.cell
def _(file_name):
    f_1 = open(file_name)
    for _line in f_1:
        print(_line)
    return (f_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Watch out, once we've read all the lines, we're at the bottom of the file, and there's nothing more to iterate over.
    """)
    return


@app.cell
def _(f_1):
    for _line in f_1:
        print(_line)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can move backwards in the file, by specifying a location to move to, but I'm not going to cover that in this course.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we should not forget to close the file:
    """)
    return


@app.cell
def _(f_1):
    f_1.close()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Also want to point out that the result of `open()` is an iterator - we can call `next()` on it, or iterate over it (as we just saw). That behavior is no different than other iterators we've worked with.
    """)
    return


@app.cell
def _(file_name):
    f_2 = open(file_name)
    print(next(f_2))
    print(next(f_2))
    print(next(f_2))
    f_2.close()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our current pattern has been:

    1. open file
    2. read data from file and perform some operations
    3. close file
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The problem with that approach is that if something goes wrong in step 2, we may never close the file explicitly.

    So maybe we would want to do this:
    """)
    return


@app.cell
def _(file_name):
    f_3 = open(file_name)
    try:
        for _row in f_3:
            print(_row)
            raise ValueError('forcing an exception...')
    finally:
        print('closing file...')
        f_3.close()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, even though we had an exception, we still closed the file by using the `finally` block.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There is a much cleaner way of doing this - using something called a **context manager**.
    """)
    return


@app.cell
def _(file_name):
    with open(file_name) as f_4:
        print(f_4.closed)  # while in this block, f remains open
    print(f_4.closed)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A context is **entered** using the `with` statement. Once the context is **exited**, some code that cleans up the context is executed (in this case, that would be closing the file, but other context managers may do other things upon entry/exit).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Using a context manager means we never have to remember to close the file ourselves, it will be done automatically as soon as the context is exited - whether normally or because of an exception does not matter.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's turn back to our sample data file, and see if we can parse the data out into a list of tuples.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First we observed that the first row in the file consists of headers - so we'll need to handle the first row differently from the others.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The other thing to observe is that some of the expected numerical data looks odd:
    """)
    return


@app.cell
def _(file_name):
    with open(file_name) as f_5:
        for _line in f_5:
            print(_line)
    return


@app.cell
def _(file_name):
    with open(file_name) as f_6:
        print(f_6.readlines())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So we can split the data on `,`, and we'll also strip each line to remove the trailing `\n`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We also have to deal with the numerical data containing `.` - what happens if we try to convert that to a float?
    """)
    return


@app.cell
def _():
    float('.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We get a `ValueError`, whereas this works just fine:
    """)
    return


@app.cell
def _():
    float('3.1415')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our goal will be to create a list of tuples of 2 elements each - date string as first element, and exchange rate as a float in the second position.
    """)
    return


@app.cell
def _(file_name):
    with open(file_name) as f_7:
        _headers = next(f_7)
        for _row in f_7:
            _row = _row.strip()
            _date, _value_str = _row.split(',')
            print(_date, _value_str)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ok, almost there:
    """)
    return


@app.cell
def _(file_name):
    data_1 = []
    with open(file_name) as f_8:
        _headers = next(f_8)
        for _row in f_8:
            _row = _row.strip()
            _date, _value_str = _row.split(',')
            try:
                value = float(_value_str)
                data_1.append((_date, value))
            except ValueError:
                pass
    print(data_1)
    return


if __name__ == "__main__":
    app.run()
