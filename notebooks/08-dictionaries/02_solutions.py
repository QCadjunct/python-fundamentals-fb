import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False, width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Solutions - Section 08 Dictionaries")
    return


@app.cell
def _():
    s1 = "And or are the basic operations of logic."
    counts_1 = {}
    for c in s1:
        if (ord(c) >= ord("a") and ord(c) <= ord("z")) or \
           (ord(c) >= ord("A") and ord(c) <= ord("Z")):
            counts_1[c] = counts_1.get(c, 0) + 1
    counts_1
    return c, counts_1, s1


@app.cell
def _():
    s2 = "Python is an awesome language"
    counts_2 = {}
    for c in s2:
        if (ord(c) >= ord("a") and ord(c) <= ord("z")) or \
           (ord(c) >= ord("A") and ord(c) <= ord("Z")):
            counts_2[c] = counts_2.get(c, 0) + 1
    counts_2
    return c, counts_2, s2


@app.cell
def _():
    d1 = {"a": 10, "b": 20, "c": 30}
    d2 = {"d": 100, "e": 200, "f": 300}
    d3 = {"f": 30, "g": 40}
    keys_1 = list(d1.keys())
    values_1 = list(d1.values())
    for d in (d2, d3):
        keys_1.extend(d.keys())
        values_1.extend(d.values())
    print("keys:  ", keys_1)
    print("values:", values_1)
    return d, d1, d2, d3, keys_1, values_1


@app.cell
def _():
    grades_1 = {
        "John": [90, 95, 98],
        "Eric": [86, 84, 92],
        "Michael": [90, 89, 85],
    }
    exam = {"Eric": 99, "John": 100}
    for student in grades_1:
        grades_1[student].insert(0, exam.get(student))
    grades_1
    return exam, grades_1, student


if __name__ == "__main__":
    app.run()
