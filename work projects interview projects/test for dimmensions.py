#fixed polygon starting position we are testing to see if POO is within
POLY_SPAWN_Y = 400
POLY_SPAWN_X = 1000

#polygon boundary calculations
POLY_WIDTH = 300
POLY_HEIGHT = 300

POLY_RIGHT_SIDE = POLY_SPAWN_X + POLY_WIDTH / 2
POLY_LEFT_SIDE = POLY_SPAWN_X - POLY_WIDTH / 2
POLY_TOP_SIDE = POLY_SPAWN_Y + POLY_HEIGHT / 2
POLY_BOTTOM_SIDE = POLY_SPAWN_Y - POLY_HEIGHT / 2

print(POLY_RIGHT_SIDE) 
print(POLY_LEFT_SIDE)
print(POLY_BOTTOM_SIDE)
print(POLY_TOP_SIDE)