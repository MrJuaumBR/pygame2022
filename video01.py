import pygame as pyg # importei o pygame
from pygame.locals import * # Importar algumas ferramentas
from sys import exit # Importei o exit do sys

SCRW = 800 # Largura da janela
SCRH = 600 # Altura da janela

pyg.init() # Iniciar o pygame

# X = Posição em questão a direita ou esquerda(Horizontal)
# Y = Posição em questão a superior ou inferior(Vertical)
# FPS = Frame per Second(Quadros por segundos)

# Criar janela
gui = pyg.display.set_mode((SCRW,SCRH))
pyg.display.set_caption('Video 001')

def main():
    x = 0
    y = 0
    while True:
        pyg.draw.rect(gui,(100,100,100),Rect(SCRW/2-100,SCRH/2-50,200,100)) # Tamanho da tela /2 - Tamanho do objeto /2
        pyg.draw.circle(gui,(50,200,200),(x,y),20)
        
        for ev in pyg.event.get():
            if ev.type == QUIT:
                pyg.quit()
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pyg.quit()
                    exit()
                if ev.key == K_d: # Adiciona valor para direita
                    x += 10
                if ev.key == K_s: # Adiciona valor para baixo
                    y += 10
                if ev.key == K_a: # Diminui valor para esquerda
                    x -= 10
                if ev.key == K_w: # Diminui valor para cima
                    y -= 10

        pyg.display.update() # Atualiza a tela
        pyg.time.Clock().tick(30) # Quanto maior o FPS mais quadros serão reproduzidos
        gui.fill((255,255,255)) # RGB(Red,Green,Blue)(Vermelho,Verde,Azul)
main()