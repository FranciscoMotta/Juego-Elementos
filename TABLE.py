# Escribe tu código aquí :-)
# Iniciamos el Pygame

import pygame
import time

pygame.init()

# Creamos la pantalla
#                                ancho alto
screen = pygame.display.set_mode((800, 600))

# 0,0 en la parte superior izquierda de la pantalla

# Titulo e ícono
pygame.display.set_caption("Element's table")
# Añadimos el ícono a la carpeta
# Seleccionamos el icono en la variable
icon = pygame.image.load('teacher.png')
# Desplegamos la seleccion anterior
pygame.display.set_icon(icon)

# Jugador

jugadorImag = pygame.image.load('Yo.png')
jugadorX = 470
jugadorY = 470
jugadorX_change = 0
def jugador(x,y):
    screen.blit(jugadorImag, (x, y))

# Bucle del juego
running = True
while running:

    # Color fondo R  G  B
    screen.fill((255,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Vemos si las flechas se precionan <- o ->
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("izquierda presionada")
                jugadorX_change = -0.2
            if event.key == pygame.K_RIGHT:
                print("derecha presionada")
                jugadorX_change = +0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Tecla soltada")
                jugadorX_change = 0

    jugadorX += jugadorX_change

    if jugadorX <= 0:
        jugadorX = 0
    elif jugadorX >= 742:
        jugadorX = 742

    jugador(jugadorX,jugadorY)
    pygame.display.update()
