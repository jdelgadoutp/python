# coding=utf-8

# importa la librería Pygame
import pygame


def main():
    # inicializa Pygame
    pygame.init()

    # establece el título de la ventana
    pygame.display.set_caption(u'Eventos del mouse')

    # establece el tamaño de la ventana
    pygame.display.set_mode((800, 600))

    # bucle infinito
    while True:
        # obtiene un solo evento de la cola de eventos
        event = pygame.event.wait()

        # si se presiona el botón 'cerrar' de la ventana
        if event.type == pygame.QUIT:
            # detiene la aplicación
            break

        # si algún botón del mouse es presionado
        if event.type == pygame.MOUSEBUTTONDOWN:
            # imprime en la consola el botón presionado y su posición en ese momento
            print u'boton {} presionado en la posicion {}'.format(event.button, event.pos)

        # si algún botón del mouse es soltado
        if event.type == pygame.MOUSEBUTTONUP:
            # imprime en la consola el botón soltado y su posición en ese momento
            print u'boton {} soltado en la posicion {}'.format(event.button, event.pos)

        # si el mouse es movido
        if event.type == pygame.MOUSEMOTION:
            # imprime en la consola los botones presionados, y su posición y movimiento relativo en ese momento
            print u'botones presionados {}, posicion {} y movimiento relativo {}'.format(event.buttons, event.pos, event.rel)

    # finaliza Pygame
    pygame.quit()


if __name__ == '__main__':
    main()