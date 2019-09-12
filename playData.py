from midiWrapper import MIDITime
import pandas as pd
import random

def mag_to_pitch_tuned(type, direction):
    # Where does this data point sit in the domain of your data? (I.E. the min magnitude is 3, the max in 5.6). 
    # In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(1, 6, random.uniform(1,6))

    # Another option: Linear scale, reverse order
    # scale_pct = mymidi.linear_scale_pct(3, 5.7, magnitude, True)

    # Another option: Logarithmic scale, reverse order
    # scale_pct = mymidi.log_scale_pct(3, 5.7, magnitude, True)

    # Pick a range of notes. This allows you to play in a key.
    #c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    c_blues = ['C','Eb','F','G','Bb']
    #c_major = ['C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'B#']
    #Find the note that matches your data point
    note = mymidi.scale_to_note(scale_pct, c_blues)

    #Translate that note to a MIDI pitch
    midi_pitch = mymidi.note_to_midi_pitch(note)

    #make different transportType are in different octaves
    midi_pitch = midi_pitch + relative_octave(type)

    return midi_pitch

def relative_octave(transportType):
    return {
        'train' : 24,
        'regional train' : 12,
        'tram' : 0,
        'bus' : -12,
        'night bus' : -24 
    }[transportType]


def velocity(transportType):
    return {
        'train' : 127,
        'regional train' : 110,
        'tram' : 100,
        'bus' : 80,
        'night bus' : 70
    }[transportType]

def duration(transportType):
    return {
        'train' : 4,
        'regional train' : 4,
        'tram' : 3,
        'bus' : 2,
        'night bus' : 2
    }[transportType]

data = pd.read_csv('final.csv')


# Instantiate the class with a tempo (120bpm is the default) and an output file destination.
mymidi = MIDITime(120, 'myfile.mid')

# Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
# midinotes = [
#     [0, 60, 127, 3],  #At 0 beats (the start), Middle C with velocity 127, for 3 beats
#     [10, 61, 127, 4]  #At 10 beats (12 seconds from start), C#5 with velocity 127, for 4 beats
# ]
start_time = int(data.head(1).sort_column)

#creates only one track, we might add more later
mymidi.create_midi_track(1)

track = 0
channel = 0
note_list = []
for index, row in data.iterrows():
    note = [int(row.sort_column) - start_time + random.uniform(0,.2), 
        int(mag_to_pitch_tuned(row.type, row.arrival_departure)), 
        int(velocity(row.type)), 
        int(duration(row.type))]
    mymidi.add_note(track, channel, note)

    #mymidi.MIDIFile.addPitchWheelEvent(track, channel, int(row.sort_column) - start_time, random.randrange(-8192, 8192))

# Output the .mid file
mymidi.save_file()
