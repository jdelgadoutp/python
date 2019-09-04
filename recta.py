import pygame
import time

def pendiente(x1,y1,x2,y2):
    m = (y2 - y1) / (x2 - x1)
    return m

print("m es igual a  : " + str(pendiente(2,2,5,8)))    

pygame.init()

windows=pygame.display.set_mode((800,600))

pygame.draw.rect(windows,(12,115,103 ),(0,0,800,600))
pygame.draw.line(windows,(255,255,255),(200,300),(600,300),2)
pygame.draw.line(windows,(255,255,255),(400,100),(400,500),2)



def recta(x1,y1,x2,y2):

    x = x1

    pygame.draw.rect(windows,(238,27,200),(400 + x1 * 20,300 - y1 * 20,5,5))
    pygame.draw.rect(windows,(238,27,200),(400 + x2 * 20,300 - y2 * 20,5,5))

    for x in range (x1,x2):
         y = (pendiente(x1,y1,x2,y2) * x - 2)
         print("x = " + str(x))
         print("y = " + str(y))
         pygame.draw.rect(windows,(238,27,200),(400 + x*20,300 - y*20,5,5))
         pygame.display.update()
         
    return y

recta(2,2,5,8)
pygame.display.update()
   
time.sleep(8.8)

       