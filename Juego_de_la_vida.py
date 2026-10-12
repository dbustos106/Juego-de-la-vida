from Letras.t import imageT
from Letras.todo import imageTodo

import numpy as np
import pygame
import ctypes
import time
import os

BG = (126, 120, 119)
GRID = (143, 143, 143)
COLOR_CELDA = (62, 1, 74)

CTR = 58                      # ancho del panel de botones
LIMITE_RELOJ = 810            # frames hasta cerrar (None para desactivar)


def cargar(ruta, ancho, alto):
    img = pygame.image.load(ruta).convert_alpha()
    return pygame.transform.scale(img, (ancho, alto))


def siguiente_estado(estado):
    """Un paso del juego de la vida."""
    vecinos = sum(
        np.roll(np.roll(estado, dx, axis=0), dy, axis=1)
        for dx in (-1, 0, 1) for dy in (-1, 0, 1)
        if (dx, dy) != (0, 0)
    )
    return ((vecinos == 3) | ((estado == 1) & (vecinos == 2))).astype(estado.dtype)


def crear_cuadricula(ancho_px, alto_px, nxC, nyC, dimCW, dimCH):
    """Dibuja las líneas de la cuadrícula."""
    surf = pygame.Surface((ancho_px, alto_px), pygame.SRCALPHA)
    for x in range(nxC + 1):
        pygame.draw.line(surf, GRID, (x * dimCW, 0), (x * dimCW, alto_px))
    for y in range(nyC + 1):
        pygame.draw.line(surf, GRID, (0, y * dimCH), (ancho_px, y * dimCH))
    return surf


def dibujar_celdas(screen, estado, dimCW, dimCH, color):
    w, h = int(dimCW) + 1, int(dimCH) + 1
    for x, y in np.argwhere(estado == 1):
        screen.fill(color, (int(x * dimCW), int(y * dimCH), w, h))


def main():
    pygame.init()

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) - 65

    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (0, 27)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Juego de la vida')

    # Cargar imagenes
    pygame.display.set_icon(pygame.image.load("Imagenes/play1.png"))
    img_fondo = cargar("Imagenes/fondo.png", 57, height)
    img_contenedor = cargar("Imagenes/contenedor.png", 50, 300)
    img_puntero = cargar("Imagenes/puntero.png", 25, 20)
    img_play1 = cargar("Imagenes/play1.png", 57, 57)
    img_play2 = cargar("Imagenes/play2.png", 57, 57)
    img_reset1 = cargar("Imagenes/reset1.png", 57, 57)
    img_reset2 = cargar("Imagenes/reset2.png", 57, 57)

    # Dimensiones del mundo
    nxC, nyC = 200, 100
    dimCW = (width - CTR) / nxC
    dimCH = height / nyC
    grid = crear_cuadricula(width - CTR, height, nxC, nyC, dimCW, dimCH)

    gameState = imageT(nxC, nyC)
    pauseExect = False
    arrastrando = False
    posPuntero = 161
    tiempoClick = 0
    velocidad = 0
    reloj = 0

    en_play = lambda x, y: width - 60 < x < width and 0 < y < 57
    en_reset = lambda x, y: width - 60 < x < width and 70 < y < 127

    while True:
        time.sleep(velocidad)

        if LIMITE_RELOJ is not None and reloj == LIMITE_RELOJ:
            break

        posX, posY = pygame.mouse.get_pos()

        # ------------------ Eventos ------------------ #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                pauseExect = not pauseExect

            if event.type == pygame.MOUSEBUTTONUP:
                arrastrando = False

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            if posX < width - CTR:
                # Pintar (izq) o borrar (der) celdas
                celX = min(int(posX / dimCW), nxC - 1)
                celY = min(int(posY / dimCH), nyC - 1)
                gameState[celX, celY] = 0 if mouseClick[2] else 1

            elif en_reset(posX, posY) and not arrastrando:
                gameState = imageT(nxC, nyC)
                pauseExect = True
                reloj = 0

            elif en_play(posX, posY) and not arrastrando:
                pauseExect = False

            # Slider de velocidad
            if width - 41 < posX < width - 16:
                if posPuntero < posY < posPuntero + 20:
                    if time.time() - tiempoClick < 0.5:
                        arrastrando = True
                    tiempoClick = time.time()
                else:
                    arrastrando = True

        if arrastrando:
            posPuntero = max(161, min(415, posY))
            velocidad = (posPuntero - 161) * 0.3 / 254

        # ------------------ Actualizar ------------------ #
        if not pauseExect:
            gameState = siguiente_estado(gameState)
            reloj += 1

        # ------------------ Dibujar ------------------ #
        screen.fill(BG)
        dibujar_celdas(screen, gameState, dimCW, dimCH, COLOR_CELDA)
        screen.blit(grid, (0, 0))

        screen.blit(img_fondo, (width - 57, 0))
        screen.blit(img_contenedor, (width - 54, 150))
        pygame.draw.rect(screen, GRID, (width - 41, 161, 25, abs(posPuntero - 160)))
        screen.blit(img_puntero, (width - 41, posPuntero))

        if en_play(posX, posY):
            screen.blit(img_play2, (width - 57, 0))
            screen.blit(img_reset1, (width - 57, 70))
        elif en_reset(posX, posY):
            screen.blit(img_play1, (width - 57, 0))
            screen.blit(img_reset2, (width - 57, 70))
        else:
            screen.blit(img_play1, (width - 57, 0))
            screen.blit(img_reset1, (width - 57, 70))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
