import pygame
import transforma as t

Ancho = 600
Alto = 600
Verde = [0,255,0]
Azul = [0,0,255]
Rojo = [250,0,0]
Blanco = [255,255,255]
Negro = [0,0,0]

if __name__=='__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([Ancho,Alto])
    a = [150,100]
    b = [400,100]
    pygame.draw.line(pantalla,Verde,[300,0],[300,600])
    pygame.draw.line(pantalla,Verde,[0,300],[600,300])
    pygame.display.flip()
    reloj = pygame.time.Clock()
    cont = 0
    e = [2,2]
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if cont < 3:
                    if cont == 0:
                        p1 = list(event.pos)
                        q1 = t.escalar(p1,e)
                        print (p1,e)
                        cont += 1
                    elif cont == 1:
                        p2 = list(event.pos)
                        q2 = t.escalar(p2,e)
                        print (p2,q2)
                        cont +=1
                    elif cont == 2:
                        p3 = list(event.pos)
                        q3 = t.escalar(p3,e)
                        print (p3,q3)
                        cont += 1
                    if cont == 3:
                        pygame.draw.line(pantalla,Blanco,p1,p2)
                        pygame.draw.line(pantalla,Blanco,p2,p3)
                        pygame.draw.line(pantalla,Blanco,p3,p1)

                        pygame.draw.line(pantalla,Azul,q1,q2)
                        pygame.draw.line(pantalla,Azul,q2,q3)
                        pygame.draw.line(pantalla,Azul,q3,q1)

                        pygame.display.flip()

                reloj.tick(30)





