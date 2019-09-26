from __future__ import division
import pygame, sys, math
import numpy as np
import time
from pygame.locals import *

windows=pygame.display.set_mode((800,600))
color=np.array([255,255,0])

pygame.init()

def draw_line_bres(surface, x1, y1, x2, y2, color=(0, 0, 255)):
    dy = y2 - y1
    dx = x2 - x1
    stepY = -1 if dy < 0 else 1
    dy = math.fabs(dy)
    stepX = -1 if dx < 0 else 1
    dx = math.fabs(dx)

    if dx > dy:
        p = 2 * dy - dx
        incE = 2 * dy
        incNE = 2 * (dy - dx)
        x = x1
        y = y1
        xEnd = x2
        stepX = 1
        surface.set_at((x,y), color)
        while x != xEnd:
            x += stepX
            if p < 0:
                p += incE
            else:
                p += incNE
                y += stepY
            surface.set_at((x,y), color)
    else:
        p = 2 * dx - dy
        incE = 2 * dx
        incNE = 2 * (dx - dy)
        x = x1
        y = y1
        yEnd = y2
        stepY = 1
        surface.set_at((x, y), color)
        while y != yEnd:
            y += stepY
            if p < 0:
                p += incE
            else:
                p += incNE
                x += stepX
            surface.set_at((x, y), color)

def draw_line_dda(surface, x1, y1, x2, y2, color=(0, 255, 0)):
	
	dy = y2 - y1
	dx = x2 - x1
	if abs(dx) > abs(dy):
	    steps = dx
	else:
	    steps = dy
	xIncrement = float(dx) / float(steps)
	yIncrement = float(dy) / float(steps)
	surface.set_at((x1, y1), color)
	for i in range(steps):
	    x1 += xIncrement
	    y1 += yIncrement
	    surface.set_at((int(round(x1)), int(round(y1))), color)

def punto(windows,color,P1):
    pygame.draw.line(windows,color,P1,P1,2)

def traslacion(P1,T):
    return P1 + T

def TrianguloR(b,h,pos_ini):
	x0=pos_ini[0]
	y0=pos_ini[1]
	draw_line_dda(windows,x0,y0,x0 + b,y0,color)
	draw_line_dda(windows,x0,y0 - h,x0,y0,color)
	draw_line_dda(windows,x0,y0 - h,x0 + b,y0,color)

def Equi(b,h,pos_ini):
    x0=pos_ini[0]
    y0=pos_ini[1] 
    x=int(x0+b/2) 
    draw_line_bres(windows,x0,y0,x0 + b,y0,color)
    draw_line_bres(windows,x,y0-h,x0,y0,color)
    draw_line_bres(windows,x,y0-h,x0 + b,y0,color)

def Rectangulo(windows,color,pos_ini,pos_fin,sombra):
    x0=pos_ini[0]
    y0=pos_ini[1]
    x1=pos_fin[0]
    y1=pos_fin[1]
    draw_line_dda(windows,x0,y0,x1,y0,color)
    draw_line_dda(windows,x0,y1,x1,y1,color)
    draw_line_dda(windows,x0,y0,x0,y1,color)
    draw_line_dda(windows,x1,y0,x1,y1,color)

    if sombra == 1:
        x=x0
        y=y0
        for x in range(x0,x1):
            for y in range(y0,y1):
                draw_line_dda(windows,x,y,x1,y1,color)
                #pygame.display.update()


TrianguloR(300,200,(100,500))

Equi(300,200,(450,500))

Rectangulo(windows,color,(100,100),(400,200),0)

P1=np.array([400,300])

punto(windows,color,P1)

P2=traslacion(P1,[-50,40])

punto(windows,color,P2)

pygame.display.update()

time.sleep(8.8)