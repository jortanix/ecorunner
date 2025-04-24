import pyglet

# CONSTANTS
MAX_FPS = 144
MOVEMENT_SPEED = 100*5
MOVEMENT_SPEED_2 = 10000
DECELARATION_TIME = .5
MAX_X_VELOCITY = (-1*MOVEMENT_SPEED*(1/MAX_FPS), 1*MOVEMENT_SPEED*(1/MAX_FPS))
SCALE = 2


def getAnimation(animationInfo):
    sprite_sheet, ROWS, COLS = animationInfo

    ROWS = ROWS or 1
    COLS = COLS or 1

    image_grid = pyglet.image.ImageGrid(sprite_sheet, rows=ROWS, columns=COLS)
    return pyglet.image.Animation.from_image_sequence(image_grid, duration=0.1)

def lerp(v0, v1, t): # interpolation linaire precise [a instant t = 1, v = v1 et a instant t = 0, v = v0]
    return (1 - t) * v0 + t * v1

def clamp(v, MIN, MAX):
    if v > MAX:
        return MAX
    elif v < MIN:
        return MIN    
    return v

