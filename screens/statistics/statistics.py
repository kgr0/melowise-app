from collections import Counter
from kivy.uix.screenmanager import Screen
from db.db import DatabaseHandler
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivy
from kivy.uix.floatlayout import FloatLayout
import numpy as np
import constants

class StatisticsScreen(Screen, FloatLayout):
    def __init__(self, **kwargs):
        super(StatisticsScreen, self).__init__(**kwargs)
        self.db = DatabaseHandler()

        self.update_chart()

    def back_to_home(self):
        self.manager.current = 'home'

    def get_answers_from_db(self):
        self.db = DatabaseHandler() 
        list = self.db.get_all_questions()
        return list

    def on_pre_enter(self):
        self.update_chart()

    def update_chart(self):
        answers = self.get_answers_from_db()
        if(len(answers) == 0):
            return
        labels = ['Correct', 'Incorrect']
        values = [
            len([obj for obj in answers if obj.user_answer == obj.correct_answer]),
            len([obj for obj in answers if obj.user_answer != obj.correct_answer])
        ]       
        colors = ['#A4AA7E', '#D07F89']
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'color':"w"})
        ax.set_title('Pie Chart')
        chart_widget = FigureCanvasKivy(fig)
        chart_container = self.ids.pie_chart_container
        chart_container.clear_widgets()
        chart_container.add_widget(chart_widget)


        #print(list(set(question.correct_answer for question in answers)))
        #intervals = list(set(question.correct_answer for question in answers))

        intervals = list(constants.INTERVALS.keys())
        correct_answers, wrong_answers = np.zeros(len(intervals)),  np.zeros(len(intervals))

        correct_answers = [len([ answer for answer in answers if answer.correct_answer == interval and answer.correct_answer == answer.user_answer]) for interval in intervals]
        wrong_answers = [len([ answer for answer in answers if answer.correct_answer == interval and answer.correct_answer != answer.user_answer]) for interval in intervals]

        penguin_means = {
            'Correct': correct_answers,
            'Wrong': wrong_answers,
        }

        x = np.arange(len(intervals))  # the label locations
        width = 0.25  # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')

        for attribute, measurement in penguin_means.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        #ax.set_ylabel('Length (mm)')
        #ax.set_title('Penguin attributes by intervals')
        ax.set_xticks(x + width, intervals)
        ax.set_ylim(0, max(max(correct_answers), max(wrong_answers))+2)

        bars_chart_widget = FigureCanvasKivy(fig)
        bars_chart_container = self.ids.bars_chart_container
        bars_chart_container.clear_widgets()
        bars_chart_container.add_widget(bars_chart_widget)
