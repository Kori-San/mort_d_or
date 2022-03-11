# utils
import pygame
from time import *
from random import *
from tkinter import *
import math
import os
import collections
import sys


# mort-d'or
from func import *


def close_window():
    pygame.quit()
    sys.exit()


def retrieve_input():
    inputValue = textBox.get("1.0", "end-1c")
    print(inputValue)


# Main()
pygame.init()

resolution_x = 1000
resolution_y = 800
tick_rate = 120000
useless_wait_var = 1
screen = pygame.display.set_mode(
    (resolution_x, resolution_y), pygame.DOUBLEBUF)
screen.set_alpha(None)
pygame.display.set_caption("Mort d'or")
clock = pygame.time.Clock()
while (1):
    tavern = pygame.image.load("HUD/tavern.png").convert_alpha()
    man = pygame.image.load("HUD/man.png").convert_alpha()
    screen.blit(tavern, (0, 0))
    screen.blit(man, (300, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window()
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if 300 < x < 520 and 250 < y < 700:
"""                 root = Tk()
                textBox = Text(root, height=2, width=10)
                textBox.pack()
                buttonCommit = Button(root, height=1, width=10, text="Commit",
                                      command=lambda: retrieve_input()) """
                print("Ouch")
    pygame.display.update()
