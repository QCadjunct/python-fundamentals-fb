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
    ### Integer Division and Modulus
    """)
    return


@app.cell
def _():
    a = 10
    b = 3
    return a, b


@app.cell
def _(a, b):
    a / b
    return


@app.cell
def _(a, b):
    a // b
    return


@app.cell
def _():
    10 % 3
    return


@app.cell
def _(mo):
    mo.md("""
    #### Example 1 - Even or odd using modulo
    """)
    return


@app.cell
def _():
    10 % 2
    return


@app.cell
def _():
    11 % 2
    return


@app.cell
def _(mo):
    mo.md("""
    #### Example 2 - Convert elapsed minutes to hours and minutes
    """)
    return


@app.cell
def _():
    elapsed_minutes_ex1 = 165
    hours_ex1 = elapsed_minutes_ex1 // 60
    minutes_ex1 = elapsed_minutes_ex1 % 60
    print(hours_ex1, minutes_ex1)
    return


@app.cell
def _(mo):
    mo.md("""
    Works with any positive integer for elapsed_minutes:
    """)
    return


@app.cell
def _():
    elapsed_minutes_ex2 = 623
    hours_ex2 = elapsed_minutes_ex2 // 60
    minutes_ex2 = elapsed_minutes_ex2 % 60
    print(hours_ex2, minutes_ex2)
    return


@app.cell
def _(mo):
    mo.md("""
    #### Example 3 - Print progress every 100 iterations using modulo
    """)
    return


@app.cell
def _():
    total_a = 0
    for i in range(1, 1_001):
        total_a += i
        print(f"total = {total_a}...")
    print(f"Final total = {total_a}")
    return


@app.cell
def _(mo):
    mo.md("""
    Print every hundred iterations instead:
    """)
    return


@app.cell
def _():
    total_b = 0
    for j in range(1, 1_001):
        total_b += j
        if j % 100 == 0:
            print(f"total = {total_b}...")
    print(f"Final total = {total_b}")
    return


if __name__ == "__main__":
    app.run()
