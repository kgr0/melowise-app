from kivy.uix.screenmanager import Screen
from kivy.app import App

class HomeScreen(Screen):

     def switch_screen(self, screen_name):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = screen_name
    
     def go_to_statistics(self):
        self.manager.current = 'statistics'