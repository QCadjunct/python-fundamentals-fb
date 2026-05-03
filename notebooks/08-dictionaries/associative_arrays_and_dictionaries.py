import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Associative Arrays and Dictionaries")
    return


@app.cell
def _():
    d1 = {"a": 1, "b": 2, "c": 3}
    d1
    return (d1,)


@app.cell
def _():
    person = {"first_name": "Eric", "last_name": "Idle", "year_born": 2016}
    person["year_born"] = 1943
    person["month_born"] = "March"
    person
    return (person,)


@app.cell
def _():
    d2 = {3.14: "pi", 2: "even", "prime": 7}
    print(d2[3.14], d2[2], d2["prime"])
    return (d2,)


@app.cell
def _():
    l = [1, 2, 3]
    try:
        d3 = {l: 100}
    except TypeError as e:
        print(f"TypeError: {e}")
    return (l,)


@app.cell
def _():
    t1 = (1, 2, 3, 4)
    t2 = ([1, 2], 3, 4)
    print(hash(t1))
    try:
        hash(t2)
    except TypeError as e:
        print(f"TypeError: {e}")
    return t1, t2


@app.cell
def _():
    d4 = {(0, 0): "origin", (1, 0): "unit-x", (0, 1): "unit-y"}
    d4[(0, 0)]
    return (d4,)


@app.cell
def _():
    d5 = {"a": 1, "b": 2, "c": 3}
    del d5["a"]
    try:
        d5["x"]
    except KeyError as e:
        print(f"KeyError: {e}")
    return (d5,)


if __name__ == "__main__":
    app.run()
