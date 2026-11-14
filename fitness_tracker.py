class Workout:

    def __init__(self, date, activity, duration, calories, steps):
        self.date = date
        self.activity = activity
        self.duration = duration
        self.calories = calories
        self.steps = steps

    def get_details(self):
        return {
            "Date": self.date,
            "Activity": self.activity,
            "Duration (min)": self.duration,
            "Calories Burned": self.calories,
            "Steps": self.steps
        }


class FitnessTracker:

    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def get_total_calories(self):
        return sum(w.calories for w in self.workouts)

    def get_total_steps(self):
        return sum(w.steps for w in self.workouts)

    def get_total_duration(self):
        return sum(w.duration for w in self.workouts)

    def get_workout_count(self):
        return len(self.workouts)

    def get_all_workouts(self):
        return [w.get_details() for w in self.workouts]