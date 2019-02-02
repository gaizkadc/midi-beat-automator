#!/usr/local/bin/python

# Imports
from midiutil import MIDIFile
from random import randint
import random
import os
from datetime import datetime
import time
import sys

############## FUNCTIONS ##############

# Create a beat
def create_beat (degrees):
    resolution = len (degrees) / 4
    duration = 1/float(resolution)
    MyMIDI.addTempo(track, time, tempo)
    degrees = 2* degrees
    for i, pitch in enumerate(degrees):
        position = time + float(i)/resolution
        if pitch == 0:
            pass
        else:
            MyMIDI.addNote(track, channel, pitch, position, duration, volume)

# Create random beat
def create_random_beat ():
    x = randint (36, 51)
    print ('Pitch: '+str (x))
    degrees  = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (0, 8):
        if bool(random.getrandbits(1)):
            degrees [i] = x
    print (degrees)
    create_beat (degrees)

# Key
def generate_key ():
    key = original_key = [0, 2, 3, 5, 7, 8, 11]
    new_key = [0, 0, 0, 0, 0, 0, 0]

    for i in range (1, 10):
        for j in range (0, len(original_key)):
            new_key [j] = 12*i + original_key [j]
        key = key + new_key
    return key

# Create a melody line
def create_melody (key):
    possible_duration = [ 0.5, 1.0, 2.0]
    total_duration = 0.0
    riff = [[]]

    while True:
        duration = possible_duration [randint(0,2)]
        total_duration += duration
        x = randint (0, 11)
        note = [key[x], duration]
        riff.append (note)
        if 8 - total_duration <= 2:
            break

    x = randint (0, 11)
    duration = 8 - total_duration
    note = [key[x], duration]
    riff.append (note)

    riff = riff [1:]
    print (riff)
    write_riff (riff)

def write_riff (riff):
    position = 0
    for i in range (0, len (riff)):
        duration = riff [i][1]
        pitch = riff [i][0]
        MyMIDI.addNote(track, channel, pitch, position, duration, volume)
        position += duration

############## DRUMS ##############

# Variables initialization
MyMIDI = MIDIFile (7) # number of MIDI tracks
channel  = 0
time     = 0    # In beats
tempo    = int (raw_input ('BPM: '))   # In BPM
style    = str (raw_input ('Style: ')) # So far, 'house' or 'lofi'
volume   = 80  # 0-127, as per the MIDI standard

# Kick
track = 0
x = 36
if style == 'lofi': 
    degrees = [x, 0, 0, 0, 0, x, 0, 0]  # MIDI note number
else:
    degrees = [x, 0, x, 0, x, 0, x, 0]
create_beat (degrees)

# Clap/Snare
track = 1
if style == 'lofi':
    x = 37
    degrees = [0, 0, x, 0, 0, 0, x, 0]
else:
    x = 39
    degrees  = [0, 0, x, 0, 0, 0, x, 0]  # MIDI note number
create_beat (degrees)

# Open Hi-Hat
track = 2
if style == 'house':
    x = 46
    degrees  = [0, x, 0, x, 0, x, 0, x]  # MIDI note number
    create_beat (degrees)

# Closed Hi-Hat
x = 42
if style == 'lofi':
    degrees = [x, x, x, x, x, x, x, x]
else:
    degrees  = [0, 0, 0, x, 0, 0, 0, x, 0, 0, 0, x, 0, 0, 0, x]  # MIDI note number
create_beat (degrees)

# Additional tracks
track = 3
additional_tracks = int (raw_input ('Additional drum tracks: '))
# print ('# additional drum tracks: '+str (additional_tracks))
for i in range (0, additional_tracks):
    create_random_beat ()

############## BASS ##############

original_key = generate_key ()
key = original_key [20:32]
print (key)

# Variables initialization
additional_tracks = int (raw_input ('# bass tracks: '))
# print ('# bass tracks: '+str (additional_tracks))
track = 4

# Tracks
for i in range (0, additional_tracks):
    create_melody (key)

############## LEAD ##############

key = original_key [33:45]
print (key)

# Variables initialization
additional_tracks = int (raw_input ('# lead tracks: '))
# print ('# lead tracks: '+str (additional_tracks))
track = 5

# Tracks
for i in range (0, additional_tracks):
    create_melody (key)

############## EVOLVE ##############

key = original_key [30:37]
print (key)

# Variables initialization
additional_tracks = int (raw_input ('# ambient tracks: '))
# print ('# ambient tracks: '+str (additional_tracks))
track = 6
duration = 2

# Tracks
for i in range (0, additional_tracks):
    riff = [[]]
    total_duration = 0.0
    for j in range (0, 4):
        x = randint (0, 6)
        total_duration += duration
        note = [key[x], duration]
        riff.append (note)
    riff = riff [1:]
    print (riff)
    write_riff (riff)

############## FILE MANAGEMENT ##############

# Save file
now = datetime.now()
timenow = now.strftime('%H%M%S')
datenow = now.strftime('%Y%m%d')
if not os.path.exists('midi'):
    os.mkdir ('midi')
if not os.path.exists('midi/'+datenow):
    os.mkdir ('midi/'+datenow)
midi_path = 'midi/'+datenow+'/random-beat-'+timenow+'.mid'
print (midi_path)
with open(midi_path, 'wb') as output_file:
    MyMIDI.writeFile (output_file)