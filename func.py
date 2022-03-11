import sys
from random import randrange, randint

import pygame as pygame
from pygame import KEYDOWN
from pygame.examples.textinput import Screen

from Player.Monster import Monster

tick_rate = 120000
clock = pygame.time.Clock()


def close_window():
    pygame.quit()
    sys.exit()


def battle(player):
    cadre = pygame.image.load('HUD/comba/derrierplan.png')
    Screen.blit(cadre, (0, 0))
    rand = randrange(0, 101)
    if rand <= 50:
        monstrei = pygame.image.load('HUD/comba/monstre/dbat.png')
        monster = Monster("Bat")
        Screen.blit(monstrei, (0, 0))
    else:
        monstrei = pygame.image.load('HUD/comba/monstre/slime.png')
        monster = Monster("Slime")
        Screen.blit(monstrei, (0, 0))
    xzone = randint(50, 820)
    zone = pygame.image.load('HUD/comba/zone mob.png')

    Screen.blit(zone, (xzone, 0))
    xcurs = randint(50, 940)
    curseur = pygame.image.load('HUD/comba/curseur.png')
    Screen.blit(curseur, (xcurs, 0))
    clock.tick(tick_rate)
    pygame.display.update()
    comba_on = True
    sens = True
    speed = 4
    while comba_on:
        if xcurs >= 896:
            sens = False
            speed += 0.5
        elif xcurs <= 0:
            sens = True
            speed += 0.5
        elif speed >= 10:
            speed = 10
        if sens:
            xcurs += speed
        elif not sens:
            xcurs -= speed
        Screen.blit(cadre, (0, 0))
        Screen.blit(zone, (xzone, 0))
        Screen.blit(curseur, (xcurs, 0))
        clock.tick(tick_rate)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # print('noice')
                    # print(xcurs)
                    if xzone - 20 <= xcurs <= xzone + 20:
                        print("Hors zone")
                        pygame.display.update()
                        clock.tick(tick_rate)
                        pygame.display.update()
                        player.attack(monster)
                        if monster.isDead():
                            comba_on = False
                    else:
                        hit = pygame.image.load('HUD/hit.png')
                        monster.attack(player)
                        # print (joueur.pvactuel)
                        Screen.blit(hit, (0, 0))
                        clock.tick(tick_rate)
                        pygame.display.update()
                        Screen.blit(monstrei, (0, 0))
                        Screen.blit(cadre, (0, 0))
                        Screen.blit(zone, (xzone, 0))
                        Screen.blit(curseur, (xcurs, 0))
                        if player.isDead():
                            print("here")
                            pygame.display.update()

                            comba_on = False
                    clock.tick(tick_rate)
                    pygame.display.update()
