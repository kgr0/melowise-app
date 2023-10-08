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

    level = 1

    selected_chords = [
        {
            'C Major': ['C4', 'E4', 'G4'],
            'D Major': ['D4', 'F#4', 'A4'],
            'E Major': ['E4', 'G#4', 'B4'],
            'A Major': ['A4', 'C#5', 'E5'],
            'G Major': ['G4', 'B4', 'D5'],
            'A Minor': ['A4', 'C5', 'E5'],
            'D Minor': ['D4', 'F4', 'A4'],
            'E Minor': ['E4', 'G4', 'B4'],
            'sample': ['E4', 'G-4', 'B4']
        },
        {
            'F Major 7': ['F4', 'A4', 'C5', 'E5'],
            'B Minor 7': ['B4', 'D5', 'F#5', 'A5'],
            'C Dominant 7': ['C4', 'E4', 'G4', 'B-4'],
            'E Minor 7': ['E4', 'G4', 'B4', 'D5'],
            'G Major 7': ['G4', 'B4', 'D5', 'F#5'],
            'D Dominant 7': ['D4', 'F#4', 'A4', 'C5'],
        },
        {
            'A Minor 9': ['A4', 'C5', 'E5', 'G5', 'B5'],
            'D Major 9': ['D4', 'F#4', 'A4', 'C#5', 'E5'],
            'B Dominant 9': ['B3', 'D#4', 'F#4', 'A4', 'C5'],
            'G Minor 9': ['G3', 'B-3', 'D4', 'F4', 'A4'],
            'F# Diminished 7 ': ['F#4', 'A4', 'C5', 'E-5'],
            'C# Augmented 7': ['C#4', 'E#4', 'G#4', 'B4'],
            'E Major 9': ['E4', 'G#4', 'B4', 'D#5', 'F#5'],
        }
    ]

    dialog = None

    def __init__(self, **kwargs):
        super(ChordSettingsScreen, self).__init__(**kwargs)

    def select_chords(self, instance, text):
        if(text == 'Beginner Level'):
            self.level = 1
        elif(text == 'Intermediate Level'):
            self.level = 2
        else:
            self.level = 3
        # if text == 'Select/Unselect all':
        #     for chord in constants.CHORDS.keys():
        #         self.ids[chord].active = value
        #     return
        # if value == True:
        #     self.selected_chords.append(text)
        # else:
        #     self.selected_chords.remove(text)

    def go_to_exercise(self):
        chord_screen = self.manager.get_screen('chord')
        chord_screen.selected_chords = self.selected_chords[self.level-1]
        values.SELECTED_CHORDS = self.selected_chords[self.level-1]
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