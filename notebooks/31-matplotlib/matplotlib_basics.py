import marimo

__generated_with = "0.23.4"
app = marimo.App(auto_instantiate=False)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Matplotlib Basics
    """)
    return


@app.cell
def _():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    return mpl, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are different buillt-in styles for Matplotlib, which can be listed this way:
    """)
    return


@app.cell
def _(mpl):
    mpl.style.available
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can see preview of these various styles here:

    https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To select a specific theme, we use `style.use()`:
    """)
    return


@app.cell
def _(mpl):
    mpl.style.use('seaborn-darkgrid')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To create a plot we have to create a figure and a set of axes.

    Each set of axes is basically a plot, and a figure can hold one or more of these axes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The simplest way to create a figure and axes is to use the `subplots()` function in the `pyplot` module:
    """)
    return


@app.cell
def _(plt):
    fig, ax = plt.subplots()
    return ax, fig


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So this create a figure and a set of axes, but of course it is blank.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To actually have something show up, we need to specify something to plot on the axes.
    """)
    return


@app.cell
def _(ax, np):
    x_pts = np.linspace(-2 * np.pi, 2 * np.pi, 200)
    y_pts = np.sin(x_pts)
    ax.plot(x_pts, y_pts, label='sin')
    return x_pts, y_pts


@app.cell
def _(fig):
    fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Typically we create and specify the plots in one cell:
    """)
    return


@app.cell
def _(plt, x_pts, y_pts):
    fig_1, ax_1 = plt.subplots()
    ax_1.plot(x_pts, y_pts, label='sin')
    return ax_1, fig_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can add more plots to the same axes, by simply creating more plots:
    """)
    return


@app.cell
def _(ax_1, fig_1, np, x_pts):
    ax_1.plot(x_pts, np.cos(x_pts), label='cos')
    fig_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can add labels to the axes:
    """)
    return


@app.cell
def _(ax_1, fig_1):
    ax_1.set_xlabel('x-axis label')
    ax_1.set_ylabel('y-axis label')
    fig_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Add a chart title:
    """)
    return


@app.cell
def _(ax_1, fig_1):
    ax_1.set_title('Trig Functions')
    fig_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Add a legend, which will be based on the labels we specified when we created the plots:
    """)
    return


@app.cell
def _(ax_1, fig_1):
    ax_1.legend()
    fig_1
    return


if __name__ == "__main__":
    app.run()
