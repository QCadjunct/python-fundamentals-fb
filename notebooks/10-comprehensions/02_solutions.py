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
    ### Solutions - Section 10 Comprehensions
    """)
    return


@app.cell
def _():
    data_1 = [
        {"open": 100, "high": 120, "low": 90, "close": 110},
        {"open": 110, "high": 130, "low": 80, "close": 120},
        {"open": 120, "high": 140, "low": 70, "close": 130},
        {"open": 130, "high": 150, "low": 60, "close": 140},
    ]
    ranges_1 = [d["high"] - d["low"] for d in data_1]
    print(ranges_1)
    return


@app.cell
def _():
    result_1 = []
    for number in range(1, 101):
        for n in range(2, 10):
            if number % n == 0:
                result_1.append(number)
                break
    not_divisible_1 = set(range(1, 101)) - set(result_1)
    print(sorted(not_divisible_1))
    return


@app.cell
def _():
    result_2 = {num for num in range(1, 101) for n in range(2, 10) if num % n == 0}
    not_divisible_2 = set(range(1, 101)) - result_2
    print(sorted(not_divisible_2))
    return


@app.cell
def _():
    data_2 = [
        {"symbol": "ABCD", "ranking": 2, "risk": 0.2},
        {"symbol": "BCDE", "ranking": 5, "risk": 0.2},
        {"symbol": "CDEF", "ranking": 8, "risk": 0.5},
        {"symbol": "DEFG", "ranking": 7, "risk": 0.8},
        {"symbol": "EFGH", "ranking": 9, "risk": 0.4},
    ]
    result_3 = [
        {"symbol": d["symbol"], "weighted": d["ranking"] * (1 - d["risk"])}
        for d in data_2
        if d["ranking"] >= 5 and d["risk"] < 0.6
    ]
    print(result_3)
    return


if __name__ == "__main__":
    app.run()
