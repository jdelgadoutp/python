from __future__ import division
import funcionespain as fn
import ventana as vn
import color as cl
import pygame, sys, math
import numpy as np
import time
from pygame.locals import *
from tkcolorpicker import askcolor

windows=pygame.display.set_mode((900,700))
windows.fill([250,250,250])
Negro =[0, 0, 0]
Amarillo = [250,235,3]
Naranja = [250,108,3]
Morado = [183,3,250]
Cafe = [108,73,24]
Verde = [0,255,0]
Azul = [0,0,255]
Rojo = [250,0,0]
Blanco = [250,250,250]
Rosa = [250,3,202]
Color = Negro
figura = [0,Negro,0]
escalav = [0,0]

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
               figura[0] = fn.validaFigura(event.pos)[0]
           
           if p[0] > 0 and p[0] <= 35 and p[1] > 245 and p[1] <=595:
               figura[1] = fn.validaColor(event.pos)
               print (str(figura) + " con color : " + str(Color))

           if p[0] > 0 and p[0] <= 35 and p[1] > 595 and p[1] <= 630:
               figura[2] = fn.transformaciones(event.pos)

           if p[0] > 0 and p[0] <= 35 and p[1] > 630 and p[1] <= 665:
               figura[2] = fn.transformaciones(event.pos)
               print (figura)

           if p[0] > 0 and p[0] <= 35 and p[1] > 665 and p[1] <= 700:
               figura[2] = fn.transformaciones(event.pos)       

        if event.type == pygame.MOUSEMOTION:
            # imprime en la consola los botones presionados, y su posicion y movimiento relativo en ese momento
            #print (u'botones presionados {}, posicion {} y movimiento relativo {}'.format(event.buttons, event.pos, event.rel))
            
            # linea a  mano alzada
            if event.pos[0] > 35 and event.buttons[0] == 1 and figura[0] == 1:
                fn.punto(windows,figura[1],event.pos)
                pygame.display.flip()

            # Borrador
            if event.pos[0] > 35 and event.buttons[0] == 1 and figura[0] == 7:
                fn.Rectangulo(windows,Blanco,event.pos,(event.pos[0]+3,event.pos[1]+3),1)
                pygame.display.flip()

                      
        if event.type == pygame.MOUSEBUTTONUP:
            if p[0] > 35 and p[1] > 0 and figura[0] == 2:

                if figura[2] == 2:
                    escalav[0] = vn.ventana("Trasladar figura","Ingrese el valor x : ")
                    escalav[1] = vn.ventana("Trasladar figura","Ingrese el valor y : ")
                    fn.Linea(windows,(p[0]+escalav[0],p[1]+escalav[1]),(event.pos[0]+escalav[0],event.pos[1]+escalav[1]),figura[1])
                    figura[2] = 0

                fn.Linea(windows,(p),(event.pos),figura[1])
                pygame.display.flip()

            if event.pos[0] > 35 and figura[0] == 3 and p < event.pos:

                if figura[2] == 1:
                    escala = vn.ventana("Escarlar figura","Ingrese el valor : ")
                    xval = event.pos[0] - p[0]
                    yval = event.pos[1] - p[1]
                    xescala = xval * escala
                    yescala = yval * escala 
                    fn.Rectangulo(windows,figura[1],(p),(event.pos[0]+xescala,event.pos[1]+yescala),0)
                    figura[2] = 0

                if figura[2] == 2:
                    escalav[0] = vn.ventana("Trasladar figura","Ingrese el valor x : ")
                    escalav[1] = vn.ventana("Trasladar figura","Ingrese el valor y : ")
                    fn.Rectangulo(windows,figura[1],(p[0]+escalav[0],p[1]+escalav[1]),(event.pos[0]+escalav[0],event.pos[1]+escalav[1]),0)    
                    figura[2] = 0

                fn.Rectangulo(windows,figura[1],(p),(event.pos),0) 
                pygame.display.flip()   

            if event.pos[0] > 35 and figura[0] == 6 and p < event.pos:

                if figura[2] == 1:
                    escala = vn.ventana("Escarlar figura","Ingrese el valor : ")
                    fn.circleBres(windows,figura[1],p[0],p[1],(event.pos[0]-p[0])*escala)
                    figura[2] = 0

                if figura[2] == 2:
                    escalav[0] = vn.ventana("Trasladar figura","Ingrese el valor x : ")
                    escalav[1] = vn.ventana("Trasladar figura","Ingrese el valor y : ")
                    fn.circleBres(windows,figura[1],p[0] + escalav[0],p[1] + escalav[1],event.pos[0]-p[0])
                    figura[2] = 0    

                fn.circleBres(windows,figura[1],p[0],p[1],event.pos[0]-p[0])
                print (event.pos[0]-p[0])
                pygame.display.flip()

            if event.pos[0] > 35 and figura[0] == 5 and p < event.pos:

                if figura[2] == 1:
                    escala = vn.ventana("Escarlar figura","Ingrese el valor : ")
                    fn.TrianguloR(windows,(event.pos[0]-p[0])*escala,(event.pos[0]-p[0])*escala,(event.pos[0]+10,event.pos[1]),figura[1])
                    figura[2] = 0

                if figura[2] == 3:
                    escala = vn.ventana("Escarlar figura","Ingrese el valor angulo : ")
                    pr = fn.rotar(escala,p) 
                    fn.TrianguloR(windows,event.pos[0]-p[0],event.pos[0]-p[0],pr,figura[1])   

                fn.TrianguloR(windows,event.pos[0]-p[0],event.pos[0]-p[0],p,figura[1])
                pygame.display.flip()

            if event.pos[0] > 35 and figura[0] == 4 and p < event.pos:
                if figura[2] == 1:
                    escala = vn.ventana("Escarlar figura","Ingrese el valor : ")
                    fn.Equilatero(windows,(event.pos[0]-p[0])*escala,(event.pos[0]-p[0])*escala,event.pos[0]+10,event.pos[1],figura[1])
                    figura[2] = 0
                
                fn.Equilatero(windows,event.pos[0]-p[0],event.pos[0]-p[0],p[0],p[1],figura[1])
                pygame.display.flip()

             

    pygame.quit()    

if __name__ == '__main__':
    main()