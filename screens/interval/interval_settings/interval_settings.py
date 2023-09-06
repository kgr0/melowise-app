from kivy.uix.screenmanager import Screen
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.checkbox import CheckBox
import constants
from .. import values

class CustomCheckBox(CheckBox):
    pass

class CustomBoxLayout(RecycleBoxLayout):
    def compute_layout(self, data, flags):
        pass

        
class IntervalSettingsScreen(Screen):

    selected_intervals = [
        "Unison",
        "Minor second",
        "Major second",
        "Minor third",
        "Major third",
        "Perfect fourth",
        "Augmented fourth",
        "Diminished fifth",
        "Perfect fifth",
        "Minor sixth",
        "Major sixth",
        "Minor seventh",
        "Major seventh",
        "Octave"
    ]

    def __init__(self, **kwargs):
        super(IntervalSettingsScreen, self).__init__(**kwargs)

    def select_intervals(self, instance, value, text):
        if text == 'Select/Unselect all':
            for interval in constants.INTERVALS.keys():
                self.ids[interval].active = value
            return
        if value == True:
            self.selected_intervals.append(text)
        else:
            self.selected_intervals.remove(text)

    def go_to_exercise(self):
        if len(self.selected_intervals) > 0:
            interval_screen = self.manager.get_screen('interval')
            interval_screen.selected_intervals = self.selected_intervals
            values.SELECTED_INTERVALS = self.selected_intervals
            interval_screen.load_question()
            self.manager.current = 'interval'

    def back_to_home(self):
        self.manager.current = 'home'