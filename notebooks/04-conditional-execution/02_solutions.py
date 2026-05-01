import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("### Solutions — Section 04")
    return


@app.cell
def _():
    a_v1 = 100
    a_v1 = "N/A" if a_v1 is None else a_v1
    print(a_v1)
    return (a_v1,)


@app.cell
def _():
    a_v2 = None
    a_v2 = "N/A" if a_v2 is None else a_v2
    print(a_v2)
    return (a_v2,)


@app.cell
def _():
    score_1 = 720
    if score_1 < 580:
        rating_1 = "Poor"
    elif score_1 < 670:
        rating_1 = "Fair"
    elif score_1 < 740:
        rating_1 = "Good"
    elif score_1 < 800:
        rating_1 = "Very Good"
    else:
        rating_1 = "Excellent"
    print(rating_1)
    return rating_1, score_1


@app.cell
def _():
    score_2 = 100
    if score_2 < 580:
        rating_2 = "Poor"
    elif score_2 < 670:
        rating_2 = "Fair"
    elif score_2 < 740:
        rating_2 = "Good"
    elif score_2 < 800:
        rating_2 = "Very Good"
    else:
        rating_2 = "Excellent"
    print(rating_2)
    return rating_2, score_2


@app.cell
def _():
    seconds_in_minute = 60
    seconds_in_hour = 60 * seconds_in_minute
    seconds_in_day = 24 * seconds_in_hour
    seconds_in_week = 7 * seconds_in_day
    return seconds_in_day, seconds_in_hour, seconds_in_minute, seconds_in_week


@app.cell
def _(seconds_in_day, seconds_in_hour, seconds_in_minute, seconds_in_week):
    elapsed_1 = 23
    if elapsed_1 < seconds_in_minute:
        magnitude_1 = "seconds"
    elif elapsed_1 < seconds_in_hour:
        magnitude_1 = "minutes"
    elif elapsed_1 < seconds_in_day:
        magnitude_1 = "hours"
    elif elapsed_1 < seconds_in_week:
        magnitude_1 = "days"
    else:
        magnitude_1 = "weeks"
    print(magnitude_1)
    return elapsed_1, magnitude_1


@app.cell
def _(seconds_in_day, seconds_in_hour, seconds_in_minute, seconds_in_week):
    elapsed_2 = 30 * 60
    if elapsed_2 < seconds_in_minute:
        magnitude_2 = "seconds"
    elif elapsed_2 < seconds_in_hour:
        magnitude_2 = "minutes"
    elif elapsed_2 < seconds_in_day:
        magnitude_2 = "hours"
    elif elapsed_2 < seconds_in_week:
        magnitude_2 = "days"
    else:
        magnitude_2 = "weeks"
    print(magnitude_2)
    return elapsed_2, magnitude_2


if __name__ == "__main__":
    app.run()
