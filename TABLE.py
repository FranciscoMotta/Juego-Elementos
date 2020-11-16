# Escribe tu código aquí :-)
# Iniciamos el Pygame

import pygame
import math
import random

pygame.init()

# Creamos la pantalla
#                                ancho alto
screen = pygame.display.set_mode((800, 600))

# 0,0 en la parte superior izquierda de la pantalla

# Fondo de pantalla

fondo = pygame.image.load('fondo.png')

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
jugadorY = 500
jugadorX_change = 0

# Tablas

tablaImag = pygame.image.load('excel.png')
tablaX = 0
tablaY = 480
tablaX_change = 0
tablaY_change = 5
tabla_estado = "listo"


# Añadimos a Luchos

LuchoImag = []
LuchoX = []
LuchoY = []
LuchoX_change = []
LuchoY_change = []
numero_de_luchos = 6


for counter in range(numero_de_luchos):
    LuchoImag.append(pygame.image.load('Lucho.png'))
    LuchoX.append(random.randint(0,735))
    LuchoY.append(random.randint(30,100))
    LuchoX_change.append(3)
    LuchoY_change.append(40)

# Puntuación

puntaje_valor = 0

font = pygame.font.Font('freesansbold.ttf', 32)

puntosX = 10
puntosY = 10

def mostrar_puntaje(x,y):
    puntaje = font.render("La nota de Lucho es: " + str(puntaje_valor), True, (255,255,255))
    screen.blit(puntaje, (x,y))

def jugador(x,y):
    screen.blit(jugadorImag, (x, y))

def Lucho(x,y, counter):
    screen.blit(LuchoImag[counter], (x, y))

def mandar_excel(x,y):
    global tabla_estado
    tabla_estado = "disparar"
    screen.blit(tablaImag, (x , y + 10))


# Impacto

def yaLlego(LuchoX, LuchoY, tablaX, tablaY):
    # Sabemos que: Distancia entre 2 puntos == D = raíz((x2-x1)^2 - (y2-y1)^2)
    # Ese análisis se aplicar con la librería de métodos matemáticos
    distancia = math.sqrt((math.pow(LuchoX - tablaX,2)) + (math.pow (LuchoY - tablaY, 2)))
    if distancia < 27:
        return True
    else:
        return False
# Bucle del juego
running = True
while running:

    # Color fondo R  G  B
    screen.fill((255,243,170))

    # Imagen de fondo

    screen.blit(fondo, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Vemos si las flechas se precionan <- o ->
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
    #            print("izquierda presionada")
                jugadorX_change = -3
            if event.key == pygame.K_RIGHT:
    #            print("derecha presionada")
                jugadorX_change = +3
            if event.key == pygame.K_SPACE:
                if tabla_estado is "listo":
                    tablaX = jugadorX
                    mandar_excel(jugadorX, tablaY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #            print("Tecla soltada")
                jugadorX_change = 0

# Mi movimiento
    jugadorX += jugadorX_change

    if jugadorX <= 0:
        jugadorX = 0
    elif jugadorX >= 743:
        jugadorX = 743

# Movimiento de Lucho
    for counter in range(numero_de_luchos):
        LuchoX[counter] += LuchoX_change[counter]
        if LuchoX[counter] <= 0:
            LuchoX_change[counter] = 2
            LuchoY[counter] += LuchoY_change[counter]
        elif LuchoX[counter] >= 743:
            LuchoX_change[counter] = -2
            LuchoY[counter] += LuchoY_change[counter]
        # Impacto

        yaLlegoTabla = yaLlego(LuchoX[counter], LuchoY[counter], tablaX, tablaY)

        if yaLlegoTabla: # Si ya llego la bala
            tablaY = 480
            tabla_estado = "listo"
            puntaje_valor += 1
            LuchoX[counter] = random.randint(0,735)
            LuchoY[counter] = random.randint(30,100)

        Lucho(LuchoX[counter], LuchoY[counter], counter)

# Movimiento del Excel
    if tablaY <= 0:
        tablaY = 480
        tabla_estado = "listo"
    if tabla_estado is "disparar":
        mandar_excel(tablaX, tablaY)
        tablaY -= tablaY_change


    jugador(jugadorX,jugadorY)
    mostrar_puntaje(puntosX, puntosY)
    pygame.display.update()
