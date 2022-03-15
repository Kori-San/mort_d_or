# --|Import
# -|Import Functions
import pygame as pygame
import tkinter as tk
import sys

# --|Vars
# -|Parameters
Resolution_X = 1000
Resolution_Y = 800
Framerate = 120
l = ["", "", ""]  # l[0, Name | 1, Description | 2, Class]

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
# -[|Tkinter|]


def getting():
    # -|getting(): Get info from Tkinter prompt
    if name.get() != "":
        print("Set name to:", name.get())
        l[0] = name.get()
    if desc.get() != "":
        print("Set desc to:", desc.get())
        l[1] = desc.get()
    if sel_class.get() != "":
        print("Set type to:", sel_class.get(), "\n")
        l[2] = sel_class.get()
    master.destroy()


def select_char():
    # -| select_char(): Display Tkinter prompt to get info for character creation
    master.title("Select your Character!")
    master.eval('tk::PlaceWindow . center')  # Center Display
    tk.Label(master, text="Nom").pack()
    name.pack()
    tk.Label(master, text="Description").pack()
    desc.pack()
    s_class.set("Warrior")  # Default Value
    class_box = tk.OptionMenu(master, s_class, "Warrior", "Wizard", "Ranger")
    class_box.pack()
    tk.Button(master, text="Set", command=getting).pack()
    tk.mainloop()

# -[|Pygame|]


def close_window():
    # -|close_window() : Close Window
    pygame.quit()
    sys.exit()


def grave(player):
    # -|grave(player): Display death of the player given in arg
    refresh_tavern()
    hit_hud = pygame.image.load("graphics/hit.png").convert_alpha()
    Screen.blit(hit_hud, (0, 0))
    skull = pygame.image.load("graphics/skull.png").convert_alpha()
    Screen.blit(skull, (0, 0))
    display_score(player)
    pygame.time.wait(3*1000)
    # Number of seconds * 1000 to match milliseconds requierements
    player.score = 0
    player.hp = player.max_hp
    print(">", player.name, "has revived! <\n")


def heal(player):
    heal_hud = pygame.image.load("graphics/heal.png").convert_alpha()
    Screen.blit(heal_hud, (0, 0))
    pygame.display.update()
    player.heal()
    pygame.time.wait(250)  # 250 MilliSeconds


def display_score(player):
    # -|display_score(player): Display score of given player on pygame
    font = pygame.font.SysFont("Myriad Pro", 72)
    text = font.render(str(player.score), True, (255, 255, 255))
    Screen.blit(text, (45, 25))
    pygame.display.update()


def refresh_tavern():
    # -|refresh_tavern(): Flip screen to gain perf and display tavern
    pygame.display.flip()
    tavern = pygame.image.load("graphics/tavern.png").convert_alpha()
    man = pygame.image.load("graphics/man.png").convert_alpha()
    Screen.blit(tavern, (0, 0))
    Screen.blit(man, (300, 250))
    pygame.display.update()
