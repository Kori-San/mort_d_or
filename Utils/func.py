# --|Import
# -|Import Functions
from re import L
from select import select
import sys
from random import randrange, randint
import pygame as pygame
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

# -|Import Classes
from Player.Monster import Monster
from Player.Wizard import Wizard
from Player.Warrior import Warrior
from Player.Ranger import Ranger

# --|Vars
# -|Parameters
Resolution_X = 1000
Resolution_Y = 800
Framerate = 120
l = ["Jenkins", "LEROYYYYYYYYYY JENKINS", "Warrior"]

# -|Screen
Screen = pygame.display.set_mode(
    (Resolution_X, Resolution_Y), pygame.DOUBLEBUF)
Screen.set_alpha(None)

# -|PyGame
Clock = pygame.time.Clock()

# -|Tkinter
master = tk.Tk()
name = tk.Entry(master)
desc = tk.Entry(master)
s_class = tk.StringVar(master)
sel_class = tk.Entry(master, textvariable=s_class)

# --|Funcs


def getting():
    print(name.get())
    if name.get() != "":
        l[0] = name.get()
    print(desc.get())
    if desc.get() != "":
        l[1] = desc.get()
    print(sel_class.get())
    if sel_class.get() != "":
        l[2] = sel_class.get()
    print(l)
    master.destroy()


def grave(player):
    refresh_tavern()
    hit_hud = pygame.image.load("graphics/hit.png").convert_alpha()
    Screen.blit(hit_hud, (0, 0))
    skull = pygame.image.load("graphics/skull.png").convert_alpha()
    Screen.blit(skull, (0, 0))
    display_score(player)
    pygame.time.wait(3*1000)
    # Number of seconds * 1000 to match milliseconds requierements
    close_window()


def select_char():
    master.title("Select your Character!")
    tk.Label(master, text="Nom").pack()
    name.pack()
    tk.Label(master, text="Description").pack()
    desc.pack()
    s_class.set("Warrior")  # Default Value
    class_box = tk.OptionMenu(master, s_class, "Warrior", "Wizard", "Ranger")
    class_box.pack()
    tk.Button(master, text="Set", command=getting).pack()
    tk.mainloop()


def display_score(player):
    font = pygame.font.SysFont("Myriad Pro", 72)
    text = font.render(str(player.score), True, (255, 255, 255))
    Screen.blit(text, (45, 25))
    pygame.display.update()


def refresh_tavern():
    pygame.display.flip()
    tavern = pygame.image.load("graphics/tavern.png").convert_alpha()
    man = pygame.image.load("graphics/man.png").convert_alpha()
    Screen.blit(tavern, (0, 0))
    Screen.blit(man, (300, 250))
    pygame.display.update()


def game():
    # -|game() : Game Loop
    select_char()
    if l[2] == "Warrior":
        player = Warrior(l[0], l[1])
    elif l[2] == "Wizard":
        player = Wizard(l[0], l[1])
    elif l[2] == "Ranger":
        player = Ranger(l[0], l[1])
    while (1):
        refresh_tavern()
        display_score(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_window()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 300 < x < 520 and 250 < y < 700:
                    print("Touch : L'homme mystérieux")
                    print("Nom:", player.name, "| Classe:", player.type)
                    print("Description:", player.talk())
                    battle(player)


def close_window():
    # -|close_window() : Close Window
    pygame.quit()
    sys.exit()


def battle(player):
    # -|battle(player) : Declare Battle against Mob (player V.S monster)
    # Load Graphics and generate random cursor and weakspot location
    hit_hud = pygame.image.load("graphics/hit.png").convert_alpha()
    Fight_BG = pygame.image.load(
        "graphics/battle/battle_bg.png").convert_alpha()
    Fight_Zone_FG = pygame.image.load(
        "graphics/battle/mob_bar.png").convert_alpha()
    Fight_Zone_X_Axis = randint(50, 820)
    Fight_Cursor_FG = pygame.image.load(
        "graphics/battle/cursor.png").convert_alpha()
    Fight_Cursor_X_Axis = randint(50, 940)
    # Generate Monster To fight against
    Fighting_Monster = Monster("Monster")
    Fighting_Monster.generate()
    Monster_Sprite = pygame.image.load(Fighting_Monster.sprite).convert_alpha()
    Screen.blit(Monster_Sprite, (0, 0))
    # Set Vars
    Fight = True
    Direction = True
    Speed = 2
    Acceleration = 0.15
    # Battle Loop
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
        # Display Battle HUD
        Screen.blit(Fight_BG, (0, 0))
        Screen.blit(Fight_Zone_FG, (Fight_Zone_X_Axis, 0))
        Screen.blit(Fight_Cursor_FG, (Fight_Cursor_X_Axis, 0))
        pygame.display.update()
        # Catch Event
        for event in pygame.event.get():
            # If press Exit cross on window HUD then quit
            if event.type == pygame.QUIT:
                close_window()
            # If Space Key is down then :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Check if cursor is on Mob Zone
                    # If it is then mob take a hit and regenerate Zone
                    if Fight_Zone_X_Axis - 20 <= Fight_Cursor_X_Axis <= Fight_Zone_X_Axis + 20:
                        print("InZeZone")
                        player.attack(Fighting_Monster)
                        if Fighting_Monster.isDead():
                            print("Mob is dead")
                            player.score = player.score + Fighting_Monster.score
                            Fight = False
                            break
                        Fight_Zone_X_Axis = randint(50, 820)
                    # If not take damage and display bloody screen
                    else:
                        print("NotInZeZone")
                        Screen.blit(hit_hud, (0, 0))
                        Screen.blit(Monster_Sprite, (0, 0))
                        Fighting_Monster.attack(player)
                        if player.isDead():
                            print("Player is dead")
                            Fight = False
                            grave(player)
                            break
            # Display  at end
            display_score(player)
