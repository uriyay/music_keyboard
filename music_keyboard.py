#!/usr/bin/python

import keyboard
import wave
import pygame
import sys

CHUNK = 5000

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
            my_sound.fadeout(200)

def init(path):
    global wf
    pygame.mixer.init()
    wf = wave.open(path, 'rb')

def install():
    keyboard.hook(hook_callback)

def uninstall():
    keyboard.unhook(hook_callback)

if __name__ == '__main__':
    init(sys.argv[1])
    install()
    raw_input()
    uninstall()
