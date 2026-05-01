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
    ### Reshaping Arrays
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Reshaping an array basically allows us to rearrange the elements of an array - it is still the same elements, but arranged in a new shape.
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(np):
    arr = np.arange(12)
    return (arr,)


@app.cell
def _(arr):
    arr
    return


@app.cell
def _(arr):
    arr.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can reshape these twelve elements into a 4 x 3 array:
    """)
    return


@app.cell
def _(arr):
    m1 = arr.reshape(4, 3)
    m1
    return (m1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    or into a 2 x 6 array:
    """)
    return


@app.cell
def _(arr):
    m2 = arr.reshape(2, 6)
    m2
    return (m2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **CAUTION** Reshaping does not modify the original array, however the "positions" in both arrays are shared references.

    This means that modifying the element value in one array will affect the element value in the other array.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll come back to how we modify array elements, but we can do it using simple indexing, just like we have with lists:
    """)
    return


@app.cell
def _(arr):
    arr
    return


@app.cell
def _(m1):
    m1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's modify the first value of `arr`:
    """)
    return


@app.cell
def _(arr):
    arr[0] = 100
    return


@app.cell
def _(arr):
    arr
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we can see, `arr` was mutated, but observe what happened to `m1` and `m2`:
    """)
    return


@app.cell
def _(m1):
    m1
    return


@app.cell
def _(m2):
    m2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And the same thing happens if we modify an element of either `m1` and `m2`:
    """)
    return


@app.cell
def _(m1):
    m1[3][2] = 200
    return


@app.cell
def _(m1):
    m1
    return


@app.cell
def _(m2):
    m2
    return


@app.cell
def _(arr):
    arr
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, you should think of reshaping as a different "view" or "rearrangement" of the original array, not an entirely independent copy of the original.

    Later we'll see that even NumPyu slices behave the same way, which is very different from Python list slices which return sliced shallow copies.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we want an independent copy, we can simply make a copy using the `copy` method:
    """)
    return


@app.cell
def _(arr):
    m3 = arr.reshape(3, 4).copy()
    return (m3,)


@app.cell
def _(m3):
    m3
    return


@app.cell
def _(arr):
    arr
    return


@app.cell
def _(arr):
    arr[1] = -100
    return


@app.cell
def _(arr):
    arr
    return


@app.cell
def _(m3):
    m3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, `m3` was unaffected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also reshape a 2-D array into a 1-D array using the same `reshape` method:
    """)
    return


@app.cell
def _(np):
    m = np.array(
        [
            [1, 2, 3],
            [4, 5, 6]
        ]
    )
    return (m,)


@app.cell
def _(m):
    m.shape
    return


@app.cell
def _(m):
    arr2 = m.reshape(6)
    return (arr2,)


@app.cell
def _(arr2):
    arr2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And of course, the same reference sharing happens:
    """)
    return


@app.cell
def _(arr2):
    arr2[2] = 300
    arr2
    return


@app.cell
def _(m):
    m
    return


if __name__ == "__main__":
    app.run()
