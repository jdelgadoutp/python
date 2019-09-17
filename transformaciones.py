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
    if x0 < x1 and y0 < y1:
        while (x < x1) :
            punto(windows,color,[x,y])
            x=x+1
            y=y+m

    #si x0=x1 y y0 < y1
    if x0 == x1 and y0 < y1:
        while (y < y1) :
            punto(windows,color,[x,y])
            y=y+1

    #si x0<x1 y y0 = y1
    if x0 < x1 and y0 == y1:
        while (x < x1) :
            punto(windows,color,[x,y])
            x=x+1

    # si x0 > x1 y y0 > y1
    if x0 > x1 and y0 > y1:
        while (x > x1) :
            punto(windows,color,[x,y])
            x=x-1
            y=y-m
    
punto(windows,color,P1)
P2=traslacion(P1,[-50,40])

punto(windows,color,P2)
linea(windows,color,[200,200],[400,400])
linea(windows,color,[100,100],[100,500])
linea(windows,color,[200,100],[600,100])
linea(windows,color,[600,500],[300,200])
pygame.display.update()
   
time.sleep(8.8)