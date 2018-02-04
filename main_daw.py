import argparse
import math
import time
import rtmidi
from pythonosc import dispatcher
from pythonosc import osc_server

def wifimidi_handler(unused_addr, args, volume):
    print("unused_addr: {}".format(unused_addr))
    print("args: {}".format(args))
    print("volume: {}".format(volume))
    print("")

if __name__ == "__main__":
    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()

    if available_ports:
        midiout.open_port(0)
        print("opening port")
    else:
        midiout.open_virtual_port("My virtual output")
        print("opening virtual port")

    # plays an octave chromatically
    #for i in range(12):
    #note_on = [0x90, 60+i, 112] # channel 1, middle C, velocity 112
    #note_off = [0x80, 60+i, 0]
    #midiout.send_message(note_on)
    #time.sleep(0.5)
    #midiout.send_message(note_off)

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
        type=int, default=9997, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/wifimidi", wifimidi_handler)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()