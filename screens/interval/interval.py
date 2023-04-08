from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class IntervalScreen(Screen):
    def __init__(self, **kwargs):
        super(IntervalScreen, self).__init__(**kwargs)
        self.sound = SoundLoader.load('././sounds/piano_c.mp3') # Load the sound file

    def play_sound(self):
        if self.sound:  # Check if the sound is loaded successfully
            self.sound.play()  # Play the sound

    def submit_answer(self, answer):
        correct_answer = "Option 3"  # Replace with your actual correct answer
        if answer == correct_answer:
            result_message = "Correct!"
        else:
            result_message = "Incorrect!"

        popup = Popup(title='Result', content=Label(text=result_message), size_hint=(None, None), size=(400, 200))
        popup.open()