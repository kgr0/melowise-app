from kivy.uix.screenmanager import Screen
from db.db import DatabaseHandler
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivy
from kivy.uix.floatlayout import FloatLayout

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
        labels = ['Correct', 'Incorrect']
        values = [
            len([obj for obj in answers if obj.user_answer == obj.correct_answer]),
            len([obj for obj in answers if obj.user_answer != obj.correct_answer])
        ]       
        print(values)
        colors = ['#5D9C59', '#DF2E38']
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'color':"w"})
        ax.set_title('Pie Chart')
        chart_widget = FigureCanvasKivy(fig)
        chart_container = self.ids.chart_container
        chart_container.clear_widgets()
        chart_container.add_widget(chart_widget)
