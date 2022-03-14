#!/bin/python3

# --|Import
# -|Import Functions
from Utils.func import *

# Main()
pygame.init()
pygame.display.set_caption("Mort d'or")
Clock = pygame.time.Clock()
Clock.tick(Framerate)
game()
