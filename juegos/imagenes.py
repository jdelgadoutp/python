import pygame
from pygame.locals import *
import sys
import time

SCREEN_WIDH = 615
SCREEN_HEIGHT = 680

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDH,SCREEN_HEIGHT))
    pygame.display.set_caption("Manejo de imagenes")

    fondo = pygame.image.load("tablero.jpeg").convert()
    pacman = pygame.image.load("RIGHT.jpeg").convert_alpha()

    pygame.mixer.music.load('soud.wav')

    def imagen(imagen):
        pacman = pygame.image.load(imagen).convert_alpha()
        screen.blit(fondo,(0,0))
        screen.blit(pacman,(pacman_pos_x,pacman_pos_y))
        pygame.display.flip()

    pacman_pos_x = 557
    pacman_pos_y = 106

    screen.blit(pacman,(pacman_pos_x,pacman_pos_y))
    screen.blit(fondo,(0,0))

    pygame.display.flip()

    while True:

        #pacman_pos_x = pacman_pos_x -1
        if pacman_pos_x < 1:
            pacman_pos_x = 557
        if pacman_pos_x > 557:
            pacman_pos_x = 1
        if pacman_pos_y > 681:
            pacman_pos_y = 1
        if pacman_pos_y < 1:
            pacman_pos_y = 681            

        screen.blit(fondo,(0,0))
        screen.blit(pacman,(pacman_pos_x,pacman_pos_y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                imagen("LEFT.jpeg")
                pacman_pos_x = pacman_pos_x - 5
                time.sleep(0.1) 
                pygame.mixer.music.play(0)
                print ("Izquierda")
            if event.key == K_RIGHT:
                imagen("RIGHT.jpeg")
                pacman_pos_x = pacman_pos_x + 5
                time.sleep(0.1)
                pygame.mixer.music.play(0)
                print ("Derecha")
            if event.key == K_DOWN:
                imagen("DOWN.jpeg")
                pacman_pos_y = pacman_pos_y + 5
                time.sleep(0.1)
                pygame.mixer.music.play(0)
                print ("Abajo") 
            if event.key == K_UP:
                imagen("UP.jpeg")
                pacman_pos_y = pacman_pos_y - 5
                time.sleep(0.1)
                pygame.mixer.music.play(0)
                print ("Arriba")

if __name__ == "__main__":
    main()