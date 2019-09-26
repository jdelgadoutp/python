from __future__ import division
import pygame, sys, math
import numpy as np
import math
import time
from pygame.locals import *

windows=pygame.display.set_mode((800,600))
color=np.array([255,255,0])

pygame.init()

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

def TrianguloR(b,h,pos_ini):
	x0=pos_ini[0]
	y0=pos_ini[1]
	draw_line_dda(windows,x0,y0,x0 + b,y0,color)
	draw_line_dda(windows,x0,y0 - h,x0,y0,color)
	draw_line_dda(windows,x0,y0 - h,x0 + b,y0,color)


TrianguloR(300,200,(100,500))

pygame.display.update()

time.sleep(8.8)
