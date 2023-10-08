from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from db.db import DatabaseHandler
from db.dtos import QuestionDTO
import random
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
from core.sound_generator import generate_chord
import constants
from . import values
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

class ChordScreen(Screen):

    dialog = None
    theme_cls = None

    answers = ['1', '2', '3', '4']

    answer_1 = StringProperty('')
    answer_2 = StringProperty('')
    answer_3 = StringProperty('')
    answer_4 = StringProperty('')

    selected_chords = constants.CHORDS.keys()

    def on_answer_1(self, instance, value):
        self.ids.answer_1.text = value
    def on_answer_2(self, instance, value):
        self.ids.answer_2.text = value
    def on_answer_3(self, instance, value):
        self.ids.answer_3.text = value
    def on_answer_4(self, instance, value):
        self.ids.answer_4.text = value

    def __init__(self, **kwargs):
        super(ChordScreen, self).__init__(**kwargs)
        self.db = DatabaseHandler()
        self.answers = []
        self.theme_cls = MDApp.get_running_app().theme_cls

    def load_question(self):
        random_key = random.choice(list(values.SELECTED_CHORDS.keys()))
        random_value = values.SELECTED_CHORDS[random_key]
        self.chord = random_key
        print(random_key, random_value)
        self.generate_sound(random_value)

        self.answers = []
        self.answers = self.generate_answers(self.chord)
        self.answer_1 = self.answers[0];
        self.answer_2 = self.answers[1];
        self.answer_3 = self.answers[2];
        self.answer_4 = self.answers[3];
        pass
    

    def generate_sound(self, notes):
        try:
            generate_chord(notes)
        except KeyError:
            #TODO fix flat problem
            self.load_question()
        self.sound = SoundLoader.load('././data/sound_1.wav')

    def play_sound(self):
        if self.sound:
            self.sound.play()

    def generate_answers(self,correct_answer):
        answers = [correct_answer]
        while len(answers) < 4:
            random_key = random.choice(list(values.SELECTED_CHORDS.keys()))
            if random_key not in answers:
                answers.append(random_key)
        random.shuffle(answers)
        return answers

    def submit_answer(self, user_answer):     
        correct_answer = self.chord
        if user_answer == correct_answer:
            result_message = "Correct!"     
        else:
            result_message = 'Incorrect! The correct answer is ' + correct_answer

        self.db.save_question(question_dto=QuestionDTO(self.answers[0], self.answers[1], self.answers[2], self.answers[3], correct_answer, user_answer))  # Save the answer in the database

        self.show_alert_dialog(result_message)

    def show_alert_dialog(self, text):
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
            self.load_question()
    
    def back_to_home(self):
        self.manager.current = 'home'