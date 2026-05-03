import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    ### Unicode
    """)
    return


@app.cell
def _():
    ord("A")
    return


@app.cell
def _():
    ord("\u03b1")
    return


@app.cell
def _():
    hex(ord("A")), hex(ord("\u03b1"))
    return


@app.cell
def _():
    int("3B1", 16)
    return


@app.cell
def _():
    var_A = "A"
    var_A
    return


@app.cell
def _():
    var_name = "\N{Latin Capital Letter A}lways look on the bright side of life."
    var_name
    return


@app.cell
def _():
    var_code = "\u0041lways look on the bright side of life"
    var_code
    return


@app.cell
def _():
    var_emoji1 = "\U0001F600"
    var_emoji1
    return


@app.cell
def _():
    var_emoji2 = "\N{Grinning Face}"
    var_emoji2
    return


if __name__ == "__main__":
    app.run()
