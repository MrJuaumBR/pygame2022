import pygame as pyg
from pygame.locals import *

class Menu():
    def buttons(gui,XeY,cor1,cor2,texto,fonte): # Criar um botão
        text = fonte.render(texto,True,cor1,cor2)
        textobjeto = text.get_rect() # Pegar o retangulo do texto
        textobjeto.center = XeY # Colocar o centro como XeY(Tupla)
        obj = gui.blit(text,textobjeto)
        return obj

    def draw_rect(gui,XeY,WeY,cor): # Var, Tupla,Tupla,Tupla
        obj = pyg.draw.rect(gui,cor,Rect(XeY[0]-WeY[0]/2,XeY[1]-WeY[1]/2,WeY[0],WeY[1])) # XeY[i] - WeY[i]/2
        return obj
        # Item 1 = 0
        # Item 2 = 1