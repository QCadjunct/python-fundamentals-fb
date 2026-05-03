import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Solutions - Section 11 Exceptions")
    return


@app.cell
def _():
    values_1 = []
    if len(values_1) == 0:
        minimum_1 = 0
    else:
        minimum_1 = abs(values_1[0])
        for value in values_1[1:]:
            if abs(value) < minimum_1:
                minimum_1 = abs(value)
    print(f"Minimum is: {minimum_1}")
    return (values_1,)


@app.cell
def _():
    values_2 = [3, -2, 5]
    if len(values_2) == 0:
        minimum_2 = 0
    else:
        minimum_2 = abs(values_2[0])
        for value in values_2[1:]:
            if abs(value) < minimum_2:
                minimum_2 = abs(value)
    print(f"Minimum is: {minimum_2}")
    return (values_2,)


@app.cell
def _():
    values_3 = []
    try:
        minimum_3 = abs(values_3[0])
        for value in values_3[1:]:
            if abs(value) < minimum_3:
                minimum_3 = abs(value)
    except IndexError:
        minimum_3 = 0
    print(f"Minimum is: {minimum_3}")
    return (values_3,)


@app.cell
def _():
    values_4 = [2, -3, 4, -1]
    try:
        minimum_4 = abs(values_4[0])
        for value in values_4[1:]:
            if abs(value) < minimum_4:
                minimum_4 = abs(value)
    except IndexError:
        minimum_4 = 0
    print(f"Minimum is: {minimum_4}")
    return (values_4,)


@app.cell
def _():
    try:
        raise ValueError("Some custom message")
    except ValueError as ex:
        print(ex)
    return


if __name__ == "__main__":
    app.run()
