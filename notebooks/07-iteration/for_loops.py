import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    ### For Loops
    """)
    return


@app.cell
def _():
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    for suit in suits:
        print(f"{suit[0].upper()} = {suit}")
    return


@app.cell
def _():
    for c in "python":
        print(c.upper())
    return


@app.cell
def _():
    for i in range(2, 11, 2):
        print(i)
    return


@app.cell
def _(mo):
    mo.md("""
    Square matrix iteration:
    """)
    return


@app.cell
def _():
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for r1 in range(len(m1)):
        for c1 in range(len(m1[r1])):
            print(f"[{r1}, {c1}] = {m1[r1][c1]}")
    return


@app.cell
def _(mo):
    mo.md("""
    Ragged matrix:
    """)
    return


@app.cell
def _():
    m2 = [[0, 1], [2, 3, 4, 5, 6], [7, 8, 9], [10]]
    for r2 in range(len(m2)):
        for c2 in range(len(m2[r2])):
            print(f"[{r2}, {c2}] = {m2[r2][c2]}")
    return


@app.cell
def _(mo):
    mo.md("""
    Build n x n identity matrix:
    """)
    return


@app.cell
def _():
    n1 = 5
    matrix_1 = []
    for r3 in range(n1):
        row = []
        for c3 in range(n1):
            row.append(1 if r3 == c3 else 0)
        matrix_1.append(row)
    matrix_1
    return


@app.cell
def _(mo):
    mo.md("""
    enumerate() - index and value together:
    """)
    return


@app.cell
def _():
    data_1 = [10, 20, 30]
    for index, value in enumerate(data_1):
        print(f"{index}: {value}")
    return


@app.cell
def _(mo):
    mo.md("""
    Replace None with average - Pythonic one-liner:
    """)
    return


@app.cell
def _():
    data_2 = [10.5, 11.2, 9.8, None, 11.5, None]
    count = sum(1 for v in data_2 if v is not None)
    total = sum(v for v in data_2 if v is not None)
    average_2 = total / count
    data_2 = [v if v is not None else average_2 for v in data_2]
    print(data_2)
    return


if __name__ == "__main__":
    app.run()
