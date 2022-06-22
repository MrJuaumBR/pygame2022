import pygame as pyg
from pygame.locals import *
from sys import exit
from Menu02 import Menu

pyg.init()

font = pyg.font.SysFont('Arial',30,True,False)

SCRW = 800
SCRH = 600

def menu(): # Menu principal
    pyg.display.set_caption('Snake Game - Menu')
    while True:
        jogar = Menu.button(gui,(400,300),(0,0,0),(90,90,200),'Jogar',font) # Cria o objeto do botão
        mouse_pos = pyg.mouse.get_pos()
        if jogar.collidepoint(mouse_pos): # Checa se estou tocando no botão
            if pyg.mouse.get_pressed(3)[0]:  # Checa se estou clicando no botão
                game()

        for ev in pyg.event.get():
            if ev.type == QUIT:
                pyg.quit()
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pyg.quit()
                    exit()
        
        pyg.time.Clock().tick(30)
        pyg.display.update()
        gui.fill((200,200,200))

def game(): # Jogo em sí
    pyg.display.set_caption('Snake Game - Play')
    run = True
    while run:

        for ev in pyg.event.get():
            if ev.type == QUIT:
                pyg.quit()
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:  # Esc = Voltar para menu
                    run = False
        
        Menu.draw_rect(gui,(400,300),(75,200,75),(20,20))

        pyg.time.Clock().tick(30)
        pyg.display.update()
        gui.fill((210,210,245))

gui = pyg.display.set_mode((SCRW,SCRH))

menu()