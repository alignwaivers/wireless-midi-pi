import argparse
import math
import time
import rtmidi
from pythonosc import dispatcher
from pythonosc import osc_server

def wifimidi_handler(unused_addr, args, volume):
    message = None
    if volume == 0:
        message = [0x80, args[0], volume]
    else:
        message = [0x90, args[0], volume]
    args[1].send_message(message)

if __name__ == "__main__":
    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()

    if available_ports:
        midiout.open_port(0)
        print("opening port")
    else:
        midiout.open_virtual_port("My virtual output")
        print("opening virtual port")

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
        type=int, default=9997, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/wifimidi", wifimidi_handler, midiout)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()