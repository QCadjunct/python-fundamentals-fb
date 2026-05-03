import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Continue, Break and Else")
    return


@app.cell
def _():
    for i in range(100):
        print(i)
        if i >= 5:
            break
    print("done")
    return (i,)


@app.cell
def _():
    for i in range(1, 11):
        if i % 2 == 1:
            continue
        print(i)
    return (i,)


@app.cell
def _():
    data_1 = [1, 2, 3, -4, 5, 6]
    all_positive_1 = True
    for element in data_1:
        if element <= 0:
            all_positive_1 = False
            break
    print("all positive:", all_positive_1)
    return all_positive_1, data_1, element


@app.cell
def _():
    data_2 = [1, 2, 3, -4, 5, 6]
    for element in data_2:
        if element < 0:
            break
    else:
        print("processing all positive elements")
    return data_2, element


@app.cell
def _():
    data_3 = [1, 2, 3, 4, 5, 6]
    for element in data_3:
        if element < 0:
            break
    else:
        print("processing all positive elements")
    return data_3, element


if __name__ == "__main__":
    app.run()
