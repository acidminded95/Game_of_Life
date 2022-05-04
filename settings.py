import os
from pygame import font

WIDTH = 1280
HEIGHT = 720
FPS = 5
SIZE = {'small': [(20,20), (25,44)], 'medium': [(10,10), (50,88)], 'large': [(5,5), (100,176)]}

APP_FOLDER = os.path.dirname(__file__)
ASSETS_FOLDER = os.path.join(APP_FOLDER, 'assets')
FONT_PATH = os.path.join(ASSETS_FOLDER, 'font/JuliusSansOne-Regular.ttf')

font.init()
julius_sans_big = font.Font(FONT_PATH, 40)
julius_sans_small = font.Font(FONT_PATH, 20)

def choose_color(color):
    if color == 'green':
        DEAD_CELL = (131, 189, 117) # rgb(131, 189, 117)
        NEUTRAL = (233, 239, 192) # rgb(233, 239, 192)
        ALIVE_CELL = (180, 225, 151) # rgb(180, 225, 151)
        BACKGROUND = (78, 148, 79) # rgb(78, 148, 79)
    elif color == 'beach':
        DEAD_CELL = (222, 217, 196) # rgb(222, 217, 196)
        NEUTRAL = (208, 202, 178) # rgb(208, 202, 178)
        ALIVE_CELL = (150, 199, 193) # rgb(150, 199, 193)
        BACKGROUND = (137, 181, 175) # rgb(137, 181, 175)
    elif color == 'pink':
        DEAD_CELL = (255, 188, 209) # rgb(255, 188, 209)
        NEUTRAL = (206, 123, 176) # rgb(206, 123, 176)
        ALIVE_CELL = (162, 103, 172) # rgb(162, 103, 172)
        BACKGROUND = (104, 103, 172) # rgb(104, 103, 172)
    return DEAD_CELL, NEUTRAL, ALIVE_CELL, BACKGROUND

DEAD_CELL, NEUTRAL, ALIVE_CELL, BACKGROUND = (choose_color('beach'))