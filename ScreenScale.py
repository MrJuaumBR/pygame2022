import pygame as pyg
from pygame.locals import *
from sys import exit

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

map = [
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1',' ',' ',' ','1','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ','1',' ',' ',' ','1',' ','1',' ',' ',' ',' ','1'],
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ','1',' ',' ','1','1',' ','1','1',' ',' ',' ','1'],
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ','1',' ',' ','1',' ','1',' ','1',' ',' ',' ','1'],
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ','1',' ',' ','1',' ','1',' ','1',' ',' ',' ','1'],
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ','1',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1'],
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ','1',' ','1',' ',' ',' ',' ',' ','1',' ',' ','1'],
    ['1',' ',' ','1',' ',' ',' ','1',' ',' ','1',' ','1',' ',' ',' ',' ',' ','1',' ',' ','1'],
    ['1',' ',' ',' ','1','1',' ',' ','1','1',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ','1'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
]

X_ROWS = len(map[0])
Y_ROWS = len(map)

X_RATIO = X_ROWS/SCREEN_WIDTH
Y_RATIO = Y_ROWS/SCREEN_HEIGHT

BTILE_SIZE = 64
ZOOM = 1

pyg.init()

SCREEN  =pyg.display.set_mode(SCREEN_SIZE)
pyg.display.set_caption("Screen Scale test")

while True:
    TILE_SIZE = BTILE_SIZE
    TILES_FOR_Y = SCREEN_HEIGHT/TILE_SIZE
    TILES_FOR_X = SCREEN_WIDTH/TILE_SIZE

    SCREEN_RATIO = ((TILES_FOR_X+TILES_FOR_Y)/2)*((X_RATIO+Y_RATIO)/2)

    TILE_SIZE *= SCREEN_RATIO
    TILE_SIZE *= ZOOM
    XY = [0,0]
    for y_col in map:
        for x_col in y_col:
            if x_col == '1':
                X,Y = XY
                pyg.draw.rect(SCREEN,(200,100,100),Rect(X,Y,TILE_SIZE,TILE_SIZE))
            XY[0] += TILE_SIZE
        XY[1] += TILE_SIZE
        XY[0] = 0
        
    for ev in pyg.event.get():
        if ev.type == QUIT:
            pyg.quit()
            exit()
        if ev.type == KEYDOWN:
            if ev.key == K_DOWN:
                BTILE_SIZE -= 1
                pyg.display.set_caption(f"Screen Scale, TILE_SIZE: {BTILE_SIZE}, ZOOM: {ZOOM}")
            elif ev.key == K_UP:
                BTILE_SIZE += 1
                pyg.display.set_caption(f"Screen Scale, TILE_SIZE: {BTILE_SIZE}, ZOOM: {ZOOM}")
            elif ev.key in [K_PLUS,K_KP_PLUS]:
                ZOOM += 0.1
                if ZOOM > 2:
                    ZOOM = 2
                pyg.display.set_caption(f"Screen Scale, TILE_SIZE: {BTILE_SIZE}, ZOOM: {ZOOM}")
            elif ev.key in [K_KP_MINUS,K_MINUS]:
                ZOOM -= 0.1
                if ZOOM < 0.1:
                    ZOOM = 0.1
                pyg.display.set_caption(f"Screen Scale, TILE_SIZE: {BTILE_SIZE}, ZOOM: {ZOOM}")

    pyg.display.update()
    SCREEN.fill((255,255,255))