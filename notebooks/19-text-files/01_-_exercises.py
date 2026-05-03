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
    ### Exercises
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


if __name__ == "__main__":
    app.run()
