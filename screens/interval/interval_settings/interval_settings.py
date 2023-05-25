from kivy.uix.screenmanager import Screen
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.checkbox import CheckBox


class CustomCheckBox(CheckBox):
    pass

class CustomBoxLayout(RecycleBoxLayout):
    def compute_layout(self, data, flags):
        pass

        
class IntervalSettingsScreen(Screen):

    checkbox_data = [
    {"text": "Checkbox 1", "active": False},
    {"text": "Checkbox 2", "active": True},
    {"text": "Checkbox 3", "active": False},
    # Add more checkbox data as needed
    ]

    def __init__(self, **kwargs):
        super(IntervalSettingsScreen, self).__init__(**kwargs)

    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")

    def go_to_exercise(self):
        self.manager.current = 'interval'

    def back_to_home(self):
        self.manager.current = 'home'