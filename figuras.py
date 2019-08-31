import pygame
import time
import math

def Vx(r,a):
    x = int (r * (math.cos(a*math.pi/180)))
    return x

def Vy(r,a):
    y = int (r * (math.sin(a* math.pi/180)))
    return y

orix=400
oriy=300

x=Vx(100,20)
y=Vy(100,20)

pygame.init()
windows=pygame.display.set_mode((800,600))
pygame.draw.rect(windows,(23,251,205),(0,0,50,30))
pygame.draw.line(windows,(23,251,205),(100,300),(700,300),2)
pygame.draw.line(windows,(23,251,205),(400,100),(400,500),2)
pygame.draw.line(windows,(255,27,23),(orix,oriy),(orix + x,oriy - y),3)
oryxtemp = orix + x
oriytemp = oriy - y
x=Vx(120,36)
y=Vy(120,36)
pygame.draw.line(windows,(3,236,26),(oryxtemp,oriytemp),(oryxtemp + x,oriytemp - y),3)

oryxtempa = oryxtemp + x
oriytempy = oriytemp - y
x=Vx(-80,30)
y=Vy(80,30)
pygame.draw.line(windows,(3,236,26),(oryxtempa,oriytempy),(oryxtempa + x,oriytempy - y),3)
pygame.display.update()

time.sleep(9.8)
