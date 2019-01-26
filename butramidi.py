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

# Kick

x = 36
degrees  = [x, 0, x, 0, x, 0, x, 0]  # MIDI note number
track    = 0

MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    position = time + float(i)/2
    if pitch == 0:
        pass
    else:
        MyMIDI.addNote(track, channel, pitch, position, duration, volume)

# Open Hi-Hat

x = 46
degrees  = [0, x, 0, x, 0, x, 0, x]  # MIDI note number
track    = 1

MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    position = time + float(i)/2
    if pitch == 0:
        pass
    else:
        MyMIDI.addNote(track, channel, pitch, position, duration, volume)

# Closed Hi-Hat

x = 42
degrees  = [0, 0, 0, x, 0, 0, 0, x, 0, 0, 0, x, 0, 0, 0, x]  # MIDI note number
track    = 2

MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    position = time + float(i)/4
    if pitch == 0:
        pass
    else:
        MyMIDI.addNote(track, channel, pitch, position, duration, volume) 

# Clap

x = 39
degrees  = [0, 0, x, 0, 0, 0, x, 0]  # MIDI note number
track    = 3

MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    position = time + float(i)/2
    if pitch == 0:
        pass
    else:
        MyMIDI.addNote(track, channel, pitch, position, duration, volume)

# Additional tracks
if additional_tracks == 0:
    pass
elif additional_tracks == 1:
    x = randint (36, 61)
    print (str (x))
    track = 4
    degrees  = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (0, 8):
        if bool(random.getrandbits(1)):
            degrees [i] = x
    MyMIDI.addTempo(track, time, tempo)

    for i, pitch in enumerate(degrees):
        position = time + float(i)/2
        if pitch == 0:
            pass
        else:
            MyMIDI.addNote(track, channel, pitch, position, duration, volume)
else:
    for i in [0, 1]:
        x = randint (36, 61)
        print (str (x))
        track = 4 + i
        degrees  = [0, 0, 0, 0, 0, 0, 0, 0]
        for j in range (0, 8):
            if bool(random.getrandbits(1)):
                degrees [i] = x
        MyMIDI.addTempo(track, time, tempo)

        for j, pitch in enumerate(degrees):
            position = time + float(i)/2
            if pitch == 0:
                pass
            else:
                MyMIDI.addNote(track, channel, pitch, position, duration, volume)
        i += 1
