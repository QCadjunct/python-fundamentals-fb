import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    from math import sqrt
    return mo, sqrt


@app.cell
def _(mo):
    mo.md("### List Comprehensions")
    return


@app.cell
def _(sqrt):
    vectors = [(0, 0), (0, 1), (1, 0), (1, 1)]
    magnitudes_1 = []
    for vector in vectors:
        magnitudes_1.append(sqrt(vector[0] ** 2 + vector[1] ** 2))
    print(magnitudes_1)
    return magnitudes_1, vector, vectors


@app.cell
def _(sqrt, vectors):
    magnitudes_2 = [sqrt(v[0] ** 2 + v[1] ** 2) for v in vectors]
    print(magnitudes_2)
    return (magnitudes_2,)


@app.cell
def _():
    strings = "Python is an awesome language".split()
    filtered_1 = [item for item in strings if len(item) >= 5]
    print(filtered_1)
    return filtered_1, strings


@app.cell
def _():
    sales = {"widget 1": 0, "widget 2": 5, "widget 3": 10, "widget 4": 2}
    high_sales_1 = [key for key, value in sales.items() if value >= 5]
    print(high_sales_1)
    return high_sales_1, sales


@app.cell
def _():
    m1 = [[0] * 3 for row in range(3)]
    m1[0][0] = 1
    print(m1)
    return (m1,)


@app.cell
def _():
    n1 = 3
    m2 = [[1 if r == c else 0 for c in range(n1)] for r in range(n1)]
    print(m2)
    return m2, n1


if __name__ == "__main__":
    app.run()
