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
    ### Writing Text Files
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So far we've seen how to open and close text files, using a context manager, and how to read data from these files.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's see how we can also write to files, again with or without a context manager.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Remember the modes we have for writing files:
    - 'w' : create file if it does not exist, or overwrite if it does
    - 'a' : create file if it does not exist, append writes to end of file if it does
    """)
    return


@app.cell
def _():
    f = open('test.csv', 'w')
    return (f,)


@app.cell
def _(f):
    f.write('abc')
    return


@app.cell
def _(f):
    f.write('123456')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The return value is the number of characters written to the file.
    """)
    return


@app.cell
def _(f):
    f.close()
    return


@app.cell
def _():
    with open('test.csv', 'r') as f_1:
        print(f_1.readlines())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we can see, the consecutive writes did not create two lines in the text file, it just keeps writing what we tell it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To create a newline, we'll have to specifically write a `\n` character:
    """)
    return


@app.cell
def _():
    with open('test.csv', 'w') as f_2:
        f_2.write('abc\n')
        f_2.write('123456\n')
    return


@app.cell
def _():
    with open('test.csv', 'r') as f_3:
        print(f_3.readlines())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we have a list of strings we want to write, we can use the `writelines` method too:
    """)
    return


@app.cell
def _():
    data = ['line 1', 'line 2', 'line 3']
    return (data,)


@app.cell
def _(data):
    with open('test.csv', 'w') as f_4:
        f_4.writelines(data)
    return


@app.cell
def _():
    with open('test.csv', 'r') as f_5:
        print(f_5.readlines())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, we still only have one line - so we need to provide the newline characters ourselves as well:
    """)
    return


@app.cell
def _():
    data_n = ['line 1', '\n', 'line 2', '\n', 'line 3', '\n']
    return (data_n,)


@app.cell
def _(data_n):
    with open('test.csv', 'w') as f_6:
        f_6.writelines(data_n)
    return


@app.cell
def _():
    with open('test.csv', 'r') as f_7:
        print(f_7.readlines())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could also have used the original list of strings, and joined them:
    """)
    return


@app.cell
def _(data):
    with open('test.csv', 'w') as f_8:
        f_8.write('\n'.join(data))
    return


@app.cell
def _():
    with open('test.csv', 'r') as f_9:
        print(f_9.readlines())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's also take a look at what happens if the code in the context manager enounters an unhandled exception:
    """)
    return


@app.cell
def _():
    with open('test.csv', 'r') as f_10:
        raise ValueError('bogus')
    return (f_10,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, we have an unhandled exception, but what happend to the file we opened?
    """)
    return


@app.cell
def _(f_10):
    f_10.closed
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The context manager closed the file for us. That's what's nice about a context manager, it cleans up after it exits, even if the exit was caused by an unhandled exception.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's look at the `a` mode for writing files.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We know we already have a file called `test.csv`:
    """)
    return


@app.cell
def _():
    with open('test.csv') as f_11:
        for _line in f_11:
            print(_line.strip())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's append some data to that file:
    """)
    return


@app.cell
def _():
    with open('test.csv', 'a') as f_12:
        f_12.write('line4\n')
        f_12.write('line5\n')
    return


@app.cell
def _():
    with open('test.csv') as f_13:
        for _line in f_13:
            print(_line.strip())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ah, our original file did not end with a newline, so the append just continued writing to the same line.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is one reason why we usually include the `\n` character, even for the last line in our text file.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What happens if we try to append to a non-existent file:
    """)
    return


@app.cell
def _():
    with open('does_not_exist.txt', 'a') as f_14:
        f_14.write('Line 1')
    return


@app.cell
def _():
    with open('does_not_exist.txt') as f_15:
        print(f_15.readlines())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, the file is create automatically for us.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's work on a practical example.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Recall the file `DEXUSEU.csv` we used previously. This same file is available course downloads - pleased make sure you save this file in the same directory as your Jupyter notebook (if not, you'll have to adjust the path when you specify the file to open).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's recall what that file looks like:
    """)
    return


@app.cell
def _():
    source_file = 'DEXUSEU.csv'
    with open(source_file) as f_16:
        for _ in range(5):
            print(next(f_16).strip())
    return (source_file,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our goal is to create a new csv file that will contain the following data (including the header names):
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```
    YEAR,MONTH,DAY,DEXUSEU
    2015,4,3,1.0990
    2015,4,6,1.1008
    etc
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, we will have to read from one file, modify the data as needed, and write it out to another file.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll look at two different approaches to do this.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The first approach will be to read the entire data file into memory, process the data, and then write everything out to the target file.
    """)
    return


@app.cell
def _():
    target_file = 'output.csv'
    return (target_file,)


@app.cell
def _(source_file):
    with open(source_file) as f_17:
        data_1 = f_17.readlines()
    return (data_1,)


@app.cell
def _(data_1):
    data_1[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First we should remove the header row:
    """)
    return


@app.cell
def _(data_1):
    del data_1[0]
    return


@app.cell
def _(data_1):
    data_1[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next we should strip each line in the data from the trailing `\n` character:
    """)
    return


@app.cell
def _(data_1):
    data_2 = [_line.strip() for _line in data_1]
    return (data_2,)


@app.cell
def _(data_2):
    data_2[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next we should split the date and exchange rate into a tuple containing the date and exchange rate:
    """)
    return


@app.cell
def _(data_2):
    data_3 = [_line.split(',') for _line in data_2]
    return (data_3,)


@app.cell
def _(data_3):
    data_3[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next we need to split the date strings into year, month and day.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's write a small utility function to do this:
    """)
    return


@app.function
def split_date(dt_str):
    return dt_str[:4], dt_str[5:7], dt_str[8:]


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's make sure it works as intended:
    """)
    return


@app.cell
def _():
    split_date('2015-04-03')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To make our life simpler and see all the code we wrote, let's write a function that takes a single (unprocessed) row from the source file and transforms it into something we can use to write to our target file:
    """)
    return


@app.function
def transform_row_for_output(row):
    row = row.strip()  # remove trailing \n
    dt_str, rate = row.split(',')  # split fields on ,
    year, month, day = split_date(dt_str)  # split date string into Y M D
    result = ','.join([year, month, day, rate])
    result = result + '\n'  # join all the fields into a , separated string
    return result  # finally add the newline character


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's try it out for a single row and make sure it's doing what we want:
    """)
    return


@app.cell
def _():
    row = '2015-04-03,1.0990\n'
    return (row,)


@app.cell
def _(row):
    transform_row_for_output(row)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Looking good, we could even try to clean up those leading zeroes in the month and day:
    """)
    return


@app.function
def transform_row_for_output_1(row):
    row = row.strip()  # remove trailing \n
    dt_str, rate = row.split(',')  # split fields on ,
    year, month, day = split_date(dt_str)  # split date string into Y M D
    month = str(int(month))
    day = str(int(day))  # clean up leading 0
    result = ','.join([year, month, day, rate])
    result = result + '\n'
    return result  # join all the fields into a , separated string  # finally add the newline character


@app.cell
def _(row):
    transform_row_for_output_1(row)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But what about data that has a missing exchange rate?
    """)
    return


@app.cell
def _():
    row_1 = '2015-04-03,.\n'
    return (row_1,)


@app.cell
def _(row_1):
    transform_row_for_output_1(row_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This works, but we may not want it in our output file. We could have the transformation function return `None` in those cases, and later we can skip writing `None` return values.
    """)
    return


@app.function
def transform_row_for_output_2(row):
    row = row.strip()  # remove trailing \n
    dt_str, rate = row.split(',')  # split fields on ,
    try:
        float(rate)
    except ValueError:
        return None
    year, month, day = split_date(dt_str)  # not a float, so return None
    month = str(int(month))
    day = str(int(day))
    result = ','.join([year, month, day, rate])  # split date string into Y M D
    result = result + '\n'
    return result  # clean up leading 0  # join all the fields into a , separated string  # finally add the newline character


@app.cell
def _():
    row_2 = '2015-04-03,.\n'
    print(transform_row_for_output_2(row_2))
    return


@app.cell
def _():
    row_3 = '2015-04-03,1.0990\n'
    print(transform_row_for_output_2(row_3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But this approach means we'll need to test each transformed row to decide whether to write it or not.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    How about returning an empty string - we can write an empty string to a file and nothing will happen - that way we can just write all transformed rows without checking if the row is `None` or not.
    """)
    return


@app.function
def transform_row_for_output_3(row):
    row = row.strip()  # remove trailing \n
    dt_str, rate = row.split(',')  # split fields on ,
    try:
        float(rate)
    except ValueError:
        return ''
    year, month, day = split_date(dt_str)  # not a float, so return empty string (no output)
    month = str(int(month))
    day = str(int(day))
    result = ','.join([year, month, day, rate])  # split date string into Y M D
    result = result + '\n'
    return result  # clean up leading 0  # join all the fields into a , separated string  # finally add the newline character


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    OK, now let's go ahead and write our code to transform the source file and write it out to the target file.
    """)
    return


@app.cell
def _(source_file):
    with open(source_file) as f_18:
        data_4 = f_18.readlines()
    return (data_4,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Delete first row (headers) from data:
    """)
    return


@app.cell
def _(data_4):
    del data_4[0]
    return


@app.cell
def _(data_4, target_file):
    with open(target_file, 'w') as f_19:
        f_19.write('YEAR,MONTH,DAY,EXCH\n')
        for row_4 in data_4:
            f_19.write(transform_row_for_output_3(row_4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's read back some our file to see what we actually wrote (you could also just open it in a text editor):
    """)
    return


@app.cell
def _(target_file):
    with open(target_file) as f_20:
        for row_5 in f_20:
            print(row_5.strip())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's actually write a function to do all those steps for us:
    """)
    return


@app.function
def transform_file_batch(source_file, target_file):
    with open(source_file) as f:
        data = f.readlines()
    del data[0]
    with open(target_file, 'w') as f:
        f.write('YEAR,MONTH,DAY,EXCH\n')
        for row in data:
            f.write(transform_row_for_output_3(row))


@app.cell
def _(source_file, target_file):
    transform_file_batch(source_file, target_file)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So this approach works just fine, but it has one real disadvantage: we are reading the entire file into memory (the `data` list), and then writing it back out.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But in reality, we don't need to load the entire file to process a single row - a better approach would be to read the source file one line at a time, and write out to the target file one line at a time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Fortunately we have all the building blocks to do this very easily:
    """)
    return


@app.function
def transform_file(source_file, target_file):
    with open(source_file) as source:
        with open(target_file, 'w') as target:
            next(source)  # need to skip first row in source file (headers)
            target.write('YEAR,MONTH,DAY,EXCH\n')
            for row in source:
                target.write(transform_row_for_output_3(row))  # write out header file


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's run it:
    """)
    return


@app.cell
def _(source_file, target_file):
    transform_file(source_file, target_file)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And let's check the output results:
    """)
    return


@app.cell
def _(target_file):
    with open(target_file) as f_21:
        for row_6 in f_21:
            print(row_6.strip())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In future sections of this course we'll cover how to handle CSV files properly. Here we did not deal with quotes used to enclose text fields, or any of the other issues we may encounter when reading or writing CSV files. But this gives us a solid foundation on reading and writing text files in case we need to special handle certain files (maybe badly CSV formatted data - that happens!!), or some other proprietary data format)
    """)
    return


if __name__ == "__main__":
    app.run()
