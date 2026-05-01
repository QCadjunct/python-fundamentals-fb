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
    mo.md("### Iterables and Iterators")
    return


@app.cell
def _():
    l_1 = [1, 2, 3]
    iterator_1 = iter(l_1)
    print(type(iterator_1))
    print(next(iterator_1), next(iterator_1), next(iterator_1))
    return iterator_1, l_1


@app.cell
def _(iterator_1):
    try:
        next(iterator_1)
    except StopIteration:
        print("StopIteration - exhausted")
    return


@app.cell
def _(l_1):
    iterator_2 = iter(l_1)
    print(next(iterator_2))
    return (iterator_2,)


@app.cell
def _():
    l_2 = [1, 2, 3, 4, 5]
    for e in l_2:
        print(e)
    return e, l_2


@app.cell
def _(l_2):
    iterator_3 = iter(l_2)
    try:
        while True:
            print(next(iterator_3))
    except StopIteration:
        pass
    return (iterator_3,)


@app.cell
def _(perf_counter):
    start_1 = perf_counter()
    r_1 = range(100_000_000)
    end_1 = perf_counter()
    print(f"range created: {end_1 - start_1:.6f}s")
    return end_1, r_1, start_1


@app.cell
def _():
    enum_1 = enumerate("abc")
    print(list(enum_1))
    print(list(enum_1))
    return (enum_1,)


@app.cell
def _():
    enum_2 = enumerate("abc")
    print(iter(enum_2) is enum_2)
    print(next(enum_2), next(enum_2))
    return (enum_2,)


if __name__ == "__main__":
    app.run()
