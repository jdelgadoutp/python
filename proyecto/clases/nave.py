import pygame
import proyectil


class naveEspacial(pygame.sprite.Sprite):
    """Clase para las naves"""

    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load('imagenes/nave.jpg')
        self.ImagenExplosion = pygame.image.load('imagenes/explosion.jpg')
        
        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-30

        self.listaDisparo=[]
        self.Vida = True
        self.velocidad = 30

        self.sonidoDisparo = pygame.mixer.Sound("sonidos/disparo.wav")
        self.sonidoExplosion = pygame.mixer.Sound("sonidos/explosion.wav")

    def movimientoDerecha(self):
        self.rect.right += self.velocidad
        self.__movimiento()

    def movimientoIzquierda(self):
        self.rect.left -= self.velocidad
        self.__movimiento()       

    def __movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rect.right > 900:
                self.rect.right = 900        

    def disparar(self,x,y):
        miProyectil = proyectil.Proyectil(x,y,"imagenes/disparoa.jpg",True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()

    def destruccion(self):
        self.sonidoExplosion.play()
        self.Vida = False
        self.velocidad = 0
        self.ImagenNave = self.ImagenExplosion

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)    
