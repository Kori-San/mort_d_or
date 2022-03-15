# --|Import
# -|Import Functions
import sys
from random import randint
import pygame as pygame
import tkinter as tk

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
    close_window()


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

# -[|Game Func|]


def game():
    # -|game() : Game Loop
    select_char()
    if l[0] == "" or l[1] == "":
        if l[2] == "Warrior":
            player = Warrior("Jenkins", "LEROYYYYYYYYYY JENKINS")
        elif l[2] == "Wizard":
            player = Wizard("Harry", "Je suis un sorcier, Harry")
        elif l[2] == "Ranger":
            player = Ranger("Legolas", "You have my bow...")
    elif l[2] == "Warrior":
        player = Warrior(l[0], l[1])
    elif l[2] == "Wizard":
        player = Wizard(l[0], l[1])
    elif l[2] == "Ranger":
        player = Ranger(l[0], l[1])
    chain = 0
    while (1):
        refresh_tavern()
        display_score(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_window()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                # Coordinates of The Mysterious Man
                if 300 < x < 520 and 250 < y < 700:
                    print("> Touched [ L'homme mystérieux ] <\n")
                    player.talk()
                    # Define Before Battle Var
                    current_hp = player.hp
                    current_score = player.score
                    # End Def
                    battle(player)
                    # Define After Battle Var
                    after_battle_hp = player.hp
                    after_battle_score = player.score
                    # End Def
                    # If Player did a perfect Battle then Heal + Chain++
                    if current_hp == after_battle_hp:
                        heal(player)
                        chain += 1
                        print("# Perfect Battle #\n[Chain]:", chain, "\n")
                    else:  # Else reset Chain
                        chain = 0
                    # If Chain is greater than one then player gain bonus score
                    if chain > 1:
                        score_delta = after_battle_score - current_score
                        score_chain = chain * score_delta
                        player.score += score_chain
                        print(player.name, "$", chain, "(+", score_delta, ")")


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
    Fight_Cursor_X_Axis = randint(235, 705)  # OG: (50, 940)
    # Generate Monster To fight against
    Fighting_Monster = Monster("Monster")
    Fighting_Monster.generate()
    Monster_Sprite = pygame.image.load(Fighting_Monster.sprite).convert_alpha()
    Screen.blit(Monster_Sprite, (0, 0))
    # Set Vars
    Fight = True
    Direction = True
    Speed = 2
    Acceleration = 0.25
    Hitbox = 21.5
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
                    # If it is then: mob take a hit and regenerate Zone
                    if Fight_Zone_X_Axis - Hitbox <= Fight_Cursor_X_Axis <= Fight_Zone_X_Axis + Hitbox:
                        print("> Touched <")
                        player.attack(Fighting_Monster)
                        if Fighting_Monster.isDead(player):
                            # print("[ Mob is dead ]\n")
                            # player.score = player.score + Fighting_Monster.score
                            # print(player.name, "(X_x)", Fighting_Monster.name,
                            #       "( +", Fighting_Monster.score, ")")
                            Fight = False
                            break
                        Fight_Zone_X_Axis = randint(50, 820)
                    # If not: take damage and display bloody screen
                    else:
                        print("> Miss <")
                        Screen.blit(hit_hud, (0, 0))
                        Screen.blit(Monster_Sprite, (0, 0))
                        Fighting_Monster.attack(player)
                        if player.isDead(Fighting_Monster):
                            # print("[ Player is dead ]\n")
                            Fight = False
                            grave(player)
                            break
            # Display  at end
            display_score(player)
