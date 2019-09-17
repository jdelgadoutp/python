import pygame
import time

pygame.init()

windows=pygame.display.set_mode((800,600))

#pygame.draw.rect(windows,(12,115,103 ),(0,0,800,600))

def cuadro(x1,y1,x2,y2):
    xh=x1
    xv=x2
    yh=y1
    yv=y2

    for xh in range(x1,x2+1):
        pygame.draw.rect(windows,(238,27,200),(100 + xh*5,400 + yh*5,5,5))
        pygame.draw.rect(windows,(238,27,200),(100 + xh*5,400 - yv*5,5,5))

    for yv in range(y1,y2+1):
        pygame.draw.rect(windows,(238,27,200),(100 + xh*5,400 + yh*5,5,5))
        print(yv)
        pygame.draw.rect(windows,(238,27,200),(100 + xv*5,400 - yv*5,5,5))
       

cuadro(2,2,10,10)

pygame.display.update()
   
time.sleep(8.8)