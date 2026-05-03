import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    import string

    return mo, string


@app.cell
def _(mo):
    mo.md("""
    ### Common Set Operations
    """)
    return


@app.cell
def _():
    s1a = {"a", "b", "c"}
    s2a = {True, False}
    s3a = {"a", 100, 200}
    print(s1a.isdisjoint(s2a), s1a.isdisjoint(s3a))
    return


@app.cell
def _():
    s_mut = set()
    s_mut.add(100)
    s_mut.add(200)
    s_mut.add(100)
    s_mut.discard("x")
    try:
        s_mut.remove("x")
    except KeyError as e:
        print(f"KeyError: {e}")
    return


@app.cell
def _():
    s1b = set("abc")
    s2b = set("abcd")
    print(s1b <= s2b, s1b < s2b, s2b >= s1b)
    return


@app.cell
def _():
    s1c = set("abc")
    s2c = set("abc")
    print(s1c <= s2c, s1c < s2c)
    return


@app.cell
def _():
    s1d = set("abc")
    s2d = set("bcd")
    print("union:       ", s1d | s2d)
    print("intersection:", s1d & s2d)
    return


@app.cell
def _():
    str_1 = "python is an awesome language!"
    str_2 = "a python is also a snake."
    common = set(str_1) & set(str_2)
    print(common)
    return


@app.cell
def _():
    s1e = {"FB", "AMZN", "AAPL", "NFLX", "GOOG", "MSFT"}
    s2e = {"BABA", "WMT", "COST"}
    s3e = {"TSLA", "F", "GM"}
    symbols = list(s1e | s2e | s3e)
    print(sorted(symbols))
    return


@app.cell
def _():
    sold = {"w1", "w2", "w3", "w4"}
    returned = {"w1"}
    not_returned = sold - returned
    print(not_returned)
    return


@app.cell
def _(string):
    text_1 = "The quick brown fox jumps over the lazy dog"
    missing_1 = set(string.ascii_letters.casefold()) - set(text_1.casefold())
    print("Missing:", missing_1)
    return


@app.cell
def _(string):
    text_2 = "aBcDeFgHiJkKlLmMnNoOpPqQrRsStTuUvVwW"
    missing_2 = set(string.ascii_letters.casefold()) - set(text_2.casefold())
    print("Missing:", missing_2)
    return


if __name__ == "__main__":
    app.run()
