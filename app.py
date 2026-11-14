import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from visualizer import create_calories_chart, create_steps_chart

from fitness_tracker import Workout, FitnessTracker
from database import initialize_db, add_workout, get_workouts

# Initialize database
initialize_db()

# Page configuration
st.set_page_config(
    page_title="Fitness Tracker",
    page_icon="🏃",
    layout="wide"
)

# Load saved records from database
tracker = FitnessTracker()

records = get_workouts()

for record in records:
    workout = Workout(
        record["date"],
        record["activity"],
        record["duration"],
        record["calories"],
        record["steps"]
    )
    tracker.add_workout(workout)

# Sidebar
st.sidebar.title("🏃 Fitness Tracker")

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Add Workout", "Workout History", "Progress"]
)

# Dashboard
if menu == "Dashboard":

    st.title("🏃 Fitness Tracker Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Calories Burned",
        f"{tracker.get_total_calories()} kcal"
    )

    col2.metric(
        "Steps Walked",
        f"{tracker.get_total_steps():,}"
    )

    col3.metric(
        "Workout Duration",
        f"{tracker.get_total_duration()} min"
    )

    col4.metric(
        "Total Workouts",
        tracker.get_workout_count()
    )

    if records:
        st.success("Your workout data is saved in SQLite!")
    else:
        st.info("Add your first workout to get started.")

# Add Workout
elif menu == "Add Workout":

    st.title("➕ Add New Workout")

    with st.form("workout_form"):

        workout_date = st.date_input("Workout Date")

        activity = st.selectbox(
            "Activity Type",
            ["Walking", "Running", "Cycling",
             "Swimming", "Yoga", "Gym", "Other"]
        )

        duration = st.number_input(
            "Duration (minutes)",
            min_value=1,
            max_value=1440,
            value=30
        )

        calories = st.number_input(
            "Calories Burned",
            min_value=0,
            value=100
        )

        steps = st.number_input(
            "Steps Walked",
            min_value=0,
            value=3000
        )

        submitted = st.form_submit_button("Save Workout")

        if submitted:

            add_workout(
                str(workout_date),
                activity,
                int(duration),
                int(calories),
                int(steps)
            )

            st.success("Workout saved successfully!")

            st.info("Open Dashboard or Workout History to see your updated records.")

# Workout History
elif menu == "Workout History":

    st.title("📋 Workout History")

    if records:
        df = pd.DataFrame(records)

        df = df.drop(columns=["id"])

        st.dataframe(df, use_container_width=True)

    else:
        st.info("No workout records available.")

# Progress
elif menu == "Progress":
    st.title("Fitness Progress")

    if records:
        calories_fig = create_calories_chart(records)
        steps_fig = create_steps_chart(records)

        st.subheader("Daily Calories Burned")
        if calories_fig is not None:
            st.pyplot(calories_fig)
            plt.close(calories_fig)

        st.subheader("Daily Steps Walked")
        if steps_fig is not None:
            st.pyplot(steps_fig)
            plt.close(steps_fig)

    else:
        st.info("No workout records available. Add a workout first!")