import sqlite3

DATABASE_NAME = "workouts.db"


# Create database and table
def initialize_db():

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            activity TEXT NOT NULL,
            duration INTEGER NOT NULL,
            calories INTEGER NOT NULL,
            steps INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# Insert workout
def add_workout(date, activity, duration, calories, steps):

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO workouts
        (date, activity, duration, calories, steps)
        VALUES (?, ?, ?, ?, ?)
    """, (date, activity, duration, calories, steps))

    connection.commit()
    connection.close()


# Retrieve all workouts
def get_workouts():

    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM workouts ORDER BY date DESC, id DESC")

    records = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return records