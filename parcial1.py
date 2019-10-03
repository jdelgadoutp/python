from __future__ import division
import pygame, sys, math
import numpy as np
import time
from pygame.locals import *

windows=pygame.display.set_mode((800,700))
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
    pygame.draw.line(windows,color,P1,P1,1)

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

def Pantalla():
    draw_line_dda(windows,0,350,800,350,color)
    draw_line_dda(windows,400,0,400,700,color)
    Rectangulo(windows,color,(0,0),(799,699),0)

def Robot():
    #------------cabeza
    circleBres(windows,color,190,15,9)
    Rectangulo(windows,color,(185,24),(195,50),0)
    Rectangulo(windows,color,(140,50),(240,110),0)
    Rectangulo(windows,color,(160,110),(220,120),0)
    #------------rostro
    circleBres(windows,color,160,70,9)
    draw_line_dda(windows,158,70,162,70,color)
    circleBres(windows,color,220,70,9)
    draw_line_dda(windows,218,70,222,70,color)
    Rectangulo(windows,color,(170,90),(210,100),0)
    draw_line_dda(windows,180,90,180,100,color)
    draw_line_dda(windows,190,90,190,100,color)
    draw_line_dda(windows,200,90,200,100,color)
    #-------------tronco    
    Rectangulo(windows,color,(120,120),(260,250),0)
    Rectangulo(windows,color,(140,140),(240,170),0)
    Equi(10,10,(154,160))
    Equi(10,10,(174,160))
    Equi(10,10,(194,160))
    Equi(10,10,(214,160))
    circleBres(windows,color,160,220,7)
    circleBres(windows,color,190,220,7)
    circleBres(windows,color,220,220,7)
    #--------------brazo derecho
    Rectangulo(windows,color,(260,130),(280,140),0)
    circleBres(windows,color,295,135,15)
    circleBres(windows,color,295,135,6)
    Rectangulo(windows,color,(288,151),(302,160),0)
    Rectangulo(windows,color,(284,160),(306,230),0)
    Rectangulo(windows,color,(288,230),(302,240),0)
    circleBres(windows,color,295,250,10)
    Rectangulo(windows,color,(275,250),(285,270),0)
    Rectangulo(windows,color,(305,250),(315,270),0)
    #---------------brazo izquierdo
    Rectangulo(windows,color,(100,130),(120,140),0)
    circleBres(windows,color,85,135,15)
    circleBres(windows,color,85,135,6)
    Rectangulo(windows,color,(78,151),(92,160),0)
    Rectangulo(windows,color,(74,160),(96,230),0)
    Rectangulo(windows,color,(78,230),(92,240),0)
    circleBres(windows,color,85,250,10)
    Rectangulo(windows,color,(65,250),(75,270),0)
    Rectangulo(windows,color,(95,250),(105,270),0)
    #---------------pierna izquierda
    Rectangulo(windows,color,(140,250),(160,310),0)
    draw_line_dda(windows,160,310,160,340,color)
    draw_line_dda(windows,95,340,160,340,color)
    draw_line_dda(windows,95,340,160,310,color)
    draw_line_dda(windows,140,310,140,320,color)
    #---------------pierna derecha
    Rectangulo(windows,color,(220,250),(240,310),0)
    draw_line_dda(windows,220,310,220,340,color)
    draw_line_dda(windows,220,340,285,340,color)
    draw_line_dda(windows,220,310,285,340,color)
    draw_line_dda(windows,240,310,240,320,color)

def Faro():
    Rectangulo(windows,color,(440,300),(480,340),0)
    Equi(40,40,(440,300))
    Rectangulo(windows,color,(480,300),(560,340),0)
    draw_line_dda(windows,460,260,540,260,color)
    draw_line_dda(windows,540,260,560,300,color)
    draw_line_dda(windows,545,100,530,260,color)
    draw_line_dda(windows,580,76,580,340,color)
    draw_line_dda(windows,560,340,680,340,color)
    draw_line_dda(windows,630,100,650,340,color)
    draw_line_dda(windows,545,100,580,90,color)
    draw_line_dda(windows,580,90,630,100,color)
    draw_line_dda(windows,535,90,545,100,color)
    draw_line_dda(windows,535,90,580,76,color)
    draw_line_dda(windows,640,90,630,100,color)
    draw_line_dda(windows,580,76,640,90,color)
    draw_line_dda(windows,585,30,580,76,color)
    draw_line_dda(windows,585,30,535,90,color)
    draw_line_dda(windows,585,30,640,90,color)
    #------------ventanas izquierda
    draw_line_dda(windows,553,124,570,120,color)
    draw_line_dda(windows,552,162,570,158,color)
    draw_line_dda(windows,553,124,551,162,color)
    draw_line_dda(windows,570,120,570,158,color)

    draw_line_dda(windows,550,194,567,190,color)
    draw_line_dda(windows,548,233,565,230,color)
    draw_line_dda(windows,550,194,548,233,color)
    draw_line_dda(windows,567,192,565,230,color)

    draw_line_dda(windows,548,275,567,275,color)
    draw_line_dda(windows,567,275,567,320,color)
    draw_line_dda(windows,560,320,567,320,color)

    #-------------ventanas derecha

    Rectangulo(windows,color,(600,275),(625,320),0)
    draw_line_dda(windows,595,120,617,124,color)
    draw_line_dda(windows,595,158,617,162,color)
    draw_line_dda(windows,595,120,595,158,color)
    draw_line_dda(windows,617,124,617,162,color)

    draw_line_dda(windows,595,190,617,194,color)
    draw_line_dda(windows,595,230,617,233,color)
    draw_line_dda(windows,595,190,595,230,color)
    draw_line_dda(windows,617,194,617,233,color)

def Cuadro1(pos_ini,x1,y1):
    x=pos_ini[0]
    y=pos_ini[1]
    Rectangulo(windows,color,(x,y),(x + x1,y + y1),0)
    draw_line_dda(windows,x + int(x1/2),y,x,y + int(y1/2),color)
    draw_line_dda(windows,x,y + int(y1/2),x + int(x1/2),y + y1,color)
    draw_line_dda(windows,x + int(x1/2),y,x + x1,y + int(y1/2),color)
    draw_line_dda(windows,x + x1,y + int(y1/2),x + int(y1/2),y + y1,color)
    Rectangulo(windows,color,(x + int((x1/2)/2),y + int((y1/2)/2)),(x + int((x1/2)/2*3),y + int((y1/2)/2*3)),0)
    draw_line_dda(windows,x + int(x1/2),y + int((y1/2)/2),x + int((x1/2)/2),y + int(y1/2),color)
    draw_line_dda(windows,x + int(x1/2),y + int((y1/2)/2),x + int((x1/2)/2*3),y + int(y1/2),color)
    draw_line_dda(windows,x + int((x1/2)/2),y + int(y1/2),x + int(x1/2),y + int((y1/2)/2*3),color)
    draw_line_dda(windows,x + int((x1/2)/2*3),y + int(y1/2),x + int(x1/2),y + int((y1/2)/2*3),color)
    draw_line_dda(windows,x + int((x1/2)/2/2*3),y + int((y1/2)/2/2*3),x + int((x1/2)/2/2*5),y + int((y1/2)/2/2*5),color)
    draw_line_dda(windows,x + int((x1/2)/2/2*5),y + int((y1/2)/2/2*3),x + int((x1/2)/2/2*3),y + int((y1/2)/2/2*5),color)

def LineasI(pos_ini,x1,y1):
    x = pos_ini[0]
    y = pos_ini[1]
    for m in range(1,7):
        draw_line_dda(windows,x + int((x1/12)*m),y,x,y + int((y1/12)*m),color)
        if m == 6:
            draw_line_dda(windows,x + int(x1/2),y + int((y1/12)*m-1),x + int((x1/12)*m-1),y + int(y1/2),color)
        else:    
            draw_line_dda(windows,x + int(x1/2),y + int((y1/12)*m),x + int((x1/12)*m),y + int(y1/2),color)
    
def LineasD(pos_ini,x1,y1):
    x = pos_ini[0]
    y = pos_ini[1]
    
    draw_line_dda(windows,x,y + int((y1/12)*11+1),x + int((x1/12)*1),y + y1,color)
    draw_line_dda(windows,x,y + int((y1/12)*10+1),x + int((x1/12)*2),y + y1,color)
    draw_line_dda(windows,x,y + int((y1/12)*9),x + int((x1/12)*3),y + y1,color)
    draw_line_dda(windows,x,y + int((y1/12)*8+1),x + int((x1/12)*4),y + y1,color)
    draw_line_dda(windows,x,y + int((y1/12)*7+1),x + int((x1/12)*5),y + y1,color)
    draw_line_dda(windows,x,y + int((y1/12)*6),x + int((x1/12)*6),y + y1,color)

    draw_line_dda(windows,x + int((x1/12)*1),y + int(y1/2),x + int(x1/2),y + int((y1/12)*11+1),color)
    draw_line_dda(windows,x + int((x1/12)*2),y + int(y1/2),x + int(x1/2),y + int((y1/12)*10+1),color)
    draw_line_dda(windows,x + int((x1/12)*3),y + int(y1/2),x + int(x1/2),y + int((y1/12)*9),color)
    draw_line_dda(windows,x + int((x1/12)*4),y + int(y1/2),x + int(x1/2),y + int((y1/12)*8+1),color)
    draw_line_dda(windows,x + int((x1/12)*5),y + int(y1/2),x + int(x1/2),y + int((y1/12)*7+1),color)

    draw_line_dda(windows,x + int((x1/12)*11+1),y,x + x1,y + int((y1/12)*1),color)
    draw_line_dda(windows,x + int((x1/12)*10+1),y,x + x1,y + int((y1/12)*2),color)
    draw_line_dda(windows,x + int((x1/12)*9),y,x + x1,y + int((y1/12)*3),color)
    draw_line_dda(windows,x + int((x1/12)*8+1),y,x + x1,y + int((y1/12)*4),color)
    draw_line_dda(windows,x + int((x1/12)*7+1),y,x + x1,y + int((y1/12)*5),color)
    draw_line_dda(windows,x + int((x1/12)*6),y,x + x1,y + int((y1/12)*6),color)

    draw_line_dda(windows,x + int(x1/2),y + int((y1/12)*5),x + int((x1/12)*7+1),y + int(y1/2),color)
    draw_line_dda(windows,x + int(x1/2),y + int((y1/12)*4),x + int((x1/12)*8+1),y + int(y1/2),color)
    draw_line_dda(windows,x + int(x1/2),y + int((y1/12)*3),x + int((x1/12)*9),y + int(y1/2),color)
    draw_line_dda(windows,x + int(x1/2),y + int((y1/12)*2),x + int((x1/12)*10+1),y + int(y1/2),color)
    draw_line_dda(windows,x + int(x1/2),y + int((y1/12)*1),x + int((x1/12)*11+1),y + int(y1/2),color)

def Cuadro2(pos_ini,x1,y1):
    x = pos_ini[0]
    y = pos_ini[1]
    Rectangulo(windows,color,(x,y),(x + x1,y + y1),0)
    draw_line_dda(windows,x + int(x1/2),y,x + int(x1/2),y + y1,color)
    draw_line_dda(windows,x,y + int(y1/2),x + x1,y + int(y1/2),color)
    LineasI(pos_ini,x1,y1)
    LineasI((x+int(x1/2),y+int(y1/2)),x1,y1)  
    LineasD(pos_ini,x1,y1)
    #-----------sombra
    draw_line_dda(windows,x + int((x1/12)*6+1),y+1,x+1,y + int((y1/12)*6+1),color)
    draw_line_dda(windows,x + int((x1/12)*6-1),y-1,x-1,y + int((y1/12)*6-1),color)
    draw_line_dda(windows,x + int((x1/12)*6+1),y-1,x + x1+1,y + int(y1/2-1),color)
    draw_line_dda(windows,x + int((x1/12)*6-1),y+1,x + x1-1,y + int(y1/2+1),color)
    draw_line_dda(windows,x + 1,y + int(y1/2)-1,x + int(x1/2)+1,y + y1-1,color)
    draw_line_dda(windows,x - 1,y + int(y1/2)+1,x + int(x1/2)-1,y + y1+1,color)
    draw_line_dda(windows,x + x1+1,y + int(y1/2)+1,x + int(x1/2)+1,y + y1+1,color)  
    draw_line_dda(windows,x + x1-1,y + int(y1/2)-1,x + int(x1/2)-1,y + y1-1,color)   

Pantalla()
Robot()
Faro()

Cuadro1((20,370),160,160)
Cuadro1((180,370),160,160)
Cuadro1((20,530),160,160)
Cuadro1((180,530),160,160)

Cuadro2((420,370),160,160)
Cuadro2((580,370),160,160)
Cuadro2((420,530),160,160)
Cuadro2((580,530),160,160)

pygame.display.update()

time.sleep(8.8)