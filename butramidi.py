#!/usr/local/bin/python

# Imports
from midiutil import MIDIFile
from random import randint
import random

# Variables initialization
additional_tracks = randint (0,4)
print (str (additional_tracks))
MyMIDI = MIDIFile(4+additional_tracks)
channel  = 0
track = 0
time     = 0    # In beats
duration = 0.25    # In beats
tempo    = 120   # In BPM
volume   = 80  # 0-127, as per the MIDI standard

# Functions
def create_beat (degrees):
    resolution = len (degrees) / 4
    MyMIDI.addTempo(track, time, tempo)
    for i, pitch in enumerate(degrees):
        position = time + float(i)/resolution
        if pitch == 0:
            pass
        else:
            MyMIDI.addNote(track, channel, pitch, position, duration, volume)

def create_random_beat ():
    x = randint (36, 52)
    print (str (x))
    degrees  = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (0, 8):
        if bool(random.getrandbits(1)):
            degrees [i] = x
    print (degrees)
    create_beat (degrees)

# Kick
x = 36
degrees  = [x, 0, x, 0, x, 0, x, 0]  # MIDI note number
create_beat (degrees)

# Open Hi-Hat
x = 46
degrees  = [0, x, 0, x, 0, x, 0, x]  # MIDI note number
create_beat (degrees)

# Closed Hi-Hat
x = 42
degrees  = [0, 0, 0, x, 0, 0, 0, x, 0, 0, 0, x, 0, 0, 0, x]  # MIDI note number
create_beat (degrees)

# Clap
x = 39
degrees  = [0, 0, x, 0, 0, 0, x, 0]  # MIDI note number
create_beat (degrees)

# Additional tracks
for i in range (0, additional_tracks):
    create_random_beat ()

# Save file
with open("house-beat.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)