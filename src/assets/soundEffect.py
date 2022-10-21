import pygame as pg
import os 

pg.init()
pg.font.init()
pg.mixer.init()

screen = pg.display.set_mode((1136, 640))
# if the code is running start the music

def backgroundMusic(filename): 
    pg.mixer.music.load(filename)
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.5)


