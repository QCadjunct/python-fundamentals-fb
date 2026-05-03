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
    Use a dictionary to count the frequency of the characters `a-z A-Z` in a given string.

    You should write your code to be as general as possible, so that it will work with any string of any given length.

    Your resulting dictionary should only contain keys for characters that occured at least once (i.e. no zero count characters should be present.)

    Hint: you will probably want to use the `ord()` function that we studied earlier along with the unicode character codes for `a`, `z`, `A` and `Z`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, if the given string is:

    ```
    s = 'Aa, Bb - A a B C'
    ```

    then your resulting dictionary should be:

    ```
    {
        'A': 2,
        'a': 2,
        'B': 2,
        'b': 1,
        'C': 1
    }
    ```

    (Note that the order of the keys in the dictionary is not important)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here are two sample strings you can use:
    """)
    return


@app.cell
def _():
    s1 = """
    “'And' and 'or' are the basic operations of logic. Together with 'no' (the logical operation 
    of negation) they are a complete set of basic logical operations — all other logical 
    operations, no matter how complex, can be obtained by suitable combinations of these.” 
    ― John von Neumann, The Computer and the Brain
    """

    s2 = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
    in culpa qui officia deserunt mollit anim id est laborum.
    """
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
    Given the following dictionaries:
    """)
    return


@app.cell
def _():
    d1 = {'a': 10, 'b': 20, 'c': 30}
    d2 = {'d': 100, 'e': 200, 'f': 300}
    d3 = {'f': 30, 'g': 40}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Construct two lists, one containing all the keys of both dictionaries, and one containing all the values of each dictionary. (It is OK for values or keys to be repeated in the lists).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the example above you should end up with two lists containing the elements:

    ```
    'a', 'b', 'c', 'd', 'e', 'f', 'f', 'g'
    ```

    and

    ```
    10, 20, 30, 100, 200, 300, 30, 40
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that the order in which the elements appear in each list is not important.
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
    In this example, suppose you have a grade book designed as follows:
    """)
    return


@app.cell
def _():
    grades = {
        'John': [90, 95, 98],
        'Eric': [86, 84, 92],
        'Michael': [90, 89, 85]
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This grade book is a dictionary that consists of the student's name as the key, and the value is a list representing results for a series of tests, from most recent to oldest.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A new exam has just been graded, and you receive the grades for that specific exam also as a dictionary:
    """)
    return


@app.cell
def _():
    exam = {
        'Eric': 99,
        'John': 100
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write code that updates the grades dictionary by adding the latest test result to the beginning of each list corresponding to the student.

    If the new exam grade is missing for a student, assign the value `None` as the latest grade in the `grades` dictionary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For the data given above, your `grades` dictionary should now contain the following information:

    ```
    {
        'John': [100, 90, 95, 98],
        'Eric': [99, 86, 84, 92],
        'Michael': [None, 90, 89, 85]
    }
    ```
    """)
    return


if __name__ == "__main__":
    app.run()
