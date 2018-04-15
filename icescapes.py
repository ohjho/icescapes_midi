from miditime.miditime import MIDITime
import pandas as pd

# Instantiate the class with a tempo (120bpm is the default) and an output file destination.
bpm = 120
fname = 'icescape.mid'
sec_per_year = 0.3
base_octave = 4
octave_range = 2
mymidi = MIDITime(bpm, fname, sec_per_year, base_octave, octave_range)

# Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
# Example Note list
midinotes = [
    [0, 60, 127, 3],  #At 0 beats (the start), Middle C with velocity 127, for 3 beats
    [10, 61, 127, 4]  #At 10 beats (12 seconds from start), C#5 with velocity 127, for 4 beats
]

# test data
# API_KEY = "d2497755fff294019d2402ba2ad8dbcd"
# GEO = "40.712784,-74.005941"
# call = "https://api.forecast.io/forecast/{0}/{1}"
# weather = call.format(API_KEY, GEO)
# r = requests.get(weather)
# daily

carbon_data = pd.Series.from_csv("data/GlobalCarbonEmissions.csv", header = 1, parse_dates = True)
#carbon_data = [float(carbon_data[i].replace(',','')) for i in range(carbon_data.size)]
for i in range(carbon_data.size):
    carbon_data[i] = carbon_data[i].replace(',','')
carbon_data = pd.to_numeric(carbon_data)

my_data = []
for i in range(carbon_data.size):
    my_data.append({'event_date' : carbon_data.index[i],'magnitude' : carbon_data[i]})

my_data_chg = []
my_data_print = []
for i in range(1, carbon_data.size):
    my_data_chg.append({'event_date' : carbon_data.index[i],'magnitude' : (carbon_data[i]/ carbon_data[i-1] -1) * 100 })
    my_data_print.append((carbon_data[i]/ carbon_data[i-1] -1) * 100)

my_data = my_data_chg[-100:]
my_data_print = my_data_print[1:]
print(max(my_data_print),min(my_data_print))
# Data should look like this
# my_data = [
#     {'event_date': <datetime object>, 'magnitude': 3.4},
#     {'event_date': <datetime object>, 'magnitude': 3.2},
#     {'event_date': <datetime object>, 'magnitude': 3.6},
#     {'event_date': <datetime object>, 'magnitude': 3.0},
#     {'event_date': <datetime object>, 'magnitude': 5.6},
#     {'event_date': <datetime object>, 'magnitude': 4.0}
# ]

# Convert date/time into an integer
my_data_epoched = [{'days_since_epoch': mymidi.days_since_epoch(d['event_date']), 'magnitude': d['magnitude']} for d in my_data]

# Convert integer date/time into something reasonable for a song
my_data_timed = [{'beat': mymidi.beat(d['days_since_epoch']), 'magnitude': d['magnitude']} for d in my_data_epoched]

start_time = my_data_timed[0]['beat']

def mag_to_pitch_tuned(magnitude):
    # Where does this data point sit in the domain of your data? (I.E. the min magnitude is 3, the max in 5.6). In this case the optional 'True' means the scale is reversed, so the highest value will return the lowest percentage.
    scale_pct = mymidi.linear_scale_pct(-17, 34, magnitude)

    # Another option: Linear scale, reverse order
    # scale_pct = mymidi.linear_scale_pct(3, 5.7, magnitude, True)

    # Another option: Logarithmic scale, reverse order
    #scale_pct = mymidi.log_scale_pct(3, 10000, magnitude, True)

    # Pick a range of notes. This allows you to play in a key.
    c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

    #Find the note that matches your data point
    note = mymidi.scale_to_note(scale_pct, c_major)

    #Translate that note to a MIDI pitch
    midi_pitch = mymidi.note_to_midi_pitch(note)

    return midi_pitch

note_list = []

for d in my_data_timed:
    note_list.append([
        d['beat'] - start_time,
        mag_to_pitch_tuned(d['magnitude']),
        100,  # velocity
        1  # duration, in beats
    ])

# Add a track with those notes
mymidi.add_track(note_list)

# Output the .mid file
mymidi.save_midi()
