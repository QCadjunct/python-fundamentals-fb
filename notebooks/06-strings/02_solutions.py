import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Solutions - Section 06 Strings")
    return


@app.cell
def _():
    s = "\u03a0, \u03cd, \u03b8, \u03c9, \u03bd"
    chars = [c.strip() for c in s.split(",")]
    code_points = [hex(ord(c)) for c in chars]
    lower = [c.lower() for c in chars]
    upper = [c.upper() for c in chars]
    print("code_points:", code_points)
    print("lower:", lower)
    print("upper:", upper)
    return chars, code_points, lower, s, upper


@app.cell
def _():
    a_ex2_v1 = 42
    print(f"The number {a_ex2_v1} {'is' if a_ex2_v1 % 2 == 0 else 'is not'} even")
    return (a_ex2_v1,)


@app.cell
def _():
    a_ex2_v2 = 31
    print(f"The number {a_ex2_v2} {'is' if a_ex2_v2 % 2 == 0 else 'is not'} even")
    return (a_ex2_v2,)


@app.cell
def _():
    a_ex2_v3 = -42
    print(f"The number {a_ex2_v3} {'is' if a_ex2_v3 % 2 == 0 else 'is not'} even")
    return (a_ex2_v3,)


@app.cell
def _():
    a_ex3 = 3.141592653589793
    b_ex3 = 6
    print(f"{a_ex3:.4f} / {b_ex3:.4f} = {a_ex3 / b_ex3:.4f}")
    return a_ex3, b_ex3


if __name__ == "__main__":
    app.run()
