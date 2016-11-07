import os
import pygame


Folder = 'C:/tmp/MediaPLayer/'


def fMaker():
    if not os.path.exists(Folder):
        os.mkdir(Folder, mode=0o777)


def L():
    Li = os.listdir(Folder)
    print(Li)


def Audio():
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    #  frequency, size, channels, bufferSize
    pygame.init()  # turn all of pyGame on.
    pygame.mixer.music.load('C:/tmp/MediaPLayer/BMA.wav')
    pygame.display.set_mode((200, 100))
    clock = pygame.time.Clock()
    pygame.mixer.music.play()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)


fMaker()
L()
Audio()

