import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Solutions - Section 09 Sets")
    return


@app.cell
def _():
    l = ["AAPL", "AAPL", "Aapl", "aapl", "MSFT"]
    unique_values_1 = set(l)
    unique_values_1
    return l, unique_values_1


@app.cell
def _(l):
    unique_values_2 = set()
    for symbol in l:
        unique_values_2.add(symbol.casefold())
    unique_values_2
    return symbol, unique_values_2


@app.cell
def _(l):
    unique_values_3 = {symbol.casefold() for symbol in l}
    unique_values_3
    return (unique_values_3,)


@app.cell
def _():
    data = {
        "d1": {"a": 1, "b": 2, "c": 3},
        "d2": {"b": 20, "c": 30, "d": 40},
        "d3": {"d": 100, "x": 200},
    }
    result = set()
    for d in data.values():
        result = result | d.keys()
    result
    return d, data, result


if __name__ == "__main__":
    app.run()
