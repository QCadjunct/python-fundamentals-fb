import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Python Sets")
    return


@app.cell
def _():
    s1 = {"a", "b", "c"}
    type(s1)
    return (s1,)


@app.cell
def _():
    s2 = set(["a", "b", "c"])
    s3 = set("python")
    s4 = set(["a", "a", "b", "b"])
    s5 = set("banana")
    print(s2, s3, s4, s5)
    return s2, s3, s4, s5


@app.cell
def _():
    s6 = set()
    print(type(s6), len(s6))
    return (s6,)


@app.cell
def _():
    s7 = set("python")
    print("p" in s7, "x" not in s7)
    for item in s7:
        print(item, end=" ")
    return item, s7


if __name__ == "__main__":
    app.run()
