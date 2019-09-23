import numpy as np
import pygame
import math
import time

windows=pygame.display.set_mode((800,600))
color=np.array([255,255,0])
P1=np.array([400,300])
pygame.init()

def punto(windows,color,P1):
    pygame.draw.line(windows,color,P1,P1,2)

def traslacion(P1,T):
    return P1 + T

#------------------------------------------------

def linea(windows,color,pos_ini,pos_fin):
    x0=pos_ini[0]
    y0=pos_ini[1]
    x1=pos_fin[0]
    y1=pos_fin[1]
    m=0.0

    if x0 != x1:
        m=round((y1-y0)/(x1-x0))

    x=x0
    y=y0

    print("Pendiente : " + str(m))

    #si x0 y y0 < x1 y y1
    while (x < x1) :
        punto(windows,color,[x,y])
        x=x+1
        y=y+m

    #si x0=x1 y y0 < y1
    while (y < y1) :
        punto(windows,color,[x,y])
        y=y+1

    #si x0<x1 y y0 = y1
    while (x < x1) :
        punto(windows,color,[x,y])
        x=x+1

    # si x0 > x1 y y0 > y1
    while (x > x1 and y > y1) :
        punto(windows,color,[x,y])
        x=x-1
        y=y+m

    #trazar las lineas de arriba a abajo y de abajo arriba    

#-------------------------------------------------------------

def Rectangulo(windows,color,pos_ini,pos_fin,sombra):
    x0=pos_ini[0]
    y0=pos_ini[1]
    x1=pos_fin[0]
    y1=pos_fin[1]

    linea(windows,color,(x0,y0),(x1,y0))
    linea(windows,color,(x0,y1),(x1,y1))
    linea(windows,color,(x0,y0),(x0,y1))
    linea(windows,color,(x1,y0),(x1,y1))

    if sombra == 1:
        x=x0
        y=y0
        for x in range(x0,x1):
            for y in range(y0,y1):
                linea(windows,color,(x,y),(x1,y1))


#del Poligono(windows,color,)

pygame.draw.rect(windows, color, (200,150,100,50),5)

pygame.draw.polygon(windows, color, [(20,20),(250,50),(10,70)],5)

Rectangulo(windows,color,(200,300),(400,500),1)
    
punto(windows,color,P1)
P2=traslacion(P1,[-50,40])

punto(windows,color,P2)
#linea(windows,color,[100,300],[700,300])
#linea(windows,color,[400,50],[400,550])
#linea(windows,color,[400,300],[600,500])
#linea(windows,color,[200,500],[400,300])
#linea(windows,color,[400,300],[600,100])
#linea(windows,color,[100,200],[400,300])


pygame.display.update()
   
time.sleep(8.8)