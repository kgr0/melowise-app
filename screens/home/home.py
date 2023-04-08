import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.app import App

class HomeScreen(Screen):

    # def __init__(self):
    #     super().__init__()

     def switch_screen(self, screen_name):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = screen_name
        
    # def switch_to_interval(self):
    #     self.manager.current = 'interval'