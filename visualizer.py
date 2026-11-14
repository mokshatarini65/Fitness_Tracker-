import matplotlib.pyplot as plt
import pandas as pd


def create_calories_chart(records):
    df = pd.DataFrame(records)

    if df.empty:
        return None

    daily_data = df.groupby("date")["calories"].sum()

    fig, ax = plt.subplots()
    daily_data.plot(kind="bar", ax=ax)

    ax.set_title("Daily Calories Burned")
    ax.set_xlabel("Date")
    ax.set_ylabel("Calories")
    plt.xticks(rotation=45)
    fig.tight_layout()

    return fig


def create_steps_chart(records):
    df = pd.DataFrame(records)

    if df.empty:
        return None

    daily_data = df.groupby("date")["steps"].sum()

    fig, ax = plt.subplots()
    daily_data.plot(kind="bar", ax=ax)

    ax.set_title("Daily Steps Walked")
    ax.set_xlabel("Date")
    ax.set_ylabel("Steps")
    plt.xticks(rotation=45)
    fig.tight_layout()

    return fig