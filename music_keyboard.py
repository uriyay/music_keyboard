#!/usr/bin/python

import keyboard
import wave
import pygame
import sys

# just a dummy, really calculated below
CHUNK = 100000

# the higher, the nicer
NICENESS_SCALE = 0.3

SEC_PER_KEY = 0.15 * NICENESS_SCALE

wf = None

g_need_to_play = 0

def hook_callback(event):
    global g_need_to_play

    if wf is not None:
	g_need_to_play += CHUNK	
        if not pygame.mixer.get_busy():
            my_sound = pygame.mixer.Sound(buffer(wf.readframes(g_need_to_play)))
            my_sound.play()
	    g_need_to_play = 0

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

    CHUNK = int(SEC_PER_KEY * wf.getframerate())
    install()
    raw_input()
    uninstall()
