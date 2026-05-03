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
    ### Working with Dictionaries
    """)
    return


@app.cell
def _():
    data_1 = {"open": 100, "high": 110, "low": 95, "close": 110}
    print("open" in data_1)
    print("volume" not in data_1)
    return


@app.cell
def _():
    data_2 = {"open": 100, "high": 110, "low": 95, "close": 110}
    print(len(data_2))
    data_2.clear()
    print(len(data_2))
    return


@app.cell
def _():
    d1 = dict(high=100, low=95)
    d2 = dict.fromkeys(["open", "high", "low", "close"], 0)
    d3 = dict.fromkeys("abc", 0)
    print(d1)
    print(d2)
    print(d3)
    return


@app.cell
def _():
    d4 = dict.fromkeys("abc", 0)
    print(d4.get("a", 100))
    print(d4.get("x", 100))
    return


@app.cell
def _():
    transactions = [
        {"item": "widget", "trans_type": "sale", "quantity": 10},
        {"item": "widget", "trans_type": "sale", "quantity": 5},
        {"item": "widget", "trans_type": "refund", "quantity": 2},
        {"item": "gadget", "trans_type": "sale", "quantity": 3},
    ]
    total_sold = {}
    for transaction in transactions:
        item = transaction["item"]
        is_sale = transaction["trans_type"] == "sale"
        quantity = transaction["quantity"]
        if is_sale:
            total_sold[item] = total_sold.get(item, 0) + quantity
    print(total_sold)
    return


@app.cell
def _():
    d5 = {"a": 1, "b": 2}
    d6 = {"c": 3, "d": 4}
    d5.update(d6)
    print(d5)
    return


@app.cell
def _():
    d7 = {"a": 1, "b": 2}
    d7.update({"b": 200, "c": 3})
    print(d7)
    return


if __name__ == "__main__":
    app.run()
