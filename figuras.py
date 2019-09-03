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

pygame.draw.rect(windows,(107,204,241),(0,0,800,600))

pygame.draw.line(windows,(255,255,255),(200,300),(600,300),2)
pygame.draw.line(windows,(255,255,255),(400,100),(400,500),2)
pygame.draw.line(windows,(157,19,247),(orix,oriy),(orix + Vx(100,20),oriy - Vy(100,20)),3)

orix=orix + Vx(100,20)
oriy=oriy - Vy(100,20)

pygame.draw.line(windows,(3,236,26),(orix,oriy),(orix + Vx(120,36),oriy - Vy(120,36)),3)

orix=orix + Vx(120,36)
oriy=oriy - Vy(120,36)

pygame.draw.line(windows,(231,114,28),(orix,oriy),(orix + Vx(-80,30),oriy - Vy(80,30)),3)

orix=orix + Vx(-80,30)
oriy=oriy - Vy(80,30)

pygame.draw.line(windows,(236,240,13),(orix,oriy),(orix + Vx(180,180),oriy - 0),3)

orix=orix + Vx(180,180)
oriy=oriy - 0

pygame.draw.line(windows,(13,161,240),(orix,oriy),(orix + Vx(-230,65),oriy - Vy(-230,65)),3)

orix=400
oriy=300

pygame.draw.line(windows,(249,46,232),(orix,oriy),(orix + Vx(170,203),oriy - Vy(170,203)),3)

pygame.display.update()

time.sleep(5.8)
