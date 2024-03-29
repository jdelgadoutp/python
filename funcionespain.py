import pygame, sys, math
import numpy as np
import color as cl
import time
from tkcolorpicker import askcolor

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

def Equilatero(windows,b,h,x0,y0,color):
   x=int(x0+b/2) 
   draw_line_bres(windows,x0,y0,x0 + b,y0,color)
   draw_line_bres(windows,x,y0-h,x0,y0,color)
   draw_line_bres(windows,x,y0-h,x0 + b,y0,color)

def TrianguloR(windows,b,h,pos_ini,color):
	x0=pos_ini[0]
	y0=pos_ini[1]
	draw_line_dda(windows,x0,y0,x0 + b,y0,color)
	draw_line_dda(windows,x0,y0 - h,x0,y0,color)
	draw_line_dda(windows,x0,y0 - h,x0 + b,y0,color)

def Poli(windows, color, vertex_count, radius, position):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(windows, color, [
        (x + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n))
        for i in range(n)
    ])

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

def validaFigura(pos_ini):
    x = pos_ini[0]
    y = pos_ini[1]
    figura = [0,"Elije una función"]
    
    if x > 0 and x <= 35 and y > 0 and y <= 35:
        figura[0] = 1
        figura[1] = "Dibujo a mano alzada"
        
    if x > 0 and x <= 35 and y > 35 and y <= 70:
        figura[0] = 2  
    if x > 0 and x <= 35 and y > 70 and y <= 105:
        figura[0] = 3 
    if x > 0 and x <= 35 and y > 105 and y <= 140:
        figura[0] = 4
    if x > 0 and x <= 35 and y > 140 and y <= 175:
        figura[0] = 5
    if x > 0 and x <= 35 and y > 175 and y <= 210:
        figura[0] = 6
    if x > 0 and x <= 35 and y > 210 and y <= 245:
        figura[0] = 7                        
    
    return figura

def validaColor(pos_ini):
    x = pos_ini[0]
    y = pos_ini[1]
    color = [0,0]
    
    if x > 0 and x <= 35 and y > 245 and y <= 280:
        color[0] = Amarillo
    if x > 0 and x <= 35 and y > 280 and y <= 315:
        color[0] = Azul  
    if x > 0 and x <= 35 and y > 315 and y <= 350:
        color[0] = Rojo 
    if x > 0 and x <= 35 and y > 350 and y <= 385:
        color[0] = Verde
    if x > 0 and x <= 35 and y > 385 and y <= 420:
        color[0] = Naranja
    if x > 0 and x <= 35 and y > 420 and y <= 455:
        color[0] = Negro
    if x > 0 and x <= 35 and y > 455 and y <= 490:
        color[0] = Cafe
    if x > 0 and x <= 35 and y > 490 and y <= 525:
        color[0] = Rosa
    if x > 0 and x <= 35 and y > 525 and y <= 560:
        color[0] = Morado
    if x > 0 and x <= 35 and y > 560 and y <= 595:
        color = cl.color()

    return color[0]

def transformaciones(pos_ini):
    x = pos_ini[0]
    y = pos_ini[1]

    if x > 0 and x <= 35 and y > 595 and y <= 630:
        funcion = 1

    if x > 0 and x <= 35 and y > 630 and y <= 665:
        funcion = 2 

    if x > 0 and x <= 35 and y > 665 and y <= 700:
        funcion = 3       

    return funcion    

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

def menu(windows,color,pos_ini):
    x = pos_ini[0]
    y = pos_ini[1]
    draw_line_dda(windows,x+5,y+20,x+30,y+20,Negro)
    for n in range(0,20):
        Rectangulo(windows,Negro,(x,y),(x + 35,y + 35),0)
        y = y + 35
        if n == 0:
            draw_line_dda(windows,x+25,y+5,x+5,y+30,Negro)
        if n == 1:
            Rectangulo(windows,Negro,(x +5,y+5),(x+30,y+30),0)    
        if n == 2:
            Equilatero(windows,20,20,x+7,y+27,Negro)
        if n == 3:
            TrianguloR(windows,20,20,(x+7,y+27),Negro)
        if n == 4:
            circleBres(windows,Negro,(x+18),(y+18),14)
        if n == 5:
            Rectangulo(windows,Negro,(x+7,y+13),(x+30,y+20),1)    
        if n == 6:
            Rectangulo(windows,Amarillo,(x+2,y+2),(x+33,y+33),1)
        if n == 7:
            Rectangulo(windows,Azul,(x+2,y+2),(x+33,y+33),1)    
        if n == 8:
            Rectangulo(windows,Rojo,(x+2,y+2),(x+33,y+33),1)
        if n == 9:
            Rectangulo(windows,Verde,(x+2,y+2),(x+33,y+33),1)
        if n == 10:
            Rectangulo(windows,Naranja,(x+2,y+2),(x+33,y+33),1)
        if n == 11:
            Rectangulo(windows,Negro,(x+2,y+2),(x+33,y+33),1)        
        if n == 12:
            Rectangulo(windows,Cafe,(x+2,y+2),(x+33,y+33),1)    
        if n == 13:
            Rectangulo(windows,Rosa,(x+2,y+2),(x+33,y+33),1)    
        if n == 14:
            Rectangulo(windows,Morado,(x+2,y+2),(x+33,y+33),1)
        if n == 15:
            Rectangulo(windows,Azul,(x+10,y+10),(x+25,y+25),1)
        if n == 16:
            Equilatero(windows,8,8,x+5,y+25,Azul)    
            Equilatero(windows,15,18,x+15,y+25,Azul) 
        if n == 17:
            Rectangulo(windows,Rojo,(x+5,y+5),(x+10,y+10),1)
            Rectangulo(windows,Morado,(x+25,y+25),(x+30,y+30),1)
        if n == 18:
            Rectangulo(windows,Rojo,(x+5,y+5),(x+7,y+30),1) 
            Rectangulo(windows,Rojo,(x+10,y+17),(x+30,y+19),1)          

    pygame.display.flip()

def Linea(windows,pos_ini,pos_fin,color):
    x0 = pos_ini[0]
    y0 = pos_ini[1]
    x1 = pos_fin[0]
    y1 = pos_fin[1]

    if y1 < y0 and x1 < x0:
        draw_line_dda(windows,x1,y1,x0,y0,color)
    else:
        draw_line_dda(windows,x0,y0,x1,y1,color)

def rotar(r,p):
    coseno = math.cos(math.radians(r))
    seno = math.sin(math.radians(r)) 
    xp = round(p[0]*coseno - p[1]*seno)
    yp = round(p[0]*seno + p[1]*coseno)
    if xp < 1:
        xp = xp * -1
    if yp < 1:
        yp = yp * -1    
    pp = [xp,yp]
    print (pp)
    return pp

def rotar2(r,p):
    coseno = math.cos(math.radians(r))
    seno = math.sin(math.radians(r)) 
    xp = p[0]*coseno + p[1]*seno
    yp = p[1]*coseno - p[0]*seno
    pp = [xp,yp]
    return pp