import sys
import pygame
import pygame.midi
import pygame.locals


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
        print('input')
        input_main(device_id)
    elif mode == 'output':
        output_main(device_id)
    elif mode == 'list':
        print('list')
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
        print("{}i: interface :{}:, name :{}:, opened :{}:  {}".format(i, interf, name, opened, in_out))




def input_main(device_id = None): #default is none
    print('inputtinnnngg')
    pygame.init()
    pygame.fastevent.init()
    event_get = pygame.fastevent.get
    event_post = pygame.fastevent.post

    pygame.midi.init()
    
    if device_id is None:
        input_id = pygame.midi.get_default_input_id()
    else:
        input_id =  device_id
        print('input_id = ')
    print("using input_id :%s:" % input_id)
    i = pygame.midi.Input( input_id )
    print("{}".format(i))


    going = True
    while going:
        if i.poll():
            midi_events = i.read(10)
            print('midi\n{}'.format(midi_events))

    del i
    pygame.midi.quit()

if __name__ == '__main__':
    print_device_info()
    input_main(int(sys.argv[1])) # properly selecting the input device HERE

