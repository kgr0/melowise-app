from kivy.uix.screenmanager import Screen
from db.db import DatabaseHandler

class StatisticsScreen(Screen):
    def __init__(self, **kwargs):
        super(StatisticsScreen, self).__init__(**kwargs)
        self.db = DatabaseHandler()  # Create an instance of DatabaseHandler with the database name

    def back_to_home(self):
        self.manager.current = 'home'  # Navigate back to the main screen

    def get_answers_from_db(self):
        self.db = DatabaseHandler() 
        list = self.db.get_all_questions()
        return list