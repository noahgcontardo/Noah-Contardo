import pygame as pg
import random

pg.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

POI_SPAWN_Y = random.randint(0, 1080)
POI_SPAWN_X = random.randint(0, 1920)

POI_Indicator = pg.Rect((POI_SPAWN_X, POI_SPAWN_Y), (50, 50))

running = True
while running:

    screen.fill((0, 0, 0))



    pg.draw.rect(screen, (255, 0, 0), POI_Indicator)

    for event in pg.event.get():
        if event.type ==pg.QUIT:
            running = False

    pg.display.update()

pg.quit()
