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

def linea(windows,color,x0,x1,y0,y1,col):
    dx=x1-x0
    dy=y1-y0
    ix=2*dx
    iy=2*dy
    y=y0
    x=x0
    e=iy - dx

    for x in range(x0,x1):
        punto(windows,color,[x,y])
        print('pixel:', x, y, col)
        if e > 0:
            y = y+1
            e = e-ix
        e = e+iy

linea(windows,color,200,100,300,500,1)

pygame.display.update()

   
time.sleep(8.8)