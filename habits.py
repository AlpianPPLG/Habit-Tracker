import json
from datetime import datetime

class Habit:
    def __init__(self, name, description, frequency):
        self.name = name
        self.description = description
        self.frequency = frequency

class HabitTracker:
    def __init__(self, habits_file='data/habits.json', progress_file='data/progress.json'):
        self.habits_file = habits_file
        self.progress_file = progress_file
        self.habits = self.load_habits()
        self.progress = self.load_progress()

    def load_habits(self):
        try:
            with open(self.habits_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def load_progress(self):
        try:
            with open(self.progress_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_habits(self):
        with open(self.habits_file, 'w') as file:
            json.dump(self.habits, file, indent=4)

    def save_progress(self):
        with open(self.progress_file, 'w') as file:
            json.dump(self.progress, file, indent=4)

    def add_habit(self, habit):
        self.habits[habit.name] = {
            'description': habit.description,
            'frequency': habit.frequency
        }
        self.save_habits()

    def track_habit(self, habit_name):
        if habit_name in self.habits:
            if habit_name not in self.progress:
                self.progress[habit_name] = []
            self.progress[habit_name].append(str(datetime.now().date()))
            self.save_progress()
