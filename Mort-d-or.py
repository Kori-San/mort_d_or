#!/bin/python3

from multiprocessing.connection import wait
from Utils.func import *


def close_window():
    pygame.quit()
    sys.exit()


# Main()
pygame.init()
pygame.display.set_caption("Mort d'or")
Clock = pygame.time.Clock()
Clock.tick(Framerate)
game()
