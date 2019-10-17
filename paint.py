from __future__ import division
import funcionespain as fn
import pygame, sys, math
import numpy as np
import time
from pygame.locals import *

windows=pygame.display.set_mode((800,600))
windows.fill([250,250,250])
Negro =[0, 0, 0]
Amarillo = [250,235,3]
Naranja = [250,108,3]
Morado = [183,3,250]
Cafe = [108,73,24]
Verde = [0,255,0]
Azul = [0,0,255]
Rojo = [250,0,0]
Blanco = [255,255,255]
Rosa = [250,3,202]
Color = Negro
figura = [0,Negro,[],[]]

def main():
    pygame.init()
    pygame.display.set_caption(u'Programa graficador')
    
    fn.menu(windows,Blanco,(0,0))
    
    while True:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
           p = (event.pos)
           print (p)
           if p[0] > 0 and p[0] <= 35 and p[1] > 0 and p[1] <=245:
               figura[0] = fn.validaFigura(event.pos)
              
           if p[0] > 0 and p[0] <= 35 and p[1] > 245 and p[1] <=560:
               figura[1] = fn.validaColor(event.pos)
               print (str(figura) + " con color : " + str(Color))
           if p[0] > 35 and p[1] > 0 and figura[0] == 2:
               figura[2] = p


        if event.type == pygame.MOUSEMOTION:
            # imprime en la consola los botones presionados, y su posicion y movimiento relativo en ese momento
            #print u'botones presionados {}, posicion {} y movimiento relativo {}'.format(event.buttons, event.pos, event.rel)
            if event.pos[0] > 35 and event.buttons[0] == 1 and figura[0] == 1:
                fn.punto(windows,figura[1],event.pos)
                pygame.display.flip()               

        if event.type == pygame.MOUSEBUTTONUP:
            if p[0] > 35 and p[1] > 0 and figura[0] == 2:
                #fn.draw_line_dda(windows,p[0],p[1],event.pos[0],event.pos[1],figura[1])
                fn.Linea(windows,(p[0],p[1]),(event.pos[0],event.pos[1]),figura[1])
                pygame.display.flip()

            if event.pos[0] > 35 and figura[0] == 3 and p < event.pos:
                fn.Rectangulo(windows,figura[1],(p),(event.pos),0) 
                pygame.display.flip()   

            if event.pos[0] > 35 and figura[0] == 6 and p < event.pos:
                fn.circleBres(windows,figura[1],p[0],p[1],event.pos[0]-p[0])
                print (event.pos[0]-p[0])
                pygame.display.flip()

            
    pygame.quit()    

if __name__ == '__main__':
    main()

    
