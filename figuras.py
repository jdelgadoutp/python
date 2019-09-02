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
pygame.draw.line(windows,(255,27,23),(orix,oriy),(orix + Vx(100,20),oriy - Vy(100,20)),3)

orix=orix + Vx(100,20)
oriy=oriy - Vy(100,20)

pygame.draw.line(windows,(3,236,26),(orix,oriy),(orix + Vx(120,36),oriy - Vy(120,36)),3)

orix=orix + Vx(120,36)
oriy=oriy - Vy(120,36)

pygame.draw.line(windows,(3,236,26),(orix,oriy),(orix + Vx(-80,30),oriy - Vy(80,30)),3)
pygame.display.update()

time.sleep(9.8)
