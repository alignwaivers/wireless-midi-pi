import sys
import pygame
import pygame.midi
from pygame.locals import *
import OSC
from OSC import OSCBundle
import time
import math

client = OSC.OSCClient()
send_address = '10.0.0.7', 9997
recieve_address = '127.0.0.1', 9001
client.connect( send_address )



def makeMsg(address, content):
    msg = OSC.OSCMessage()
    msg.setAddress(address)
    msg.append(content)
    return msg



def main(mode='input', device_id=None):
    """Run a Midi example

    Arguments:
    mode - if 'output' run a midi keyboard output example
              'input' run a midi event logger input example
              'list' list available midi devices
           (default 'output')
    device_id - midi device number; if None then use the default midi input or
                output device for the system

    """

    if mode == 'input':
        print 'input'
        input_main(device_id)
    elif mode == 'output':
        output_main(device_id)
    elif mode == 'list':
        print 'list'
        print_device_info()
    else:
        raise ValueError("Unknown mode option '%s'" % mode)


def print_device_info():
    pygame.midi.init()
    _print_device_info()
    pygame.midi.quit()

def _print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
               (i, interf, name, opened, in_out))
        



def input_main(device_id = None): #default is none
    pygame.init()
    pygame.fastevent.init()
    event_get = pygame.fastevent.get
    event_post = pygame.fastevent.post

    pygame.midi.init()

    _print_device_info()


    if device_id is None:
        input_id = pygame.midi.get_default_input_id()
    else:
        input_id =  device_id
        print 'input_id = '
    print ("using input_id :%s:" % input_id)
    i = pygame.midi.Input( input_id )
    print i

    
    going = True
    while going:
        events = event_get()
##        if not events:
##            pass
##        else:
##            print 'hihihihihih', events[0]

            


##            
##        for e in events:
##            if e.type in [QUIT]:
##                going = False
##            if e.type in [KEYDOWN]:
##                going = False
##            if e.type in [pygame.midi.MIDIIN]:
##                print (e)
##
        if i.poll():
            midi_events = i.read(10)
            nte, vel = midi_events[0][0][1], midi_events[0][0][2]
            print nte, vel
            msg1 = makeMsg("/1", [nte,vel] )
            client.send(msg1)

            
            
            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

            for m_e in midi_evs:
                event_post( m_e )
                
           


    del i
    pygame.midi.quit()

if __name__ == '__main__':
    input_main(3)
##
##    try:
##        device_id = int( sys.argv[-1] )
##    except:
##        device_id = None
##
##    if "--input" in sys.argv or "-i" in sys.argv:
##
##        input_main(device_id)
##
##    elif "--output" in sys.argv or "-o" in sys.argv:
##        output_main(device_id)
##    elif "--list" in sys.argv or "-l" in sys.argv:
##        print_device_info()
##    else:
##        print 'usaginystic'
##        usage()
##
