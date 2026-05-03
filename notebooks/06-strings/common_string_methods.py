import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    from timeit import timeit
    return mo, timeit


@app.cell
def _(mo):
    mo.md("### Common String Methods")
    return


@app.cell
def _():
    message_1 = "The definitive guide to Python"
    print(message_1.upper())
    print(message_1.lower())
    print(message_1.title())
    return (message_1,)


@app.cell
def _():
    brand_1 = "BMW"
    row_brand_1 = "bmw"
    print(brand_1.upper() == row_brand_1.upper())
    print(brand_1.lower() == row_brand_1.lower())
    return brand_1, row_brand_1


@app.cell
def _():
    street = "stra\N{LATIN SMALL LETTER SHARP S}e"
    data_1 = "STRASSE"
    print("lower:", street.lower() == data_1.lower())
    print("casefold:", street.casefold() == data_1.casefold())
    return data_1, street


@app.cell
def _():
    name_1 = "   Fred Baptiste   "
    print(repr(name_1.strip()))
    return (name_1,)


@app.cell
def _():
    data_2 = "Baptiste, Fred"
    last, first = data_2.split(",")
    print(repr(last), repr(first))
    return data_2, first, last


@app.cell
def _():
    data_3 = ["item 1", "item 2", "item 3"]
    ", ".join(data_3)
    return (data_3,)


@app.cell
def _():
    message_2 = "To every action there is always an equal and opposite reaction."
    print(message_2.index("every"))
    print(message_2.index("action"))
    return (message_2,)


@app.cell
def _(message_2):
    start_1 = message_2.index("action") + len("action")
    message_2.index("action", start_1)
    return (start_1,)


@app.cell
def _(timeit):
    message_3 = "Imagination is more important than knowledge - Einstein"
    t_in = timeit("'Einstein' in m", globals={"m": message_3}, number=1_000_000)
    t_find = timeit("m.find('Einstein')", globals={"m": message_3}, number=1_000_000)
    print(f"in: {t_in:.3f}s  find: {t_find:.3f}s")
    return message_3, t_find, t_in


if __name__ == "__main__":
    app.run()
