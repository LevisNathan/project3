import os
import pygame
import sys
from pygame.locals import *

Folder = 'C:/tmp/MediaPLayer/'


def fMaker():
    if not os.path.exists(Folder):
        os.mkdir(Folder, mode=0o777)


def L():
    Li = os.listdir(Folder)
    print(Li)


def Audio():
    pressed = False
    vol = .75
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    #  frequency, size, channels, bufferSize
    pygame.init()  # turn all of pyGame on.
    pygame.mixer.music.load('C:/tmp/MediaPLayer/BMA.wav')
    pygame.display.set_mode((400, 100))
    # screen = pygame.display.set_mode((640, 480))
    # pygame.draw.rect(screen, (255, 0, 0), {300, 75}, 0)
    pygame.display.set_caption("Music Player")
    clock = pygame.time.Clock()
    pygame.mixer.music.play()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        pess = pygame.key.get_pressed()
        if pess[K_1]:
            vol += .05
            print(pygame.mixer.music.get_volume())
        if pess[K_2]:
            vol -= .05
            print(pygame.mixer.music.get_volume())

        if pess[K_DELETE]:
            pygame.mixer.music.pause()

        if pess[K_BACKSPACE]:
            pygame.mixer.music.unpause()

        if pess[K_INSERT]:
            pygame.quit()
            sys.exit(0)
        pygame.mixer.music.set_volume(vol)
        clock.tick(10)

fMaker()
L()
Audio()
pygame.quit()
sys.exit(0)
