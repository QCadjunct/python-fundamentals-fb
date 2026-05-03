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
    ### Handling Exceptions
    """)
    return


@app.cell
def _():
    try:
        1 / 0
    except ZeroDivisionError as ex:
        print(f"Exception: {type(ex)}, {ex}")
    print("code continues running...")
    return


@app.cell
def _():
    l_1 = [1, 2, 3, 4, 5]
    try:
        while True:
            print(l_1.pop())
    except IndexError:
        print("all done")
    return


@app.cell
def _():
    l_2 = (1, 2, 3, 4, 5)
    try:
        while True:
            print(l_2.pop())
    except IndexError:
        print("all done")
    except AttributeError as e:
        print(f"AttributeError: {e}")
    return


@app.cell
def _(mo):
    mo.md("""
    Averaging with EAFP - normal data:
    """)
    return


@app.cell
def _():
    data_1 = [10, 20, 10, 5]
    sum_data_1 = 0
    count_data_1 = 0
    try:
        for e1 in data_1:
            sum_data_1 += e1
            count_data_1 += 1
        average_1 = sum_data_1 / count_data_1
    except ZeroDivisionError:
        average_1 = 0
    except TypeError:
        average_1 = 0
    print(f"average = {average_1}")
    return


@app.cell
def _(mo):
    mo.md("""
    Empty list - ZeroDivisionError caught:
    """)
    return


@app.cell
def _():
    data_2 = []
    sum_data_2 = 0
    count_data_2 = 0
    try:
        for e2 in data_2:
            sum_data_2 += e2
            count_data_2 += 1
        average_2 = sum_data_2 / count_data_2
    except ZeroDivisionError:
        average_2 = 0
    print(f"average = {average_2}")
    return


@app.cell
def _(mo):
    mo.md("""
    Mixed types - skip non-numeric elements:
    """)
    return


@app.cell
def _():
    data_3 = [10, 20, "a"]
    sum_data_3 = 0
    count_data_3 = 0
    try:
        for e3 in data_3:
            try:
                sum_data_3 += e3
                count_data_3 += 1
            except TypeError:
                pass
        average_3 = sum_data_3 / count_data_3
    except ZeroDivisionError:
        average_3 = 0
    print(f"average = {average_3}")
    return


@app.cell
def _():
    try:
        raise ValueError("custom message")
    except ValueError as ex:
        print(f"handled ValueError: {ex}")
    finally:
        print("this always executes")
    print("all done")
    return


if __name__ == "__main__":
    app.run()
