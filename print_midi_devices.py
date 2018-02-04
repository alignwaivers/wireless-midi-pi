"""
Print all available MIDI devices.
"""
import sys
import pygame
import pygame.midi
import pygame.locals

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

if __name__ == '__main__':
    print_device_info()
