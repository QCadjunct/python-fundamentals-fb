import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from time import perf_counter
    return mo, perf_counter


@app.cell
def _(mo):
    mo.md("### Solutions - Section 12 Iterables and Iterators")
    return


@app.cell
def _():
    l_1 = [10, "abc", 3.14, True]
    for i, value in enumerate(l_1):
        print(f"l[{i}] = {value}")
    return i, l_1, value


@app.cell
def _(perf_counter):
    start_1 = perf_counter()
    for _ in range(10):
        g_1 = (i ** i for i in range(1, 10_001))
        for _ in range(5):
            next(g_1)
    end_1 = perf_counter()
    print(f"generator: {end_1 - start_1:.4f}s")
    return end_1, g_1, start_1


@app.cell
def _(perf_counter):
    start_2 = perf_counter()
    l_2 = [i ** i for i in range(1, 10_001)]
    for _ in range(10):
        for value in l_2[:5]:
            pass
    end_2 = perf_counter()
    print(f"list: {end_2 - start_2:.4f}s")
    return end_2, l_2, start_2, value


if __name__ == "__main__":
    app.run()
