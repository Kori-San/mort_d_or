# --|Import
# -|Import Functions
import sys
from random import randrange, randint
import pygame as pygame

# -|Import Classes
from Player.Player import Player
from Player.Monster import Monster
from Player.Wizard import Wizard
from Player.Warrior import Warrior
from Player.Ranger import Ranger

# --|Vars
# -|Parameters
Resolution_X = 1000
Resolution_Y = 800
Framerate = 120

# -|Screen
Screen = pygame.display.set_mode(
    (Resolution_X, Resolution_Y), pygame.DOUBLEBUF)
Screen.set_alpha(None)

# -|PyGame
Clock = pygame.time.Clock()
useless_wait_var = 1

# --|Funcs


def refresh_tavern():
    tavern = pygame.image.load("HUD/tavern.png").convert_alpha()
    man = pygame.image.load("HUD/man.png").convert_alpha()
    Screen.blit(tavern, (0, 0))
    Screen.blit(man, (300, 250))
    pygame.display.update()


def game():
    # -|game() : Game Loop
    while (1):
        refresh_tavern()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_window()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 300 < x < 520 and 250 < y < 700:
                    print("Touch : L'homme mystérieux")
                    player = Warrior("Jenkins", "LEROYYYYYYYYYYYYY JENKINS")
                    battle(player)


def close_window():
    # -|close_window() : Close Window
    pygame.quit()
    sys.exit()


def battle(player):
    # -|battle(player) : Declare une bataille (player V.S un Monstre généré)
    Fight_BG = pygame.image.load('HUD/comba/derrierplan.png')
    Fight_Zone_FG = pygame.image.load('HUD/comba/zone mob.png')
    Fight_Zone_X_Axis = randint(50, 820)
    Fight_Cursor_FG = pygame.image.load('HUD/comba/curseur.png')
    Fight_Cursor_X_Axis = randint(50, 940)
    # Methode à écrire pour généré un monstre et rajouter le path en attribut
    # Monster_Rand = randrange(0, 101)
    # if Monster_Rand <= 50:
    #     Monster_Sprite = pygame.image.load('HUD/comba/monstre/dbat.png')
    #     Fighting_Monster = Monster("Bat")
    # else:
    #     Monster_Sprite = pygame.image.load('HUD/comba/monstre/slime.png')
    #     Fighting_Monster = Monster("Slime")
    # Fin Methode
    Fighting_Monster = Monster('Monster')
    Fighting_Monster.generate()
    Monster_Sprite = pygame.image.load(Fighting_Monster.sprite)
    Screen.blit(Monster_Sprite, (0, 0))
    Fight = True
    Direction = True
    Speed = 6
    Acceleration = 1
    while Fight:
        # Check Speed
        if Speed >= 10:
            Speed = 10
        # Direction Management
        if Direction:
            Fight_Cursor_X_Axis += Speed
            if Fight_Cursor_X_Axis >= 896:
                Speed += Acceleration
                Direction = False
        elif not Direction:
            Fight_Cursor_X_Axis -= Speed
            if Fight_Cursor_X_Axis <= 0:
                Speed += Acceleration
                Direction = True
        Screen.blit(Fight_BG, (0, 0))
        Screen.blit(Fight_Zone_FG, (Fight_Zone_X_Axis, 0))
        Screen.blit(Fight_Cursor_FG, (Fight_Cursor_X_Axis, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_window()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if Fight_Zone_X_Axis - 20 <= Fight_Cursor_X_Axis <= Fight_Zone_X_Axis + 20:
                        print("InZeZone")
                        player.attack(Fighting_Monster)
                        if Fighting_Monster.isDead():
                            Fight = False
                    else:
                        print("NotInZeZone")
                        Screen.blit(pygame.image.load('HUD/hit.png'), (0, 0))
                        Screen.blit(Monster_Sprite, (0, 0))
                        Fighting_Monster.attack(player)
                        if player.isDead():
                            Fight = False
