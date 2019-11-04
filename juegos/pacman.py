import pygame
from pygame.locals import *
import sys
import time
import matriz as mt

SCREEN_WIDH = 615
SCREEN_HEIGHT = 680

def main():
    pygame.init()
    pospacman = [2,3]

    screen = pygame.display.set_mode((SCREEN_WIDH,SCREEN_HEIGHT))
    pygame.display.set_caption("Manejo de imagenes")

    fondo = pygame.image.load("tablero.jpeg").convert()
    pacman = pygame.image.load("LEFT.jpeg").convert_alpha()

    pygame.mixer.music.load('soud.wav')

    def imagen(imagen):
        pacman = pygame.image.load(imagen).convert_alpha()
        screen.blit(fondo,(0,0))
        screen.blit(pacman,(pacman_pos_x,pacman_pos_y))
        pygame.display.flip()

    pacman_pos_x = 15
    pacman_pos_y = 15

    screen.blit(pacman,(pacman_pos_x,pacman_pos_y))
    screen.blit(fondo,(0,0))

    pygame.display.flip()

    screen.blit(fondo,(0,0))
    screen.blit(pacman,(pacman_pos_x,pacman_pos_y))
    pygame.display.flip()

    while True:

        #pacman_pos_x = pacman_pos_x -1
                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                imagen("LEFT.jpeg")
                vandera = mt.mapa(pospacman,1)

                if (vandera[0]):
                    pacman_pos_x = pacman_pos_x - 5
                    pospacman = vandera[1]
                    time.sleep(0.1) 
                    pygame.mixer.music.play(0)
                    print ("Izquierda")

            if event.key == K_RIGHT:
                imagen("RIGHT.jpeg")
                vandera = mt.mapa(pospacman,0)

                if (vandera[0]):
                    pacman_pos_x = pacman_pos_x + 5
                    pospacman = vandera[1]
                    time.sleep(0.1)
                    pygame.mixer.music.play(0)
                    print ("Derecha")

            if event.key == K_DOWN:
                imagen("DOWN.jpeg")
                vandera = mt.mapa(pospacman,2)

                if (vandera[0]):
                    pacman_pos_y = pacman_pos_y + 5
                    pospacman = vandera[1]
                    time.sleep(0.1)
                    pygame.mixer.music.play(0)
                    print ("Abajo") 

            if event.key == K_UP:
                imagen("UP.jpeg")
                vandera = mt.mapa(pospacman,3)

                if (vandera[0]):
                    pacman_pos_y = pacman_pos_y - 5
                    pospacman = vandera[1]
                    time.sleep(0.1)
                    pygame.mixer.music.play(0)
                print ("Arriba")

if __name__ == "__main__":
    main()