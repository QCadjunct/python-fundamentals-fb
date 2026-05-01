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
    Generate the sample space of rolling two 6-sided dice, numbered `'9', '10', 'J', 'Q', 'K', 'A'`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    (The sample space is the set of all possible outcomes).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your result should be a list containing tuples for the outcome of each die, e.g.

    ```
    [('9', '9'),
     ('9', '10'),
     ('9', 'J'),
     ('9', 'Q'),
     ('9', 'K'),
     ('9', 'A'),
     ('10', '9'),
     ('10', '10'),
     ('10', 'J'),
     ('10', 'Q'),
     ('10', 'K'),
     ('10', 'A'),
     etc
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Make this a function that returns the sample space, called `make_sample_space`.
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
    Using the sample space you just created above, simulate throwing the two die `n` times by making random choices from the sample space.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Again, make this into a function that returns the random choices as a list of tuples, with `n` as a parameter of this function.

    Call the function `simulate_throws_from_sample_space`.
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
    Your goal here is to implement a function `simulate_throws`, similar to the one you wrote in Question 2, but without generating a sample space at all - just using the `face_values`.

    Write a function that implements this, and name it `simulate_throws`.
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
    Using both methods of generating throws, build a dictionary that contains the face values as keys, and the number of times they were selected in the simulated throws.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, assuming you made `100` throws using one of these methods, your dictionary might look like this:

    ```
    {
        '9': 39,
        '10': 27,
        'J': 28,
        'Q': 34,
        'K': 36,
        'A': 36
    }
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that your values in the dictionary should add up to `200` is you made one `100` throws.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that is given the function to use to generate the throws, the number of throws to simulate, and returns this dictionary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question 5
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that given two arguments `a` and `b` returns a random float between `a` (inclusive) and `b` (exclusive).
    """)
    return


if __name__ == "__main__":
    app.run()
