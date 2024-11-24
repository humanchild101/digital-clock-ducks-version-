import random
import sys
import pygame
from pygame import QUIT
from SpriteSheet import SpriteSheet
from Duck import Duck
from Button import *
import pytz
import datetime

pygame.init()
WIDTH, HEIGHT = 1000, 1000
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("attacking ducks")
win.fill((230, 230, 230))

'''---------------------------'''


bg_surf = pygame.Surface((1000, 1000))

white = (240, 240, 240, 255)
gray_blue = (106, 129, 166, 255)
navy_blue = (38, 66, 110, 255)
midnight_purple = (37, 29, 112, 255)
midnight_blue = (2, 15, 36, 255)
wisteria = (135, 107, 219, 255)
flowers = (219, 107, 189, 255)
red = (255, 59, 75, 255)
lava = (245, 67, 22, 255)
lemonade = (240, 222, 144, 255)
olive = (121, 138, 83, 255)
sea_glass = (143, 227, 182, 255)

colors = [white, gray_blue, navy_blue, midnight_purple, wisteria, flowers, red, lava, lemonade, olive, sea_glass]
i = 2  # for iterating through colors

# the default ig
bg_surf.fill(navy_blue)
curtz = None  # Tracks selected timezone (None for default)


def bg_change_in_order():
    global i
    bg_surf.fill(colors[i])
    i = (i + 1) % len(colors)

def random_color():
    global i
    if event.type == pygame.MOUSEBUTTONDOWN:
        for _ in range(random.randint(5, 15)):  # Flash through 5-15 colors
            i = (i + random.randint(1, len(colors) - 1)) % len(colors)
            win.fill(colors[i])
            pygame.display.update()
            pygame.time.delay(50)

# Update timezone
def default():
    global curtz
    curtz = None


def london():
    global curtz
    curtz = "Europe/London"


def india():
    global curtz
    curtz = "Asia/Kolkata"

def canada():
    global curtz
    curtz = "America/Toronto"

def belgium():
    global curtz
    curtz = "Europe/Brussels"



# Display time
def display_time(timezone=None):
    if timezone:
        tz = pytz.timezone(timezone)
        now = datetime.datetime.now(tz)
    else:
        now = datetime.datetime.now()

    current_time = now.strftime("%H:%M:%S")
    font = pygame.font.Font("fonts/Orbitron-VariableFont_wght.ttf", 60)
    time_text = font.render(current_time, True, white)
    w, h = font.size(current_time)

    win.blit(time_text, ((500 - w / 2, 500 - h / 2)))  # Display time in the center

'''----------------------------'''

leftp = pygame.image.load("sprite_sheets/leftp.png").convert_alpha()
rightp = pygame.image.load("sprite_sheets/rightp.png").convert_alpha()
lefty = pygame.image.load("sprite_sheets/lefty.png").convert_alpha()
righty = pygame.image.load("sprite_sheets/righty.png").convert_alpha()

lp = SpriteSheet(leftp)
rp = SpriteSheet(rightp)
ly = SpriteSheet(lefty)
ry = SpriteSheet(righty)

lp_list = []
rp_list = []
ly_list = []
ry_list = []

for x in range(7):
    lp_list.append(lp.get_image(x, 190, 195, 0.5))
    rp_list.append(rp.get_image(x, 190, 195, 0.5))
    ly_list.append(ly.get_image(x, 183, 161, 0.5))
    ry_list.append(ry.get_image(x, 183, 161, 0.5))

bg = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()

cute = 0
insane = 0

cute_spawn_time = 0
insane_spawn_time = 0



ducks = [Duck("cute", ly_list, ry_list), Duck("cute", ly_list, ry_list, random_color), Duck("cute", ly_list, ry_list),
         Duck("cute", ly_list, ry_list), Duck("cute", ly_list, ry_list), Duck("cute", ly_list, ry_list),
         Duck("cute", ly_list, ry_list), Duck("cute", ly_list, ry_list)]



'''------------------------'''


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        def spawn_duck(duck_list):
            global cute, insane, cute_spawn_time, insane_spawn_time
            timer = pygame.time.get_ticks()
            if timer - cute_spawn_time >= 4000:
                duck_list.append(Duck("cute", ly_list, ry_list, belgium))
                duck_list.append(Duck("cute", ly_list, ry_list, india))
                duck_list.append(Duck("cute", ly_list, ry_list, london))
                cute += 1
                cute_spawn_time = timer
            if timer - cute_spawn_time >= 4000:
                duck_list.append(Duck("cute", ly_list, ry_list, bg_change_in_order))
                cute += 1
                cute_spawn_time = timer
            if timer - cute_spawn_time >= 9000:
                duck_list.append(Duck("cute", ly_list, ry_list, random.choice([india, belgium, london])))
                cute += 1
                cute_spawn_time = timer
            if timer - cute_spawn_time >= 9000:
                duck_list.append(Duck("cute", ly_list, ry_list, belgium))
                cute += 1
                cute_spawn_time = timer
            if timer - insane_spawn_time >= 11000:
                duck_list.append(Duck("insane", lp_list, rp_list))
                insane += 1
                insane_spawn_time = timer
            if timer - insane_spawn_time >= 32000:
                duck_list.append(Duck("insane", lp_list, rp_list, random_color))
                insane += 1
                insane_spawn_time = timer
            for duck in ducks:
                duck.move(win)


        for duck in ducks:
            duck.clicked(event)


        defa = Button(win, 815, 10, 175, 40, white, "Local Time", white, default, midnight_blue)
        lon = Button(win, 815, 60, 175, 40, white, "London Time", white, london, midnight_blue)
        ind = Button(win, 815, 110, 175, 40, white, "India Time", white, random.choice([india,lambda: spawn_duck(ducks)]), midnight_blue)
        can = Button(win, 815, 160, 175, 40, white, "Canada Time", white, canada, midnight_blue)
        bel = Button(win, 815, 210, 175, 40, white, "Belgium Time", white, belgium, midnight_blue)


        button = Button(win, 10, 10, 175, 40, white, "Change Color", white, bg_change_in_order, midnight_blue)

        defa.clicked(event)
        lon.clicked(event)
        ind.clicked(event)
        can.clicked(event)
        bel.clicked(event)

        button.clicked(event)

        # Draw background and buttons
    win.blit(bg_surf, (0, 0))
    defa.draw()
    lon.draw()
    ind.draw()
    can.draw()
    bel.draw()
    button.draw()


    # Display the correct time
    if curtz:
        display_time(curtz)
    else:
        display_time()

    spawn_duck(ducks)

    pygame.display.update()



#add random functions/szes to ducks
#does not spawn ducks until a button is clikced so add to all the buttons a random(choice choose betwee your actual function, and this one) but idk how to get it to
#add more timezones for more buttons
#spawn for 20 seconds at a time then stop spawning
