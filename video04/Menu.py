import pygame as pyg
from pygame.locals import *

class Menu():
    def buttons(gui,XeY,cor1,cor2,texto,fonte): # Criar um botão
        text = fonte.render(texto,True,cor1,cor2)
        textobjeto = text.get_rect() # Pegar o retangulo do texto
        textobjeto.center = XeY # Colocar o centro como XeY(Tupla)
        obj = gui.blit(text,textobjeto)
        if obj.collidepoint(pyg.mouse.get_pos()): # se está tocando no botão
            if pyg.mouse.get_pressed(3)[0]: # se o mouse está pressionado
                return True
            else:
                return False
        else:
            return False

    def draw_rect(gui,XeY,WeY,cor): # Var, Tupla,Tupla,Tupla
        obj = pyg.draw.rect(gui,cor,Rect(XeY[0]-WeY[0]/2,XeY[1]-WeY[1]/2,WeY[0],WeY[1])) # XeY[i] - WeY[i]/2
        return obj
        # Item 1 = 0
        # Item 2 = 1

    def draw_text(gui,XeY,cor,texto,fonte):
        text = fonte.render(texto,True,cor)
        textobj = text.get_rect()
        textobj.center = XeY
        gui.blit(text,textobj)

    def slider(gui,cor,cor2,XeY1,XeY2,MaxSize):
        pyg.draw.rect(gui,cor2,Rect(XeY2[0],XeY2[1]-5,MaxSize,10))
        s1 = pyg.draw.circle(gui,cor,XeY1,10)
        mpos = pyg.mouse.get_pos()
        if s1.collidepoint(mpos): # Tocando em mouse
            if pyg.mouse.get_pressed(3)[0]: # Mouse está pressionado
                return True,(mpos[0],XeY1[1]), s1 # Retorna Verdadeiro, Nova posição da bolinha, Objeto da bolinha para dar update
            else:
                return False, XeY1, s1 # Retorna Falso, Posição antiga, Objeto da bolinha
        else:
            return False, XeY1, s1 # Retorna Falso, Posição antiga, Objeto da bolinha