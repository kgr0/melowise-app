from collections import Counter
from kivy.uix.screenmanager import Screen
from db.db import DatabaseHandler
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
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
        colors = ['#7abd7e', '#ff6961']
        explode = (0.05,0.05)
        fig, ax = plt.subplots()

        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', pctdistance=0.85, startangle=90, explode = explode)

        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        #ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%')
        
        #ax.set_title('Pie Chart')
        chart_widget = FigureCanvasKivy(fig)
        chart_container = self.ids.pie_chart_container
        chart_container.clear_widgets()

        # pie_chart_label = Label(
        #     text= labels[0] + ' ' + str(round((values[0]/len(answers))*100))+'% ' + labels[1] + ' ' + str(100 - round((values[0]/len(answers))*100)) + '%',
        #     font_size=20,
        #     color=(.788, .521, .517, 1),
        #     halign='center',
        #     valign='middle',
        #     size_hint=(None, None), 
        #     size=(300, 44)
        # )
        # chart_container.add_widget(pie_chart_label)
        chart_container.add_widget(chart_widget)
        
        

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

        fig2, ax2 = plt.subplots(layout='constrained')


        colors = {
            'Correct': '#7abd7e',  # This is green in hex
            'Wrong': '#ff6961'     # This is red in hex
        }
        for attribute, measurement in penguin_means.items():
            offset = width * multiplier
            rects = ax2.bar(x + offset, measurement, width, label=attribute, color=colors[attribute])
            ax2.bar_label(rects, padding=3)
            multiplier += 1
        
        formatted_intervals = [label.replace(" ", "\n") for label in intervals]
        ax2.set_xticks(x + width, formatted_intervals)
        ax2.set_ylim(0, max(max(correct_answers), max(wrong_answers))+2)

        bars_chart_widget = FigureCanvasKivy(fig2)
        bars_chart_container = self.ids.bars_chart_container
        bars_chart_container.clear_widgets()
        bars_chart_container.add_widget(bars_chart_widget)
