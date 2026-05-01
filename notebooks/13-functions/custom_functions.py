import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from datetime import datetime

    return datetime, mo


@app.cell
def _(mo):
    mo.md("""
    ### Custom Functions
    """)
    return


@app.cell
def _():
    def say_hello():
        return "hello!"
    say_hello()
    return (say_hello,)


@app.cell
def _(say_hello):
    alias = say_hello
    print(alias is say_hello)
    print(alias())
    return


@app.cell
def _():
    def add(a, b, c):
        return a + b + c
    result_1 = add(1, 2, 3)
    result_2 = add(3, 2, 1)
    print(result_1, result_2)
    return


@app.cell
def _():
    def find_max(a, b, c):
        max_ = a
        if b > max_:
            max_ = b
        if c > max_:
            max_ = c
        return max_
    print(find_max(10, 20, 30))
    print(find_max(30, 10, 20))
    return


@app.cell
def _(datetime):
    def log(message):
        curr_time = datetime.utcnow().isoformat()
        print(f"{curr_time} - [{message}]")
    log("log 1")
    log("log 2")
    return


@app.cell
def _():
    def is_all_positive(data):
        for element in data:
            if element < 0:
                return False
        return True
    print(is_all_positive([1, 2, 3, 4, 5]))
    print(is_all_positive({10, 20, -3}))
    print(is_all_positive(range(10)))
    return


@app.cell
def _():
    def gen_matrix(rows, cols, default_value):
        return [[default_value for _ in range(cols)] for _ in range(rows)]
    print(gen_matrix(3, 2, 1))
    print(gen_matrix(rows=3, cols=5, default_value=0))
    return


if __name__ == "__main__":
    app.run()
