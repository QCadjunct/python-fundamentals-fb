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
    Write some code that generates a file containing containing rows containing the following data:

    ```
    i, fibonacci_i, factorial_i, gcd_fibonacci_i_factorial_i
    ```

    where:
    - `i`: integer values from `0` to `100`
    - `fibonacci_i`: the `i`th Fibonacci number
    - `factorial_i`: the factorial of `i` (`i!`)
    - `gcd_fib_i_fact_i`: the greatest common denominator of the `i`th Fibonacci number and `i!`

    Hint: look at the `math.factorial` and `math.gcd` functions in the Python docs

    Also make sure to include a header row in your file.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, the first few rows in your file should contain this data:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```
    i,fib,fact,gcd
    0,1,1,1
    1,1,1,1
    2,2,2,2
    3,3,6,3
    4,5,24,1
    5,8,120,8
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
    Let's start by writing or importing the function's we'll need to calculate
    - the Fibonacci numbers (I'll use the sequence `1, 1, 2, 3, 5, ...` where the first number will be indexed as `0`. Also, we'll use the `lru_cache` decorator to speed up our recursive algorithm.
    - the factorial of `i` (using the `math.factorial` function)
    - the greatest common denominator (using the `math.gcd` function)
    """)
    return


@app.cell
def _():
    from functools import lru_cache
    from math import factorial, gcd

    return factorial, gcd, lru_cache


@app.cell
def _(lru_cache):
    @lru_cache
    def fib(i):
        if i in {0, 1}:
            return 1
        else:
            return fib(i - 1) + fib(i - 2)

    return (fib,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's call the `fib` function and make sure it outputs the expected results:
    """)
    return


@app.cell
def _(fib):
    [fib(_i) for _i in range(10)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could then generate the data we'll need to eventually write to a file as follows:
    """)
    return


@app.cell
def _(factorial, fib, gcd):
    _n = 10  # later we can change this to 100
    for _i in range(_n):
        print(_i, fib(_i), factorial(_i), gcd(fib(_i), factorial(_i)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, we actually need this data as a single string that can be written to a file. To do this, we can `join` the string representations of each number:
    """)
    return


@app.cell
def _(factorial, fib, gcd):
    _n = 10  # later we can change this to 100
    for _i in range(_n):
        data = [_i, fib(_i), factorial(_i), gcd(fib(_i), factorial(_i))]
        _row = ','.join([str(data[0]), str(data[1]), str(data[2]), str(data[3])])
        print(_row)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This works, but applying the `str` function to each element of `data` individually is not very elegant.

    Instead we can use the `map` function:
    """)
    return


@app.cell
def _(factorial, fib, gcd):
    _n = 10
    for _i in range(_n):
        data_1 = [_i, fib(_i), factorial(_i), gcd(fib(_i), factorial(_i))]
        _row = ','.join(map(str, data_1))
        print(_row)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can now use this to write data to a file.
    """)
    return


@app.cell
def _(factorial, fib, gcd):
    file_name = 'data.csv'
    headers = ('i', 'fib', 'fact', 'gcd')
    _n = 100
    with open(file_name, 'w') as _f:
        _f.write(','.join(headers))
        _f.write('\n')
        for _i in range(_n):
            data_2 = [_i, fib(_i), factorial(_i), gcd(fib(_i), factorial(_i))]
            _row = ','.join(map(str, data_2))
            _f.write(_row)
            _f.write('\n')
    return (file_name,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Go ahead and open that file in some text editor and check its content.
    """)
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
    Using the file you just generated, write three functions:
    - `fib`
    - `fact`
    - `gcd_fib_fact`

    that perform the same calculations as our original `fib` function, the `math` module's `factorial` and the `gcd` of the corresponding fibonacci and factorial numbers, but uses the data that was saved in the file as a cache/lookup mechanism - i.e. just use the numbers in the file if they are available, otherwise make the calculation.
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
    The easiest approach will probably be to load up the data form the file and store it some lists that we can easily lookup.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could do this inside each function we are going to create, but here I'm going to load up the data into our notebook, and pass the relevant data to each function - this avoids re-loading the data form file each time the function is called.
    """)
    return


@app.cell
def _(file_name):
    with open(file_name) as _f:
        next(_f)  # skip header row
        for _row in _f:
            print(_row)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So a few things:
    - we should `strip` each `row`
    - we'll need to split each row (on `,`), and cast each of the strings to integers
    """)
    return


@app.cell
def _(file_name):
    with open(file_name) as _f:
        next(_f)  # skip header row
        for _row in _f:
            print(_row.strip())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then split on the comma:
    """)
    return


@app.cell
def _(file_name):
    with open(file_name) as _f:
        next(_f)  # skip header row
        for _row in _f:
            print(_row.strip().split(','))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And finally make each item an integer - we'll use the `map` function again:
    """)
    return


@app.cell
def _(file_name):
    with open(file_name) as _f:
        next(_f)  # skip header row
        for _row in _f:
            print(list(map(int, _row.strip().split(','))))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, let's store those values into a list (of lists).

    We could do it this way:
    """)
    return


@app.cell
def _(file_name):
    data_3 = []
    with open(file_name) as _f:
        next(_f)
        for _row in _f:
            data_3.append(list(map(int, _row.strip().split(','))))
    print(data_3[:10])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But, we can also just use a comprehension:
    """)
    return


@app.cell
def _(file_name):
    with open(file_name) as _f:
        next(_f)
        data_4 = [list(map(int, _row.strip().split(','))) for _row in _f]
    print(data_4[:10])
    return (data_4,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now that we have our pre-calculated data, let's create individual sequences for Fibonacci, factorial and gcd numbers:
    """)
    return


@app.cell
def _(data_4):
    fib_stored = [_row[1] for _row in data_4]
    fact_stored = [_row[2] for _row in data_4]
    gcd_stored = [_row[3] for _row in data_4]
    return fact_stored, fib_stored, gcd_stored


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, we can write our functions, starting with `fact`:
    """)
    return


@app.cell
def _(fact_stored, factorial):
    def fact(i):
        if i < len(fact_stored):
            print('looking up fact in cache...')
            return fact_stored[i]
        else:
            return factorial(i)

    return (fact,)


@app.cell
def _(fact):
    fact(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can do something similar for Fibonacci numbers:
    """)
    return


@app.cell
def _(fib, fib_stored):
    def fib_1(i):
        if i < len(fib_stored):
            print('looking up fib in cache...')
            return fib_stored[i]
        elif i in {0, 1}:
            return 1
        else:
            return fib(i - 1) + fib(i - 2)

    return (fib_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before we run this, let's make sure we apply an `lru_cache` to it as well:
    """)
    return


@app.cell
def _(fib_1, fib_stored, lru_cache):
    @lru_cache
    def fib_2(i):
        if i < len(fib_stored):
            print('looking up in cache...')
            return fib_stored[i]
        elif i in {0, 1}:
            return 1
        else:
            return fib_1(i - 1) + fib_1(i - 2)

    return (fib_2,)


@app.cell
def _(fib_2):
    fib_2(10)
    return


@app.cell
def _(fib_2):
    fib_2(101)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You'll notice that to calculate `fib(101)` required calculating `fib(100) + fib(99)`, which were both in our loaded data - hence why we see two `looking up fib in cache...` prints in our output.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, we can process `gcd` in the same way:
    """)
    return


@app.cell
def _(fact, fib_2, gcd, gcd_stored):
    def gcd_fib_fact(i):
        if i < len(gcd_stored):
            print('Looking up gcd in cache...')
            return gcd_stored[i]
        else:
            return gcd(fact(i), fib_2(i))

    return (gcd_fib_fact,)


@app.cell
def _(gcd_fib_fact):
    gcd_fib_fact(11)
    return


@app.cell
def _(gcd_fib_fact):
    gcd_fib_fact(101)
    return


if __name__ == "__main__":
    app.run()
