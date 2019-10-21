# coding=utf-8

# importa la librería Pygame
import pygame


def main():
    # inicializa Pygame
    pygame.init()

    # establece el título de la ventana
    pygame.display.set_caption(u'Eventos del teclado')

    # establece el tamaño de la ventana
    pygame.display.set_mode((400, 400))

    # bucle infinito
    while True:
        # obtiene un solo evento de la cola de eventos
        event = pygame.event.wait()

        # si se presiona el botón 'cerrar' de la ventana
        if event.type == pygame.QUIT:
            # detiene la aplicación
            break

        # captura los eventos 'KEYDOWN' y 'KEYUP'
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            # obtiene el nombre de la tecla
            key_name = pygame.key.name(event.key)

            # convierte el nombre de la tecla en mayúsculas
            key_name = key_name.upper()

            # si alguna tecla es presionada
            if event.type == pygame.KEYDOWN:
                # imprime en la consola la tecla presionada
                print u'Tecla "{}" presionada'.format(key_name)

            # si alguna tecla es soltada
            elif event.type == pygame.KEYUP:
                # imprime en la consola la tecla soltada
                print u'Tecla "{}" soltada'.format(key_name)

    # finaliza Pygame
    pygame.quit()


if __name__ == '__main__':
    main()