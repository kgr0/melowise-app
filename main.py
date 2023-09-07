from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import kivy
from screens.chord.chord import ChordScreen
from screens.chord.chord_settings.chord_settings import ChordSettingsScreen
from screens.home.home import HomeScreen
from screens.interval.interval import IntervalScreen
from screens.interval.interval_settings.interval_settings import IntervalSettingsScreen
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from screens.start.start import StartScreen
from kivy.core.window import Window

from screens.statistics.statistics import StatisticsScreen

from kivy.config import Config

#set the window size to be resizable
#Config.set('graphics', 'resizable', True)
# Config.set('graphics', 'width', '828')
# Config.set('graphics', 'height', '1792')

kivy.require('1.9.0')

Builder.load_file('screens/home/home.kv')
Builder.load_file('screens/interval/interval.kv')
Builder.load_file('screens/interval/interval_settings/interval_settings.kv')
Builder.load_file('screens/chord/chord.kv')
Builder.load_file('screens/chord/chord_settings/chord_settings.kv')
Builder.load_file('screens/statistics/statistics.kv')
Builder.load_file('screens/start/start.kv')

colors = {
    "Teal": {
        "200": "#c2e8d1",
        "500": "#c2e8d1",
        "700": "#c2e8d1",
    },
    "Red": {
        "200": "#fea6b4",
        "500": "#fea6b4",
        "700": "#fea6b4",
    },
    "Light": {
        "StatusBar": "#c2e8d1",
        "AppBar": "#c2e8d1",
        "Background": "#e1f7e9",
        "CardsDialogs": "#fea6b4",
        "FlatButtonDown": "#CCCCCC",
    },
}

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(IntervalScreen(name='interval'))
        sm.add_widget(IntervalSettingsScreen(name='interval_settings'))
        sm.add_widget(ChordScreen(name='chord'))
        sm.add_widget(ChordSettingsScreen(name='chord_settings'))
        sm.add_widget(StatisticsScreen(name='statistics'))
        sm.add_widget(StartScreen(name="start_screen"))
        sm.current = "start_screen"
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.theme_style = "Light"
        Window.size = (360   , 780  )
        
        self.title = 'Melowise'

        
        return sm


if __name__ == '__main__':
    MyApp().run()
