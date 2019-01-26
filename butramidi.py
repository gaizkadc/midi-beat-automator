#!/usr/local/bin/python

from midiutil import MIDIFile
from random import randint
import random

additional_tracks = randint (0,2)
print (str (additional_tracks))
MyMIDI = MIDIFile(4+additional_tracks)

channel  = 0
time     = 0    # In beats
duration = 0.25    # In beats
tempo    = 120   # In BPM
volume   = 80  # 0-127, as per the MIDI standard

def create_beat (degrees, track):
    resolution = len (degrees) / 4
    MyMIDI.addTempo(track, time, tempo)
    for i, pitch in enumerate(degrees):
        position = time + float(i)/resolution
        if pitch == 0:
            pass
        else:
            MyMIDI.addNote(track, channel, pitch, position, duration, volume)

def create_random_beat (track):
    x = randint (36, 61)
    print (str (x))
    degrees  = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (0, 8):
        if bool(random.getrandbits(1)):
            degrees [i] = x
    print (degrees)
    create_beat (degrees, track)

# Kick

x = 36
degrees  = [x, 0, x, 0, x, 0, x, 0]  # MIDI note number
track    = 0
create_beat (degrees, track)

# Open Hi-Hat

x = 46
degrees  = [0, x, 0, x, 0, x, 0, x]  # MIDI note number
track    = 1

create_beat (degrees, track)

# Closed Hi-Hat

x = 42
degrees  = [0, 0, 0, x, 0, 0, 0, x, 0, 0, 0, x, 0, 0, 0, x]  # MIDI note number
track    = 2

create_beat (degrees, track)

# Clap

x = 39
degrees  = [0, 0, x, 0, 0, 0, x, 0]  # MIDI note number
track    = 3

create_beat (degrees, track)

# Additional tracks
if additional_tracks == 0:
    pass
elif additional_tracks == 1:
    create_random_beat (4)
else:
    for i in [0, 1]:
        create_random_beat (4+i)

with open("house-beat.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)