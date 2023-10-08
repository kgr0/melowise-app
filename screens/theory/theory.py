from collections import Counter
from kivy.uix.screenmanager import Screen
from db.db import DatabaseHandler
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
import numpy as np
import constants
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

class TheoryScreen(Screen, FloatLayout):
    def __init__(self, **kwargs):
        super(TheoryScreen, self).__init__(**kwargs)

    dialog = None
    
    def show_instruction(self):
        if not self.dialog:
            text='Relative pitch is the ability to determine the relationships between pitches without reference to a fixed pitch. In other words, if you have relative pitch, you might be able to recognize that a series of notes forms a particular melody or that two notes are a certain interval apart, even if you cant immediately identify the absolute pitches of those notes without a reference tone. \n\n For instance, someone with good relative pitch might hear a series of notes and recognize that the sequence corresponds to the intervals of the opening of "Happy Birthday," even if they cant immediately say that the starting note is a C or an F or any other specific pitch.\n\nRelative pitch is contrasted with absolute pitch (often called perfect pitch), which is the ability to identify or produce a given pitch without any external reference. For example, someone with absolute pitch might hear a note and immediately recognize it as an A-flat without having to compare it to another note.\n\nMany musicians develop relative pitch through training and practice, particularly those who regularly play in ensemble settings or those who practice ear training exercises. It is a valuable skill for understanding and reproducing musical relationships, harmonies, and melodies.'
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

