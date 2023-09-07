from kivy.uix.screenmanager import Screen
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.checkbox import CheckBox
import constants
from .. import values
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

class CustomCheckBox(CheckBox):
    pass

class CustomBoxLayout(RecycleBoxLayout):
    def compute_layout(self, data, flags):
        pass

        
class ChordSettingsScreen(Screen):

    selected_chords = [
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

    dialog = None

    def __init__(self, **kwargs):
        super(ChordSettingsScreen, self).__init__(**kwargs)

    def select_chords(self, instance, value, text):
        if text == 'Select/Unselect all':
            for chord in constants.CHORDS.keys():
                self.ids[chord].active = value
            return
        if value == True:
            self.selected_chords.append(text)
        else:
            self.selected_chords.remove(text)

    def go_to_exercise(self):
        if len(self.selected_chords) > 0:
            chord_screen = self.manager.get_screen('chord')
            chord_screen.selected_chords = self.selected_chords
            values.SELECTED_CHORDS = self.selected_chords
            chord_screen.load_question()
            self.manager.current = 'chord'

    def back_to_home(self):
        self.manager.current = 'home'

    def show_instruction(self):
        if not self.dialog:
            text='In this exercise, you can train your ears to recognize musical intervals. Intervals are the building blocks of music and understanding them is essential for any musician.\n\nOnce the exercise starts, you can click on bytton and you will hear two notes played in succession.Your task is to identify the interval between these two notes.\n\nAfter making your selection, the correct answer will be displayed. Use this feedback to learn and improve. Remember, it is okay to make mistakes; they are a part of the learning process! \n\nYou can end the exercise at any point by selecting the Back option. Your progress and score will be saved, and you can review them in the Statistics section.'
            self.dialog = MDDialog(
                text='[color=183e50]' + text + '[/color]',
                radius=[20, 7, 20, 7],
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color='#8d3448',
                        on_release=self.close_dialog,
                    )
                ],
            )
        self.dialog.open()

    def close_dialog(self, instance):
        if self.dialog:
            self.dialog.dismiss()