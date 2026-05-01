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
    Given the following list:
    """)
    return


@app.cell
def _():
    l = [10, 'abc', 3.14, True]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write code that prints out the index number and value at that index for every element of `l`.
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
    We saw in this section how generator expressions can be more efficient, not only in terms os memory, but also in terms of computation time when not all values in the generator are iterated.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Create a generator expression that when iterated over will produce the integers from `1` to `10_000` raised to the power of `1`, `2`, `3`, etc.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So this generator should produce these results:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```
    1**1, 2**2, 3**3, 4**4, ...
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Once you have created a generator expression to do this, time your results to create the generator and iterate through the first 5 elements of the generator.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then, do the same thing, but using a list comprehension instead of a generator expression.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hint: you should use the `perf_counter` apprioach we have seen a few times in previous lectures:

    ```
    from time import perf_counter

    start = perf_counter()
    # your code goes here
    end = perf_counter()
    print('elapsed:', end - start)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To make timings more accurate, you should time a loop that repeats your code at least 10 times.
    """)
    return


if __name__ == "__main__":
    app.run()
