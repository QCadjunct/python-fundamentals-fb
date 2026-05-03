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
    mo.md("### Solutions - Section 13 Functions")
    return


@app.cell
def _():
    def average_v1(*args):
        try:
            return sum(args) / len(args)
        except ZeroDivisionError:
            raise ValueError("At least one argument required.")
    print(average_v1(1, 2, 3))
    try:
        average_v1()
    except ValueError as e:
        print(f"ValueError: {e}")
    return (average_v1,)


@app.cell
def _():
    def average_v2(arg, *args):
        sum_values_2 = arg + sum(args)
        return sum_values_2 / (len(args) + 1)
    print(average_v2(1, 2, 3))
    try:
        average_v2()
    except TypeError as e:
        print(f"TypeError: {e}")
    return (average_v2,)


@app.cell
def _():
    def separator(number=10, *, char="-"):
        return char * number
    print(separator())
    print(separator(5))
    print(separator(char="*"))
    print(separator(5, char="*"))
    return (separator,)


@app.cell
def _():
    def count_unique(iterable):
        return len(set(iterable))
    print(count_unique("abcdabcd"))
    print(count_unique([1, 1, 2, 2, 3]))
    f_unique = lambda iterable: len(set(iterable))
    print(f_unique("aabbcc"))
    return count_unique, f_unique


@app.cell
def _(Counter):
    def word_frequencies(s=""):
        s = s.replace(",", " ").replace(".", " ")
        return dict(Counter(s.split()))
    print(word_frequencies("word1, word2, word1. word1 word3"))
    return (word_frequencies,)


@app.cell
def _(word_frequencies):
    s_1 = "This is the first sentence. This is the scecond sentence. This is not the fourth sentence, it is the third sentence."
    computed_1 = word_frequencies(s_1)
    result_1 = {"This": 3, "is": 4, "the": 4, "first": 1, "sentence": 4, "scecond": 1, "not": 1, "fourth": 1, "it": 1, "third": 1}
    print(computed_1 == result_1)
    return computed_1, result_1, s_1


if __name__ == "__main__":
    app.run()
