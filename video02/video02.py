import pygame as pyg
from pygame.locals import *
from sys import exit
from Menu import Menu

pyg.init()

SCRW = 800
SCRH = 600
FPS = 30
font_buttons = pyg.font.SysFont('Arial',30,True,False)

def main():
    pyg.display.set_caption('Snake game - Menu')
    while True:
        Play =  Menu.buttons(gui,(400,150),(45,45,45),(170,200,170),'Jogar',font_buttons)
        mxmy = pyg.mouse.get_pos() # Posição do mouse
        if Play.collidepoint(mxmy):
            if pyg.mouse.get_pressed(3)[0]:
                game()
        for ev in pyg.event.get():
            if ev.type == QUIT:
                pyg.quit()
                exit()
        
        pyg.time.Clock().tick(30)
        pyg.display.update()
        gui.fill((200,200,200))

def game():
    pyg.display.set_caption('Snake game - Play')
    run = True
    while run:
        cobra = Menu.draw_rect(gui,(400,300),(30,30),(135,200,135))
        for ev in pyg.event.get():
            if ev.type == QUIT:
                pyg.quit()
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE: # Caso a tecla esc seja apertada run = False
                    run = False
        pyg.display.update()
        gui.fill((190,190,215))

gui = pyg.display.set_mode((SCRW,SCRH))

main()