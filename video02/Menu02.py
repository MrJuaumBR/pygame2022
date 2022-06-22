import pygame as pyg
from pygame.locals import *
from sys import exit

class Menu():
    def button(gui,XeY,cor,cor2,text,font):
        texto = font.render(text,True,cor,cor2)
        textobjeto = texto.get_rect()
        textobjeto.center = XeY
        button = gui.blit(texto, textobjeto)
        return button

    def draw_rect(gui,XeY,cor,WeH):
        pyg.draw.rect(gui,cor,Rect(XeY[0]-WeH[0]/2,XeY[1]-WeH[1]/2,WeH[0],WeH[1]))
        # Item 1 = 0
        # Item 2 = 1