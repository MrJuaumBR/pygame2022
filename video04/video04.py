import pygame as pyg
from pygame.locals import *
from sys import exit
from Menu import Menu
from random import randint

pyg.init()

SCRW = 800
SCRH = 600
FPS = 30

# Melhorar o botão, adicionar a mecanica da cobra, fazer uma forma de alterar a cor da cobra e contar os pontos
font_buttons = pyg.font.SysFont('Arial',30,True,False)
font_text = pyg.font.SysFont('Arial',20,True,True)

def main():
    pyg.display.set_caption('Snake game - Menu')
    CR = 100 # Cor Red
    CG = 200 # Cor Verde
    CB = 100 # Cor Azul
    SCR = 100
    SCG = 200
    SCB = 100
    RSXeY = (100,180+50)
    GSXeY = (100,220+50)
    BSXeY = (100,260+50)
    c_type = 1
    while True:
        Play =  Menu.buttons(gui,(400,150),(0,0,0),(90,190,75),'Jogar',font_buttons)
        cor = Menu.buttons(gui,(325,175),(0,0,0),(CR,CG,CB),'Cor',font_buttons)
        RSlider = Menu.slider(gui,(125,50,50),(0,0,0),RSXeY,(100,180+50),410) # Este Slider é para a cor vermelha
        GSlider = Menu.slider(gui,(50,125,50),(0,0,0),GSXeY,(100,220+50),410) # Este Slider é para a cor Verde
        BSlider = Menu.slider(gui,(50,50,125),(0,0,0),BSXeY,(100,260+50),410) # Este Slider é para a cor Azul
        Set_cor = Menu.buttons(gui,(100,375),(0,0,0),(SCR,SCG,SCB),'Cor RGB',font_buttons)
        if Set_cor:
            SCR = round(RSXeY[0]/2) # Pegar cor Vermelha
            SCG = round(GSXeY[0]/2) # Pegar cor verde
            SCB = round(BSXeY[0]/2) # Pegar Cor azul
            c_type = 2
        if RSlider[0]: # Se é True
            RSXeY = RSlider[1] # Nova posição
            if RSXeY[0] >= 511:
                RSXeY = (410,RSXeY[1])
            elif RSXeY[0] <= 99:
                RSXeY = (101,RSXeY[1])
            pyg.time.Clock().tick(FPS*10) # Aumentar o tick de 30 para 300
            pyg.display.update(RSlider[2]) # Dar Update apenas da bolinha
        if GSlider[0]: # Se é True
            GSXeY = GSlider[1] # Nova posição
            if GSXeY[0] >= 511:
                GSXeY = (410,GSXeY[1])
            elif RSXeY[0] <= 99:
                GSXeY = (101,GSXeY[1])
            pyg.time.Clock().tick(FPS*10) # Aumentar o tick de 30 para 300
            pyg.display.update(RSlider[2]) # Dar Update apenas da bolinha
        if BSlider[0]: # Se é True
            BSXeY = BSlider[1] # Nova posição
            if BSXeY[0] >= 511:
                BSXeY = (410,BSXeY[1])
            elif BSXeY[0] <= 99:
                BSXeY = (101,BSXeY[1])
            pyg.time.Clock().tick(FPS*10) # Aumentar o tick de 30 para 300
            pyg.display.update(RSlider[2]) # Dar Update apenas da bolinha
        if Play:
            if c_type == 1:
                color = (CR,CG,CB)
            elif c_type == 2:
                color = (SCR,SCG,SCB)
            game(color)
        if cor:
            c_type = 1
            CR = randint(0,200)
            CG = randint(0,200)
            CB = randint(0,200)
            pyg.time.Clock().tick(FPS/5)
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
    size = 5
    CobraList = []
    while run:
        for i in CobraList:
            cobra = Menu.draw_rect(gui,(i[0],i[1]),(30,30),cor)
        maca = Menu.draw_rect(gui,mxy,(30,30),(200,100,100))
        Menu.draw_text(gui,(65,35),(0,0,0),f'Pontos: {pontos}',font_text)
        if maca.collidepoint((cx,cy)):
            mxy = (randint(30,770),randint(30,570))
            size += 1
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
        
        head = []
        head.append(cx)
        head.append(cy)
        CobraList.append(head)
        if len(CobraList) > size:
            del CobraList[0]

        for i in CobraList[:-1]: # Código fixado após o vídeo!!!!!
            print(CobraList)
            print(head)
            if i == head:
                run = False

        pyg.time.Clock().tick(FPS/2)
        pyg.display.update()
        gui.fill((190,190,215))

gui = pyg.display.set_mode((SCRW,SCRH))

main()