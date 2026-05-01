import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### While Loops")
    return


@app.cell
def _():
    price_1 = 100
    while price_1 > 90:
        print(f"price = {price_1} - waiting...")
        price_1 -= 1
    print(f"buying at {price_1}.")
    return (price_1,)


@app.cell
def _():
    price_2 = 100
    while price_2 < 50:
        print(f"price={price_2}")
    print("done")
    return (price_2,)


@app.cell
def _():
    data_1 = [100, 200, 300, 400, 500]
    while len(data_1) > 0:
        last = data_1.pop()
        print(f"processing: {last}")
    return data_1, last


@app.cell
def _():
    data_2 = [100, 200, 300, 400, 500]
    for i in range(len(data_2)):
        print(f"i={i}, data={data_2}")
        try:
            elem = data_2.pop(i)
            print(f"processing: {elem}")
        except IndexError as e:
            print(f"IndexError: {e}")
            break
    return data_2, elem, i


if __name__ == "__main__":
    app.run()
