# import kivy
# from kivy.app import App
# from kivy.lang import Builder

# from screens.home.home import HomeScreen
# from kivy.uix.screenmanager import ScreenManager, Screen

# kivy.require('1.9.0')

# class MeloWise(App):
    
#     def build(self):
#         Builder.load_file('views/home.kv')
#         return HomeScreen()

# melowise = MeloWise()
# melowise.run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import kivy
from screens.home.home import HomeScreen
from screens.interval.interval import IntervalScreen
from kivymd.app import MDApp

from screens.statistics.statistics import StatisticsScreen

kivy.require('1.9.0')

Builder.load_file('screens/home/home.kv')
Builder.load_file('screens/interval/interval.kv')
Builder.load_file('screens/statistics/statistics.kv')

class MyApp(MDApp):
    def build(self):
        # Builder.load_file('screens/home/home.kv')
        # return HomeScreen()
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(IntervalScreen(name='interval'))
        sm.add_widget(StatisticsScreen(name='statistics'))
        #sm.current = 'home'
        return sm

if __name__ == '__main__':
    MyApp().run()
