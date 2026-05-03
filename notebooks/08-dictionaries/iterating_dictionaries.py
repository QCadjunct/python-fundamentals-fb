import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Iterating Dictionaries")
    return


@app.cell
def _():
    d1 = {"key 1": 1, "key 2": 2, 3.14: "pi"}
    for k in d1:
        print(k)
    return d1, k


@app.cell
def _(d1):
    for k, v in d1.items():
        print(f"{k} = {v}")
    return k, v


@app.cell
def _():
    d2 = {"a": 1, "b": 2, "c": 3}
    d2["x"] = 24
    d2["b"] = 200
    for k, v in d2.items():
        print(k, v)
    return d2, k, v


@app.cell
def _(d2):
    del d2["b"]
    d2["b"] = 200
    for k, v in d2.items():
        print(k, v)
    return k, v


if __name__ == "__main__":
    app.run()
