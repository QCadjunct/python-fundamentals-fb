import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Default Values")
    return


@app.cell
def _():
    def func_1(a=1):
        return a
    print(func_1(), func_1(10), func_1(a=10))
    return (func_1,)


@app.cell
def _():
    def func_2(a, b=10, c=20):
        return a, b, c
    print(func_2(1))
    print(func_2(1, 2))
    print(func_2(1, 2, 3))
    print(func_2(1, c=100))
    return (func_2,)


@app.cell
def _():
    def is_close(a, b, abs_tol=0.01):
        return abs(a - b) <= abs_tol
    print(is_close(1.255, 1.256))
    print(is_close(10_001, 10_002))
    print(is_close(10_001, 10_002, 5))
    return (is_close,)


@app.cell
def _():
    def parse(s, sep=",", strip=True):
        items = s.split(sep)
        if strip:
            return [item.strip() for item in items]
        return items
    print(parse("  a,   b ,  c  "))
    print(parse("a  :  b : c ", sep=":"))
    return (parse,)


@app.cell
def _():
    data = [[10, 20, 30], [100, 200, 300], [1000, 2000, 3000]]
    return (data,)


@app.cell
def _(data):
    def process_row(row, item_sep):
        return item_sep.join(str(e) for e in row)
    def process_data(data, item_sep=",", line_sep="\n"):
        row_strings_1 = [process_row(row, item_sep) for row in data]
        return line_sep.join(row_strings_1)
    print(process_data(data))
    print(process_data(data, "|"))
    return process_data, process_row


if __name__ == "__main__":
    app.run()
