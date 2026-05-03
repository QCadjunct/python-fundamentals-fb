import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Solutions - Section 05 Sequence Types")
    return


@app.cell
def _():
    l1_ex1 = [1, 2, 3, 4, 5]
    l2_ex1 = [6, 7, 8, 9, 10]
    l3_ex1 = l1_ex1 + l2_ex1
    print(l3_ex1)
    return l1_ex1, l2_ex1, l3_ex1


@app.cell
def _():
    l1_ex2 = [1, 2, 3]
    l2_ex2 = l1_ex2 * 3
    print(l2_ex2)
    return l1_ex2, l2_ex2


@app.cell
def _():
    l1_ex3 = [1, 2, 3, 4, 5]
    l2_ex3 = l1_ex3[1:4]
    l3_ex3 = l1_ex3[::-1]
    print(l2_ex3, l3_ex3)
    return l1_ex3, l2_ex3, l3_ex3


if __name__ == "__main__":
    app.run()
