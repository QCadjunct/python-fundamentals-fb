import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Raising Exceptions")
    return


@app.cell
def _():
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    return


@app.cell
def _():
    ex_1 = ValueError("Name must be at least 5 characters long.")
    print(type(ex_1))
    print(repr(ex_1))
    print(str(ex_1))
    return (ex_1,)


@app.cell
def _(ex_1):
    try:
        raise ex_1
    except ValueError as e:
        print(f"Caught: {e}")
    return


@app.cell
def _():
    name_1 = "Ana"
    try:
        if len(name_1) < 5:
            raise ValueError(f"{name_1} is not 5 characters or more...")
        print(f"Hello {name_1}!")
    except ValueError as e:
        print(f"ValueError: {e}")
    return (name_1,)


@app.cell
def _():
    name_2 = "Frederick"
    if len(name_2) < 5:
        raise ValueError(f"{name_2} is not 5 characters or more...")
    print(f"Hello {name_2}!")
    return (name_2,)


@app.cell
def _():
    print(issubclass(KeyError, LookupError))
    print(issubclass(KeyError, Exception))
    print(issubclass(LookupError, Exception))
    return


@app.cell
def _():
    ex_2 = KeyError("some message")
    print(isinstance(ex_2, KeyError))
    print(isinstance(ex_2, LookupError))
    print(isinstance(ex_2, IndexError))
    return (ex_2,)


if __name__ == "__main__":
    app.run()
