from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from db.db import DatabaseHandler
from db.dtos import QuestionDTO
import random
from kivy.properties import StringProperty

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
        self.db = DatabaseHandler()  # Create an instance of DatabaseHandler with the database name
        self.answers = []
        self.load_question()

    def load_question(self):
        self.sound = SoundLoader.load('././sounds/piano_c.mp3') # Load the sound file
        self.interval = random.choice(self.INTERVALS)

        self.answers = []  # Set the answers to an empty list before generating the new answers
        self.answers = self.generate_answers(self.interval)
        self.answer_1 = self.answers[0];
        self.answer_2 = self.answers[1];
        self.answer_3 = self.answers[2];
        self.answer_4 = self.answers[3];
        pass

    def play_sound(self):
        if self.sound:  # Check if the sound is loaded successfully
            self.sound.play()  # Play the sound

    INTERVALS = ['minor second', 'major second', 'minor third', 'major third',
             'perfect fourth', 'augmented fourth', 'diminished fifth',
             'perfect fifth', 'minor sixth', 'major sixth', 'minor seventh',
             'major seventh', 'perfect octave']

    def generate_answers(self,correct_answer):
        answers = [correct_answer]
        while len(answers) < 4:
            answer = random.choice(self.INTERVALS)
            if answer not in answers:
                answers.append(answer)
        random.shuffle(answers)
        return answers

    def submit_answer(self, user_answer):     
        correct_answer = self.interval  # Replace with your actual correct answer
        if user_answer == correct_answer:    
            result_message = "Correct!"     
        else:
            result_message = "Incorrect!"

        self.db.save_question(question_dto=QuestionDTO(self.answers[0], self.answers[1], self.answers[2], self.answers[3], correct_answer, user_answer))  # Save the answer in the database

        popup = Popup(title='Result', content=Label(text=result_message), size_hint=(None, None), size=(400, 200))
        popup.open()

        self.load_question()
    
    def back_to_home(self):
        self.manager.current = 'home'