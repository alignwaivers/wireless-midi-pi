"""
Controller side script, using pygame.midi
"""
import sys
import argparse
import pygame
import pygame.midi
from pythonosc import osc_message_builder
from pythonosc import udp_client
  
class Controller():
    """
    Takes MIDI input from a control surface, sends it over
    the network to an OSC server running the DAW-side code.
    
    osc_ip      -->     IP of OSC server on DAW-side
    osc_port    -->     Port of OSC server on DAW-side
    device_id   -->     Device ID of MIDI control service attached to pi 
    """
    def __init__(self, osc_ip, osc_port, device_id):
        pygame.midi.init()
        self.midi_in = pygame.midi.Input(device_id)
        self.osc_client = udp_client.SimpleUDPClient(osc_ip, osc_port)
        
    def run(self):
        while True:
            if self.midi_in.poll():
                midi_events = self.midi_in.read(10)
                ############# SEND VIA OSC ###############
                print('{}'.format(midi_events[0][0][1:3]))
                self.osc_client.send_message("/filter", midi_events[0][0][1:3])
                ##########################################

    def end(self):
        pygame.midi.quit()
      
if __name__ == '__main__':
    #osc client setup
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="192.168.0.36",
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=9997,
        help="The port the OSC server is listening on")
    parser.add_argument("--deviceid", type=int, default=3,
        help="The MIDI device id of the control surface")
    args = parser.parse_args()

    c = Controller(args.ip, args.port, args.deviceid)
    print("MIDI device {} configured to send to {}:{}".
              format(args.deviceid, args.ip, args.port))
    try:
        print("MIDI relay starting")
        c.run()
    except KeyboardInterrupt:
        c.end()
