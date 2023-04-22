from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from db.db import DatabaseHandler

class IntervalScreen(Screen):
    def __init__(self, **kwargs):
        super(IntervalScreen, self).__init__(**kwargs)
        self.sound = SoundLoader.load('././sounds/piano_c.mp3') # Load the sound file
        self.db = DatabaseHandler()  # Create an instance of DatabaseHandler with the database name

    def play_sound(self):
        if self.sound:  # Check if the sound is loaded successfully
            self.sound.play()  # Play the sound

    def submit_answer(self, answer):
        question_id = 1
        correct_answer = "Option 3"  # Replace with your actual correct answer
        if answer == correct_answer:
            answer = True
            result_message = "Correct!"
        else:
            answer = False
            result_message = "Incorrect!"

        self.db.save_answer(question_id, answer)  # Save the answer in the database

        popup = Popup(title='Result', content=Label(text=result_message), size_hint=(None, None), size=(400, 200))
        popup.open()
    
    def back_to_home(self):
        self.manager.current = 'home'