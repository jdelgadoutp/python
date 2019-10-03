from __future__ import division
import pygame, sys, math
import numpy as np
import time
from pygame.locals import *

windows=pygame.display.set_mode((800,700))
color=np.array([12, 102, 240])
color1=np.array([5, 164, 250])

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

def punto(windows,color,P1):
    pygame.draw.line(windows,color,P1,P1,1)

def drawCircle(windows,color,xc,yc,x,y):
    punto(windows,color,[xc+x,yc+y])
    punto(windows,color,[xc-x,yc+y])
    punto(windows,color,[xc+x,yc-y])
    punto(windows,color,[xc-x,yc-y])
    punto(windows,color,[xc+y,yc+x])
    punto(windows,color,[xc-y,yc+x])
    punto(windows,color,[xc+y,yc-x])
    punto(windows,color,[xc-y,yc-x])

def circleBres(windows,color,xc,yc,r):
    x = 0
    y = r
    d = 3 - 2 * r
    drawCircle(windows,color,xc,yc,x,y)
    while (y >= x):
        x = x + 1
        if (d > 0):
            y = y - 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        drawCircle(windows,color,xc,yc,x,y)

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
        for x0 in range(x0,x1):
            for y0 in range(y0,y1):
                draw_line_dda(windows,x0,y0,x1,y0,color)

def figura1(windows,pos_ini,x0,y0):
    x = pos_ini[0]
    y = pos_ini[1]
    for n in range(0,4):
        if n == 0 or n == 3:
            Rectangulo(windows,color1,(x , y),(x + x0,y + y0),1)
        else:
            Rectangulo(windows,color,(x , y),(x + x0,y + y0),0)    
        x = x + x0
        if n == 1:
            y = y + y0
            x = pos_ini[0]

def figura2(windows,pos_ini,x0,y0):
    x = pos_ini[0]
    y = pos_ini[1]
    for n in range(0,9):
        
        if n == 1 or n == 3 or n ==5 or n == 7:
            Rectangulo(windows,color1,(x , y),(x + x0,y + y0),1)
        else:
            Rectangulo(windows,color,(x , y),(x + x0,y + y0),0) 
        
        x = x + x0
        if n == 2 or n == 5:
            y = y + y0
            x = pos_ini[0]

def figura3(windows,pos_ini,x0,y0):
    x = pos_ini[0]
    y = pos_ini[1]
    for n in range(0,9):
        
        if n == 1 or n == 3 or n == 4 or n == 5 or n == 7:
            Rectangulo(windows,color1,(x , y),(x + x0,y + y0),1)
        else:
            Rectangulo(windows,color,(x , y),(x + x0,y + y0),0) 
        
        x = x + x0
        if n == 2 or n == 5:
            y = y + y0
            x = pos_ini[0]

def figura4(windows,pos_ini,x0,y0):
    x = pos_ini[0]
    y = pos_ini[1]
    e = 0
    s = 1
    for n in range(0,5):
        Rectangulo(windows,color,(x , y),(x + x0 + e,y + y0),1)
        Rectangulo(windows,color1,(x + 2, y + 2),(x + x0 + e - 2,y + y0 - 2),1)
        e = e + int(x0/3*s)
        s = s + 1
        x = pos_ini[0]
        y = y + y0

def figura5(windows,pos_ini,x0,y0):
    x = pos_ini[0]
    y = pos_ini[1]
    e = 0
    for n in range(0,6):
        Rectangulo(windows,color,(x - e, y),(x + x0 + e,y + y0),0)
        Rectangulo(windows,color1,(x - e + 2,y+2),(x + x0 + e -2,y + y0 -2),1)
        e = e + int(x0/3*2)
        x = pos_ini[0]
        y = y + y0        

def figura6(b,h,pos_ini):
	x0=pos_ini[0]
	y0=pos_ini[1]
	draw_line_dda(windows,x0,y0,x0 + b,y0,color)
	draw_line_dda(windows,x0,y0 - h,x0,y0,color)
	draw_line_dda(windows,x0,y0 - h,x0 + b,y0,color)

def figura7(b,h,pos_ini):
    x0=pos_ini[0]
    y0=pos_ini[1] 
    x=int(x0+b/2) 
    draw_line_dda(windows,x0,y0,x0 + b,y0,color)
    draw_line_dda(windows,x,y0-h,x0,y0,color)
    draw_line_dda(windows,x,y0-h,x0 + b,y0,color)

def figura8(windows,pos_ini,x0,y1):
    x = pos_ini[0]
    y = pos_ini[1]
    draw_line_dda(windows,x,y,x + x0,y,color)
    draw_line_dda(windows,x - 50,y1,x + x0 + 50,y1,color)
    draw_line_dda(windows,x,y,x - 50,y1,color)
    draw_line_dda(windows,x + x0,y,x + x0 + 50,y1,color)

def figura10(windows,cx,cy,r):
    circleBres(windows,color,cx,cy,r)

def figura9(windows, color, vertex_count, radius, position):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(windows, color, [
        (x + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n))
        for i in range(n)
    ])

#--------------se hace el llamado de la funcion figura mas el numero del ejercicio ejemplo figura1,figura2

#figura1(windows,(100,100),200,100)
#figura2(windows,(100,100),100,100)
#figura3(windows,(100,100),100,100)
#figura4(windows,(100,100),120,80)
#figura5(windows,(350,50),80,80)
#figura6(300,300,(100,500))
#figura7(300,300,(200,500))
#figura8(windows,(200,100),200,300)
figura9(windows,color,5,200,(200,300))
#figura10(windows,400,300,200)


pygame.display.update()

time.sleep(8.8)