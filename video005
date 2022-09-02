# Criar mapa
#W.. O
import pygame as pyg
from pygame.locals import *
from sys import exit

pyg.init()
gui = pyg.display.set_mode((800,600))

map = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W....W.........WW....W........W",
    "W....W.........WW....W........W",
    "W....W.........WW....W........W",
    "W..............WW.............W",
    "W..............WW.............W",
    "W.............................W",
    "W..............W..............W",
    "WO.............W..............W",
    "W..............W..............W",
    "WO.......O..........WWWWWW....W",
    "WO.......O..........W....W....W",
    "WO.......O............O..W....W",
    "WO.......O..........W....W....W",
    "WO.......O..........WWWWWW....W",
    "WO.......O....................W",
    "WO.......O....................W",
    "WO.......O....................W",
    "WO.......O....................W",
    "WO.......O....................W",
    "WO.......O....................W",
    "WO.......O....................W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW" # 8 Letras W
]

# 800 X 600 | 8 Colunas 800//8 | 6 Colunas 600//6

while True:
    for ev in pyg.event.get():
        if ev.type == QUIT:
            pyg.quit()
            exit()
    pos = [-1,-1]
    for i in map:
        for y in i:
            if y == 'W':
                pyg.draw.rect(gui,(0,0,0),Rect(pos[0],pos[1],25,25))
            if y == "O":
                pyg.draw.circle(gui,(0,0,0),(pos[0]+12,pos[1]+12),12)
            pos[0] += 26
        pos[0] = -1
        pos[1] += 26

    pyg.display.update()
    gui.fill((255,255,255))
