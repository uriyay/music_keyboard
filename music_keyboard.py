#!/usr/bin/python

import keyboard
import wave
import pygame
import sys

# just a dummy, really calculated below
CHUNK = 100000

# the higher, the nicer
NICENESS_SCALE = 5

SEC_PER_KEY = 0.15 * NICENESS_SCALE

wf = None

def hook_callback(event):
    print '{}: {} ({})'.format(event.time, event.name, event.scan_code)
    if wf is not None:
        if pygame.mixer.get_busy():
            #TODO: We need to identify that the sound isn't over yet
            print 'wait'
        else:
            my_sound = pygame.mixer.Sound(buffer(wf.readframes(CHUNK)))
            my_sound.play()

def init(path):
    global wf
    pygame.mixer.init()
    wf = wave.open(path, 'rb')

def install():
    keyboard.hook(hook_callback)

def uninstall():
    keyboard.unhook(hook_callback)

if __name__ == '__main__':
    global CHUNK

    init(sys.argv[1])

    CHUNK = int(SEC_PER_KEY * wf.getframerate())
    install()
    raw_input()
    uninstall()
