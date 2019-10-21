import pygame
from pygame.locals import *
import sys

SCREEN_WIDH = 616
SCREEN_HEIGHT = 681

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDH,SCREEN_HEIGHT))
    pygame.display.set_caption("Manejo de imagenes")

    fondo = pygame.image.load("tablero.jpeg").convert()
    pacman = pygame.image.load("pacman.jpeg").convert_alpha()

    pacman_pos_x = 557
    pacman_pos_y = 106

    screen.blit(pacman,(pacman_pos_x,pacman_pos_y))
    screen.blit(fondo,(0,0))

    pygame.display.flip()

    while True:

        #pacman_pos_x = pacman_pos_x -1
        if pacman_pos_x < 1:
            pacman_pos_x = 557

        screen.blit(fondo,(0,0))
        screen.blit(pacman,(pacman_pos_x,pacman_pos_y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                pacman_pos_x = pacman_pos_x - 2  

if __name__ == "__main__":
    main()