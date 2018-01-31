import sys
import pygame
import pygame.midi
from pygame.locals import *


def main(mode='input', device_id=None):


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
    print 'inputtinnnngg'
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
    if not events:
        pass
    else:
        print events

    del i
    pygame.midi.quit()

if __name__ == '__main__':
    input_main(3) # properly selecting the input device HERE

