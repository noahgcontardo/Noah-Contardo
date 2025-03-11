import pygame as pg
import random
import numpy as np

#start pg
pg.init()

#arbitrary resolution
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

#use screen as the grid
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#random POO spawn
POO_SPAWN_Y = random.randint(0, 1080)
POO_SPAWN_X = random.randint(0, 1920)

#fixed POI spawn
POI_SPAWN_Y = (100)
POI_SPAWN_X = (300)

#fixed polygon starting position we are testing to see if POO is within
POLY_SPAWN_Y = (400)
POLY_SPAWN_X = (1000)

#noting polygon boundary, may be used might not be used

POLY_RIGHT_SIDE = POLY_SPAWN_X + 300
POLY_LEFT_SIDE = POLY_SPAWN_X - 300
POLY_TOP_SIDE = POLY_SPAWN_Y + 300
POLY_BOTTOM_SIDE = POLY_SPAWN_Y - 300



#create 10x10 rectangle to represent POO
POO_Indicator = pg.Rect((POO_SPAWN_X, POO_SPAWN_Y), (10, 10))

#create 200x200 dangerous zone we cant be firing from
POLY_Indicator =pg.Rect((POLY_SPAWN_X, POLY_SPAWN_Y), (300, 300))

#program loop to keep screen open
running = True
while running:

#black screen
    screen.fill((0, 0, 0))

#shape to test for
    pg.draw.rect(screen, (100, 100, 0), POLY_Indicator)

#when running draw a POO indicator with red RGB value on matrix made by screen variable
    pg.draw.rect(screen, (255, 0, 0), POO_Indicator)

#create simple POI circle
    pg.draw.circle(screen, (0, 255, 0), (POI_SPAWN_X, POI_SPAWN_Y), 10)

#create a line illustrating POO hitting POI dead on
    pg.draw.line(screen, (0, 0, 255), (POO_SPAWN_X, POO_SPAWN_Y), (POI_SPAWN_X, POI_SPAWN_Y), 5)

#function determining X & Y distance between POO and POI

    X_DIFFERENCE = (POI_SPAWN_X - POO_SPAWN_X)
    Y_DIFFERENCE = (POI_SPAWN_Y - POO_SPAWN_Y)

#find square roots of differences squared (^2)
    HYPOTENUSE = ( np.sqrt((X_DIFFERENCE ** 2) + (Y_DIFFERENCE  ** 2)))

#without UI need a way to sotp on exit button
    for event in pg.event.get():
        if event.type ==pg.QUIT:

#print basic debugging info
            print("POO X:", (POO_SPAWN_X))
            print("POO Y:", (POO_SPAWN_Y))
            print("POI X:", (POI_SPAWN_X))
            print("POI Y:", (POI_SPAWN_Y))
            print("POLY TOP:", (POLY_TOP_SIDE))
            print("POLY BOTTOM:", (POLY_BOTTOM_SIDE))
            print("POLY LEFT:", (POLY_LEFT_SIDE))
            print("POLY RIGHT:", (POLY_RIGHT_SIDE))
            print("HYPOTENUSE (LINE LENGTH):", (HYPOTENUSE))
            running = False

    pg.display.update()


pg.quit()
