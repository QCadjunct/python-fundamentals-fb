import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Objects
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll cover this later in this course, but let me first show you how we can create custom objects with state and functionality.

    So, don't worry if you don't understand this code right now, you soon will!
    """)
    return


@app.class_definition
class Account:
    def __init__(self, account_number, account_type, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance
        
    def deposit(self, amount):
        # should also check that amount is a numerical value!
        if amount > 0:
            self.balance = self.balance + amount
            print(f'Deposited {amount}')
            print(f'New balance is: {self.balance}')
        else:
            print(f'{amount} is an invalid amount.')
            
    def withdraw(self, amount):
        # should also check that amount is a numerical value!
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print(f'Withdrawal: {amount}')
            print(f'New Balance: {self.balance}')
        else:
            if amount < 0:
                print(f'{amount} is an invalid amount')
            else:
                print('Insufficient funds.')
                print(f'Current balance is {self.balance}')


@app.cell
def _():
    my_account = Account('123-456', 'savings', 1_000.00)
    return (my_account,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `my_account` is an **object** with **state**:
    """)
    return


@app.cell
def _(my_account):
    my_account.account_number
    return


@app.cell
def _(my_account):
    my_account.account_type
    return


@app.cell
def _(my_account):
    my_account.balance
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And it has **functionality**:
    """)
    return


@app.cell
def _(my_account):
    my_account.deposit(100)
    return


@app.cell
def _(my_account):
    my_account.withdraw(600)
    return


@app.cell
def _(my_account):
    my_account.withdraw(10_000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see we can access state and functionality of objects using this **dot** notation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In Python, everything is an object - this means everything we work with has state and functionality.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, integers are objects - they have **state** (their value), as well as **functionality** (they know how to add another number to themselves):
    """)
    return


@app.cell
def _():
    10 + 15
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `+` operator is actually using a functional attribute of the integer, called `__add__`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could have done the addition this way:
    """)
    return


@app.cell
def _():
    (10).__add__(15)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the same way, `floats` are also objects:
    """)
    return


@app.cell
def _():
    0.125
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One piece of functionality they have is the `as_integer_ratio` method, which can be useful if you want to get an exact representation of the float:
    """)
    return


@app.cell
def _():
    (0.125).as_integer_ratio()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see `0.125` is stored **exactly** as `1/8`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But as we know, not every float literal we specify can be stored exactly as we wrote it:
    """)
    return


@app.cell
def _():
    0.1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This may look like Python is storing this as `0.1`, but we know better:
    """)
    return


@app.cell
def _():
    format(0.1, '.25f')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But what is the **exact** number?
    """)
    return


@app.cell
def _():
    (0.1).as_integer_ratio()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we can see it is some big fraction, very close to `1`, but not exactly `1`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll come back to these kinds of topics, but for now the main take away is that everything we work with in Python is an object.
    """)
    return


if __name__ == "__main__":
    app.run()
