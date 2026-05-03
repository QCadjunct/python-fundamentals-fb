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
    Write a function that takes a variable number of arguments (with a minimum of one), and returns the average of these numbers.
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
    Write a function that returns a string based on two input arguments:
    - a character or string to be repeated
    - the number of times the string should be repeated
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The function should be such that the number of repetitions defaults to `10` if it is not passed by the caller, and the default character to be repeated should be a negative sign (`-`).

    Call your function `separator`.

    Use a keyword-only argument for the string argument.
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
    Write a lambda function that returns the number of unique elements in an iterable. This could be the number of unique characters in a string, or the number of unique elements in a list, tuple, etc.

    If the iterable received by the lambda function is empty, then it should return `0`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 4
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that receives a string as an argument (defaults to an empty string) and returns a dictionary with the unique words and their frequency.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, for a string such as:

    ```
    This is the first sentence. This is the scecond sentence. This is not the fourth sentence, it is the third sentence.
    ```

    the result of the function should be:
    """)
    return


@app.cell
def _():
    result = {
        'This': 3,
        'is': 4,
        'the': 4,
        'first': 1,
        'sentence': 4,
        'scecond': 1,
        'not': 1,
        'fourth': 1,
        'it': 1,
        'third': 1
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You may assume that word separators are limited to spaces, commas, and periods (no newline characters).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hint: You will want to split based on some character. Problem is that we really need to split based on three different characters: spaces, commas and periods. One approach would be to replace all commas and periods with spaces and then split on spaces.
    """)
    return


if __name__ == "__main__":
    app.run()
