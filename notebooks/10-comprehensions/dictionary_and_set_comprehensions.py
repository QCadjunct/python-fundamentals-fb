import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    from collections import Counter
    return Counter, mo


@app.cell
def _(mo):
    mo.md("### Dictionary and Set Comprehensions")
    return


@app.cell
def _():
    widget_sales = [
        {"name": "widget 1", "sales": 10},
        {"name": "widget 2", "sales": 5},
        {"name": "widget 3", "sales": 0},
    ]
    sales_by_widget_1 = {d["name"]: d["sales"] for d in widget_sales}
    print(sales_by_widget_1)
    return sales_by_widget_1, widget_sales


@app.cell
def _(widget_sales):
    sales_by_widget_2 = {d["name"]: d["sales"] for d in widget_sales if d["sales"] > 0}
    print(sales_by_widget_2)
    return (sales_by_widget_2,)


@app.cell
def _():
    paragraph_1 = "To be or not to be that is the question Whether tis nobler in the mind to suffer"
    words_1 = {word.lower() for word in paragraph_1.split() if len(word) > 4}
    print(words_1)
    return paragraph_1, words_1


@app.cell
def _():
    data = ["a", "a", "a", "b", "b", "c", "c", "c", "d"]
    freq_1 = {element: len([c for c in data if c == element]) for element in set(data)}
    print(freq_1)
    return data, freq_1


@app.cell
def _(Counter, data):
    freq_2 = Counter(data)
    print(dict(freq_2))
    return (freq_2,)


@app.cell
def _(Counter):
    paragraph_2 = "Lorem ipsum dolor sit amet consectetur adipiscing elit."
    ignored = " ,.
"
    freq_3 = {k: v for k, v in Counter(paragraph_2.casefold()).items() if k not in ignored}
    print(freq_3)
    return freq_3, ignored, paragraph_2


if __name__ == "__main__":
    app.run()
