import marimo

__generated_with = "0.23.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Basic Imports
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To use a module or package, either from Python's standard library, or a 3rd party library (which needs ot be installed into your virtual environment first of course), you have to `import` it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This essentially loads the module, and sets a local symbol (variable) pointing to the module.

    (Yes, modules are objects too!)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Once we have that module imported and a symbol pointing to it, we can reach inside for whatever objects that module has (such as functions, data types, or maybe even nested modules).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's look at the `math` module in Python, which contains a slew of math related functions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First we need to import it:
    """)
    return


@app.cell
def _():
    import math

    return (math,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now `math` is a variable (symbol) in our current namespace pointing to this math module (object), just like:
    """)
    return


@app.cell
def _():
    a = 1
    return (a,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    creates a variable(symbol) `a` pointing to the integer `1`
    """)
    return


@app.cell
def _(a):
    a
    return


@app.cell
def _(math):
    math
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This `math` module has quite a few functions available.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can see read the official docs here: https://docs.python.org/3/library/math.html
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or, you can use the built-in `help()` function as well:
    """)
    return


@app.cell
def _(math):
    help(math)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, we can see that there is a `factorial` function. We can load the help for just that function:
    """)
    return


@app.cell
def _(math):
    help(math.factorial)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we can see, this function takes a single argument (`x`) and the function will raise a `ValueError` exception if `x` is not a non-negative integer.

    The `/` you see in the docs means that all the parameters before it **must** be passed as positional arguments.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So we can reference the `factorial` function in the `math` module using dot notation (just like have been using with objects and properties or methods on those objects). After all, modules are objects, and we are basically accessing functions and attributes inside that object.
    """)
    return


@app.cell
def _(math):
    math.factorial(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are also non-function-like objects in the `math` module, such as `pi`:
    """)
    return


@app.cell
def _(math):
    math.pi
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see a few more functions in that module:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can find the greatest common divisor of two integers:
    """)
    return


@app.cell
def _(math):
    math.gcd(15, 25)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The square root function is also found here:
    """)
    return


@app.cell
def _(math):
    math.sqrt(16)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If you use the `math.sqrt` function, you cannot use a negative number. Although Python supports complex numbers, you need to use a special module for complex math, called `cmath`.
    """)
    return


@app.cell
def _():
    import cmath

    return (cmath,)


@app.cell
def _(cmath):
    cmath.sqrt(-4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll come back to the `math` module in a later chapter in this course.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, when we import a module:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Not only does Python load the module specified, but it also assigns that object to a variable, which by default is named the same.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can, if we prefer, assign it to a different name - an alias if you will, using `as`:
    """)
    return


@app.cell
def _():
    import math as m

    return (m,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now `m` is a variable in our namespace that points to the `math` module.
    """)
    return


@app.cell
def _(m):
    m
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    (We already have a symbol called `math` in our namespace that points to the same module, so in fact we can use both `math.` and `m.` - but that's because we basically imported the same module twice. Note that is is not actually inefficient - once a module has been loaded, Python will not re-load the module if it is re-imported - that module object exists and a new import just ends up creating a new variable pointing to the same object)
    """)
    return


@app.cell
def _(m, math):
    math is m
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's load a different module using an alias just to see that the original module name is not available, only the alias:
    """)
    return


@app.cell
def _():
    import random as rnd

    return (rnd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we loaded the random module, and we have a variable (symbol) named `rnd` that points to that `random` module:
    """)
    return


@app.cell
def _(rnd):
    rnd
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The docs for that module can be found here: https://docs.python.org/3/library/random.html
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, we can generate a random integer bounded (inclusively) by two values:
    """)
    return


@app.cell
def _(rnd):
    rnd.randint(10, 20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `random` module is another module we'll come back to later in more detail.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In general it is customary not to rename (alias) a module, unless there are reasons to do so - like trying to import two modules from different libraries that might be named the same.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As always there are exceptions to that rule, and you'll often see people import some of the standard libraries such as `numpy` using `np` as an alias, or `pandas` using `pd` as an alias.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    These are pretty much widely known and accepted conventions, so that's OK. But otherwise, using a custom alias might make your code harder to read, so use wisely.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example using `m` as an alias to `math` like I did earlier is probably a good example of what **not** to do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One thing you will notice when you compare the Python standard library vs 3rd party libraries is that Python tends to keep modules/packages very flat - not a whole lot of nested modules.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What do I mean by nested modules?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's look at the `os` module. It provides functionality for dealing with OS level things, like files, directories, etc.
    """)
    return


@app.cell
def _():
    import os

    return (os,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To get the current directory (as a relative path), we have to use `curdir` that is in the `path` module contained in the `os` module:
    """)
    return


@app.cell
def _(os):
    os.path.curdir
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could actually import and alias `os.path`:
    """)
    return


@app.cell
def _():
    import os.path as os_path

    return (os_path,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And now we can use `os_path`
    """)
    return


@app.cell
def _(os_path):
    os_path.curdir
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In fact, remember what I said that no matter how many times you import the same module, we always get the same object back:
    """)
    return


@app.cell
def _(os, os_path):
    os_path is os.path
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could even alias it this way:
    """)
    return


@app.cell
def _():
    import os.path as path

    return (path,)


@app.cell
def _(path):
    path.abspath(path.curdir)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There's actually a better way to do this that we'll see in the next set of videos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So far we have seen that we can get functions and other variables (such as `pi`) from modules.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But modules can also define data types (aka classes) beyond what's in the built-ins (int, list, etc).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For example, there is a `fractions` module that allows us to define fraction type objects:
    """)
    return


@app.cell
def _():
    import fractions

    return (fractions,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This module has a class (data type) called `Fraction` that we can use to create and manipulate fractions (rational numbers):
    """)
    return


@app.cell
def _(fractions):
    f1 = fractions.Fraction(1, 2)
    return (f1,)


@app.cell
def _(f1):
    f1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is the fractions `1/2`.
    """)
    return


@app.cell
def _(fractions):
    f2 = fractions.Fraction(1, 4)
    return (f2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can add those two fractions for example:
    """)
    return


@app.cell
def _(f1, f2):
    f1 + f2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can see more information about the `fractions` module here: https://docs.python.org/3/library/fractions.html?highlight=fractions#module-fractions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One interesting functionality of the `Fraction` type is that you can request a fraction that is exactly equal to some `float`:
    """)
    return


@app.cell
def _(fractions):
    f = fractions.Fraction.from_float(0.3)
    return (f,)


@app.cell
def _(f):
    f
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So now, you have a way to see an exact representation of a float as a rational number. As expected `0.3` cannot be stored exactly, so we do not get:
    """)
    return


@app.cell
def _(fractions):
    fractions.Fraction(3, 10)
    return


@app.cell
def _(fractions):
    fractions.Fraction(3, 10) == fractions.Fraction.from_float(0.3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python has many modules and packages available in the standard library:

    https://docs.python.org/3/library/
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should peruse those docs once in a while and start to get familiar with the official Python docs (how things are laid out, where to find thingsd) as well as get a sense for what's included standard with Python.
    """)
    return


if __name__ == "__main__":
    app.run()
