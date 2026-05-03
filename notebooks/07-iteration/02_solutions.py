import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Solutions - Section 07 Iteration")
    return


@app.cell
def _():
    m_1 = 3
    n_1 = 4
    for row in range(1, m_1 + 1):
        for col in range(1, n_1 + 1):
            print(f"{row} x {col} = {row * col}")
        print("-" * 15)
    return col, m_1, n_1, row


@app.cell
def _():
    m_2 = 5
    n_2 = 5
    for row in range(1, m_2 + 1):
        for col in range(1, n_2 + 1):
            print(f"{row} x {col} = {row * col}")
        print("-" * 15)
    return col, m_2, n_2, row


@app.cell
def _():
    data_1 = (
        ["2021-01-01", 10, 20],
        ["2021-01-02", 20, 18],
        ["2021-01-03", -10, 10],
        ["2021-01-04", 100, 102],
        ["2021-01-05", 20, 45],
    )
    for row in data_1:
        row.append(abs(row[1] - row[2]))
    data_1
    return (data_1,)


@app.cell
def _(data_1):
    max_spread_1 = data_1[0][-1]
    max_date_1 = data_1[0][0]
    for dt, num1, num2, spread in data_1[1:]:
        if spread > max_spread_1:
            max_spread_1 = spread
            max_date_1 = dt
    print(f"Max spread: {max_spread_1} on {max_date_1}")
    return dt, max_date_1, max_spread_1, num1, num2, spread


@app.cell
def _():
    data_2 = (
        ["2021-01-01", 10, 20],
        ["2021-01-02", 20, 18],
        ["2021-01-03", -10, 10],
        ["2021-01-04", 100, 102],
        ["2021-01-05", 20, 45],
    )
    for row in data_2:
        row.append(abs(row[1] - row[2]))
    max_spread_2 = data_2[0][-1]
    max_date_2 = data_2[0][0]
    for row in data_2[1:]:
        if row[-1] > max_spread_2:
            max_spread_2 = row[-1]
            max_date_2 = row[0]
    print(f"Max spread: {max_spread_2} on {max_date_2}")
    return data_2, max_date_2, max_spread_2, row


if __name__ == "__main__":
    app.run()
