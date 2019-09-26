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

def Equi(b,h,x0,y0):
   x=int(x0+b/2) 
   draw_line_bres(windows,x0,y0,x0 + b,y0,color)
   draw_line_bres(windows,x,y0-h,x0,y0,color)
   draw_line_bres(windows,x,y0-h,x0 + b,y0,color)

Equi(200,300,100,500)

pygame.display.update()

time.sleep(8.8)
