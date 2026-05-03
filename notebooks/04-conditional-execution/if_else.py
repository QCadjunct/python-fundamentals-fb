import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### if...else...")
    return


@app.cell
def _():
    if 1 < 2:
        print("1 is less than 2")
    return


@app.cell
def _():
    account_enabled_s1 = True
    balance_s1 = 1000
    withdraw_s1 = 100
    if account_enabled_s1 and withdraw_s1 <= balance_s1:
        print("withdrawal authorized")
    else:
        print("withdrawal not authorized")
    return account_enabled_s1, balance_s1, withdraw_s1


@app.cell
def _():
    account_enabled_s2 = True
    balance_s2 = 1000
    withdraw_s2 = 10_000
    if account_enabled_s2 and withdraw_s2 <= balance_s2:
        print("withdrawal authorized")
    else:
        print("withdrawal not authorized")
    return account_enabled_s2, balance_s2, withdraw_s2


@app.cell
def _():
    account_enabled_s3 = False
    balance_s3 = 1000
    withdraw_s3 = 100
    if account_enabled_s3 and withdraw_s3 <= balance_s3:
        print("withdrawal authorized")
    else:
        print("withdrawal not authorized")
    return account_enabled_s3, balance_s3, withdraw_s3


@app.cell
def _():
    grade_1 = 72
    letter_grade_1 = "F"
    if grade_1 >= 60:
        letter_grade_1 = "D"
    if grade_1 >= 70:
        letter_grade_1 = "C"
    if grade_1 >= 80:
        letter_grade_1 = "B"
    if grade_1 >= 90:
        letter_grade_1 = "A"
    print(letter_grade_1)
    return grade_1, letter_grade_1


if __name__ == "__main__":
    app.run()
