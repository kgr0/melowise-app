from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from colors import MAIN_RGBA

class StartScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.switch_screen, 1)

    def switch_screen(self, dt):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = "home"