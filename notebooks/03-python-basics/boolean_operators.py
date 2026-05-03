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
    ### Boolean Operators
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    not reverses the truth value:
    """)
    return


@app.cell
def _():
    not True
    return


@app.cell
def _():
    not False
    return


@app.cell
def _():
    print(True and True)
    print(True and False)
    print(False and True)
    print(False and False)
    return


@app.cell
def _():
    print(True or True)
    print(True or False)
    print(False or True)
    print(False or False)
    return


@app.cell
def _():
    balance = 1000.00
    withdrawal = 50.00
    withdrawal_limit = 500.00
    (withdrawal < withdrawal_limit) and (withdrawal <= balance)
    return


@app.cell
def _(mo):
    mo.md("""
    Short-circuit evaluation -- normal case b non-zero:
    """)
    return


@app.cell
def _():
    a1 = 20
    b1 = 10
    a1 / b1 > 1
    return


@app.cell
def _(mo):
    mo.md("""
    When b is zero, a/b raises ZeroDivisionError. Guard with short-circuit and:
    """)
    return


@app.cell
def _():
    a2 = 20
    b2 = 0
    return a2, b2


@app.cell
def _(a2, b2):
    b2 != 0 and a2 / b2 > 1
    return


@app.cell
def _():
    a3 = 20
    b3 = 10
    print(b3 != 0 and a3 / b3 > 1)
    return


if __name__ == "__main__":
    app.run()
