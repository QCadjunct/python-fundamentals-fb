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
    ### The elif Clause
    """)
    return


@app.cell
def _():
    grade_1 = 72
    if grade_1 >= 80:
        print("Passed with distinction")
    elif grade_1 >= 70:
        print("Passed")
    else:
        print("Failed")
    return


@app.cell
def _():
    grade_2 = 72
    if grade_2 >= 90:
        letter_grade_2 = "A"
    elif grade_2 >= 80:
        letter_grade_2 = "B"
    elif grade_2 >= 70:
        letter_grade_2 = "C"
    elif grade_2 >= 60:
        letter_grade_2 = "D"
    else:
        letter_grade_2 = "F"
    print(letter_grade_2)
    return


@app.cell
def _():
    account_enabled_s1 = True
    balance_s1 = 1000
    withdraw_s1 = 100_000
    if not account_enabled_s1:
        print("account disabled")
    elif withdraw_s1 > balance_s1:
        print("insufficient funds")
    else:
        print("withdrawal authorized")
    return


if __name__ == "__main__":
    app.run()
