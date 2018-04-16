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

## References
* [Turn your data into sound...][3]
* [The Sound of Data][4]
* [The Sound of Data on YouTube by a Musician Software Engineer][5]

### Further reading
* [Music Information Retrieval using Scikit-learn][6]
* [Music VAE][7]

[1]: https://github.com/cirlabs/miditime
[2]: https://github.com/geofft/timidity
[3]: https://www.revealnews.org/blog/turn-your-data-into-sound-using-our-new-miditime-library/
[4]: https://programminghistorian.org/lessons/sonification
[5]: https://www.youtube.com/watch?v=vb9c_WFMYeI
[6]: https://www.youtube.com/watch?v=oGGVvTgHMHw
[7]: https://magenta.tensorflow.org/music-vae
