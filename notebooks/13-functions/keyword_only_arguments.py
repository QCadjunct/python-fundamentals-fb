import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Keyword-Only Arguments")
    return


@app.cell
def _():
    def func_1(a, b, *, c):
        print(a, b, c)
    func_1(10, 20, c=30)
    try:
        func_1(10, 20, 30)
    except TypeError as e:
        print(f"TypeError: {e}")
    return (func_1,)


@app.cell
def _():
    def func_2(a, b=2, c=3, *, d=10, e, f=30):
        print(a, b, c, d, e, f)
    func_2(1, e=20)
    func_2(1, c=3.5, d=100, e=200)
    return (func_2,)


@app.cell
def _():
    data = [[10, 20, 30], [100, 200, 300], [1000, 2000, 3000]]
    def process_data_1(data, item_sep=",", line_sep="\n"):
        row_strings_1 = [item_sep.join([str(e) for e in row]) for row in data]
        return line_sep.join(row_strings_1)
    print(process_data_1(data, ":", "\n\n"))
    return data, process_data_1


@app.cell
def _(data):
    def process_data_2(data, *, item_sep=",", line_sep="\n"):
        row_strings_2 = [item_sep.join([str(e) for e in row]) for row in data]
        return line_sep.join(row_strings_2)
    print(process_data_2(data, item_sep=":", line_sep="\n\n"))
    try:
        process_data_2(data, ":", "\n\n")
    except TypeError as e:
        print(f"TypeError: {e}")
    return (process_data_2,)


@app.cell
def _():
    def coords_to_json(*, longitude, latitude):
        return f"{{\"longitude\": {longitude}, \"latitude\": {latitude}}}"
    print(coords_to_json(latitude=20, longitude=10))
    return (coords_to_json,)


if __name__ == "__main__":
    app.run()
