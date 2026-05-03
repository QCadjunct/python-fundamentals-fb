import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Ternary Conditional Operator")
    return


@app.cell
def _():
    ask_price_1 = 100
    volume_1 = 50 if ask_price_1 > 50 else 80
    print(volume_1)
    return ask_price_1, volume_1


@app.cell
def _():
    ask_price_2 = 100
    volume_2 = 50 if ask_price_2 > 50 else 80
    print(volume_2)
    return ask_price_2, volume_2


@app.cell
def _():
    a1 = 10
    b1 = 20
    distance_1 = a1 - b1 if a1 >= b1 else b1 - a1
    print(distance_1)
    return a1, b1, distance_1


@app.cell
def _():
    a2 = 20
    b2 = 10
    distance_2 = a2 - b2 if a2 >= b2 else b2 - a2
    print(distance_2)
    return a2, b2, distance_2


@app.cell
def _():
    current_value_1 = 100
    running_total_1 = 15000
    cleaned_value_1 = 0 if current_value_1 == -999 else current_value_1
    running_total_1 = running_total_1 + cleaned_value_1
    print(running_total_1)
    return cleaned_value_1, current_value_1, running_total_1


@app.cell
def _():
    current_value_2 = -999
    running_total_2 = 15000
    cleaned_value_2 = 0 if current_value_2 == -999 else current_value_2
    running_total_2 = running_total_2 + cleaned_value_2
    print(running_total_2)
    return cleaned_value_2, current_value_2, running_total_2


if __name__ == "__main__":
    app.run()
