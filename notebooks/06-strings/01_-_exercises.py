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
    Given this string of comma separated characters, create three new variables containing the unicode codepoint (in hex), uppercase and lower case versions of each character (also comma delimited).

    For example, if the string was `'a, b, c'` you should generate three lists that look like:
    * `['0x61', '0x62', '0x63']`
    * `['a', 'b', 'c']`
    * `['A', 'B', 'C']`

    [You should use the `split()` and `strip()` functions, amongst others, to help you solve this.]
    """)
    return


@app.cell
def _():
    s = 'Π, ύ, θ, ω, ν'
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
    Using two types of string interpolation, and given the variable `a` that contains an integer, print out the following string for `a`:

    `The number ...value of a... is (or is not) even`

    For example, if `a` is `42`, the your code should print:

    `'The number 42 is even'`

    But if `a` is `31`, then the **same** code should print:

    `'The number 31 is not even'`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 3
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You are given two variables `a` and `b` (with `b` non-zero), and you need to generate a string that reads something like this:

    ```
    'a / b = (result)'
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But you want your string to be nicely formatted for display purposes, so you want to limit displaying possible digits after the decimal point in all your values to 4 digits.
    """)
    return


if __name__ == "__main__":
    app.run()
