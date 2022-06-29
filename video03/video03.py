import pygame as pyg
from pygame.locals import *
from sys import exit
from Menu import Menu
from random import randint

pyg.init()

SCRW = 800
SCRH = 600
FPS = 15

# Melhorar o botão, adicionar a mecanica da cobra, fazer uma forma de alterar a cor da cobra e contar os pontos
font_buttons = pyg.font.SysFont('Arial',30,True,False)
font_text = pyg.font.SysFont('Arial',20,True,True)

def main():
    pyg.display.set_caption('Snake game - Menu')
    CR = 100 # Cor Red
    CG = 200 # Cor Verde
    CB = 100 # Cor Azul
    while True:
        Play =  Menu.buttons(gui,(400,150),(0,0,0),(90,190,75),'Jogar',font_buttons)
        cor = Menu.buttons(gui,(325,175),(0,0,0),(CR,CG,CB),'Cor',font_buttons)
        if Play:
            game((CR,CG,CB))
        if cor:
            CR = randint(0,200)
            CG = randint(0,200)
            CB = randint(0,200)
            pyg.time.Clock().tick(FPS/3)
        for ev in pyg.event.get():
            if ev.type == QUIT:
                pyg.quit()
                exit()
        
        pyg.time.Clock().tick(FPS)
        pyg.display.update()
        gui.fill((200,200,200))

def game(cor):
    pyg.display.set_caption('Snake game - Play')
    run = True
    x = 20
    y = 0
    cx = 400
    cy = 300
    pontos = 0
    mxy = (randint(30,770),randint(30,570))
    while run:
        cobra = Menu.draw_rect(gui,(cx,cy),(30,30),cor)
        maca = Menu.draw_rect(gui,mxy,(30,30),(200,100,100))
        Menu.draw_text(gui,(65,35),(0,0,0),f'Pontos: {pontos}',font_text)
        if maca.collidepoint((cx,cy)):
            mxy = (randint(30,770),randint(30,570))
            pontos += 1

        if cx > 770: # Tudo sobre X
            cx = 30
            x = 15
            y = 0
        elif cx < 30:
            cx = 770
            x = -15
            y = 0
        if cy > 570: # Tudo sobre Y
            cy = 30
            y = 15
            x = 0
        elif cy < 30:
            cy = 570
            y = -15
            x = 0

        for ev in pyg.event.get():
            if ev.type == QUIT:
                pyg.quit()
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE: # Caso a tecla esc seja apertada run = False
                    run = False
                if ev.key == K_w: # sobe
                    if not y > 0: # Y
                        y = -15
                        x = 0
                if ev.key == K_a:
                    if not x > 0: # X
                        x = -15
                        y = 0
                if ev.key == K_s:
                    if not y < 0: # Y
                        y = 15
                        x = 0
                if ev.key == K_d:
                    if not x < 0: # X
                        x = 15
                        y = 0
        cx += x
        cy += y
        
        pyg.time.Clock().tick(FPS)
        pyg.display.update()
        gui.fill((190,190,215))

gui = pyg.display.set_mode((SCRW,SCRH))

main()