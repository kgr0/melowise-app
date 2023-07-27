from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from db.db import DatabaseHandler
from db.dtos import QuestionDTO
import random
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
from core.sound_generator import generate
import constants

class IntervalScreen(Screen):

    answers = ['1', '2', '3', '4']

    answer_1 = StringProperty('')
    answer_2 = StringProperty('')
    answer_3 = StringProperty('')
    answer_4 = StringProperty('')

    def on_answer_1(self, instance, value):
        self.ids.answer_1.text = value
    def on_answer_2(self, instance, value):
        self.ids.answer_2.text = value
    def on_answer_3(self, instance, value):
        self.ids.answer_3.text = value
    def on_answer_4(self, instance, value):
        self.ids.answer_4.text = value

    def __init__(self, **kwargs):
        super(IntervalScreen, self).__init__(**kwargs)
        self.db = DatabaseHandler()
        self.answers = []
        self.load_question()

    def load_question(self):
        (random_key, random_value) = random.choice(list(constants.INTERVALS.items()))
        self.interval = random_key
        root_note = random.choice(constants.PITCHES) + "4"
        
        self.generate_sound(root_note, random_value)

        self.answers = []
        self.answers = self.generate_answers(self.interval)
        self.answer_1 = self.answers[0];
        self.answer_2 = self.answers[1];
        self.answer_3 = self.answers[2];
        self.answer_4 = self.answers[3];
        pass
    

    def generate_sound(self,root_note, interval ):
        try:
            generate(root_note, interval)
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
            (random_key, random_value) = random.choice(list(constants.INTERVALS.items()))
            if random_key not in answers:
                answers.append(random_key)
        random.shuffle(answers)
        return answers

    def submit_answer(self, user_answer):     
        correct_answer = self.interval
        if user_answer == correct_answer:    
            result_message = "Correct!"     
        else:
            result_message = f'Incorrect! The correct answer is {correct_answer}'

        self.db.save_question(question_dto=QuestionDTO(self.answers[0], self.answers[1], self.answers[2], self.answers[3], correct_answer, user_answer))  # Save the answer in the database

        popup = Popup(title='Result', content=Label(text=result_message), size_hint=(None, None), size=(400, 200))
        popup.open()

        self.load_question()
    
    def back_to_home(self):
        self.manager.current = 'home'