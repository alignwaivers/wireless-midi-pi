"""
Creates a midi port on the DAW side and plays a chromatic octave.
"""

import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
    print("opening port")
else:
    midiout.open_virtual_port("My virtual output")
    print("opening virtual port")

# plays an octave chromatically
for i in range(12):
    note_on = [0x90, 60+i, 112] # channel 1, middle C, velocity 112
    note_off = [0x80, 60+i, 0]
    midiout.send_message(note_on)
    time.sleep(0.5)
    midiout.send_message(note_off)

del midiout