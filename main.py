"""
Controller side script, using pygame.midi
"""
import sys
import pygame
import pygame.midi
        

if __name__ == '__main__':
    pygame.midi.init()
    
    device_id = int(sys.argv[1]) # device id from first cl argument
    if device_id is None:
        input_id = pygame.midi.get_default_input_id()
    else:
        input_id =  device_id
    print("using input_id :{}:".format(input_id))
    i = pygame.midi.Input(input_id)

    try:
        while True:
            if i.poll():
                midi_events = i.read(10)
                ############# SEND VIA OSC ###############
                print('{}'.format(midi_events))
                ##########################################
    except KeyboardInterrupt:
        del i
        pygame.midi.quit()
