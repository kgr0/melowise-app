#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.io import wavfile
from core import utils
import music21

# import random

# notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
# intervals = {
#     'P1': 0, 'm2': 1, 'M2': 2, 'm3': 3, 'M3': 4,
#     'P4': 5, 'A4': 6, 'd5': 6, 'P5': 7, 'A5': 8,
#     'm6': 8, 'M6': 9, 'm7': 10, 'M7': 11, 'P8': 12
# }

# def generate_interval(root_note, interval_name):
#     root_index = notes.index(root_note)
#     interval_semitones = intervals[interval_name]
#     interval_index = (root_index + interval_semitones) % len(notes)
#     interval_note = notes[interval_index]
#     return interval_note


def build_interval(root_note, interval_name):
    # Create a pitch object for the root note
    
    root_pitch = music21.pitch.Pitch(root_note)

    # Create an interval object based on the interval name
    interval = music21.interval.Interval(interval_name)

    # Calculate the pitch of the second note based on the interval and root pitch
    second_pitch = interval.transposePitch(root_pitch)

    # Return the interval as a tuple containing the root note and second note

    return str(second_pitch)

def generate(root_note, interval):
    second_note = build_interval(root_note, interval)



    right_hand_notes = [root_note, second_note]
    right_hand_duration = [1, 1]

    factor = [0.68, 0.26, 0.03, 0.  , 0.03]
    length = [0.01, 0.6, 0.29, 0.1]
    decay = [0.05,0.02,0.005,0.1]
    sustain_level = 0.1



    right_hand = utils.get_song_data(right_hand_notes, right_hand_duration, 2,
                                    factor, length, decay, sustain_level)
    factor = [0.73, 0.16, 0.06, 0.01, 0.02, 0.01  , 0.01]
    length = [0.01, 0.29, 0.6, 0.1]
    decay = [0.05,0.02,0.005,0.1]

    data = right_hand
    data = data * (4096/np.max(data))
    wavfile.write('./data/sound_1.wav', 44100, data.astype(np.int16))