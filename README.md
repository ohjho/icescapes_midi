# Climate Change Music
Code we used to create midi files from Climate change data see `/data`

Big thanks to creator of [miditime][1]

To try this yourself, clone this repo.

```
pip install -r requirements.txt
python icescapes.py
```

Within `icescapes.py` many parameters are configurable:
```
# Current settings:
bpm = 120
fname = 'icescape.mid'
sec_per_year = 0.3
base_octave = 4
octave_range = 2
```

To play the midi file, try using [timidity][2]:
```
timidity icescapes.mid
```
[1]: https://github.com/cirlabs/miditime
[2]: https://sourceforge.net/projects/timidity/
