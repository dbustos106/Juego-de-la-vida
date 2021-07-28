from Letras.t import imageT
from Letras.e import imageE
from Letras.a import imageA
from Letras.m import imageM
from Letras.o import imageO
from Letras.todo import imageTodo
import numpy as np
import pygame
import ctypes
import time
import os


"""
Función que imprime botones
"""
def botton(screen, dir, posX, posY, width, height):
    imagen = pygame.image.load(dir)
    picture = pygame.transform.scale(imagen, [width, height])
    screen.blit(picture, [posX, posY])


"""
Función que actualiza filas
"""
def actualizarColum():

    for x in range(0, nxC):
        for y in range(0, nyC):

            # Si no hay pausa, actualiza los estados
            if not pauseExect:
                n_neigh  =  gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                            gameState[(x)  % nxC   , (y - 1) % nyC] + \
                            gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                            gameState[(x - 1) % nxC, (y) % nyC] + \
                            gameState[(x + 1) % nxC, (y) % nyC] + \
                            gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                            gameState[(x) % nxC    , (y + 1) % nyC] + \
                            gameState[(x + 1) % nxC, (y + 1) % nyC]

                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            # Crear los poligonos
            poly = [((x)     * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH), 
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x)     * dimCW, (y + 1) * dimCH)]

            # Imprimir las celdas
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (143, 143, 143), poly, 1)
            else:
                pygame.draw.polygon(screen, (r,g,b), poly, 0)
                pygame.draw.polygon(screen, (143, 143, 143), poly, 1)


if __name__ == '__main__':

    pygame.init()
    pygame.mixer.init()
    
    # Cargar musica
    pygame.mixer.music.load("Canciones/chachacha.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play()

    # Calcular las dimensiones de la ventana
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) - 30

    # Crear la ventana del juego
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (0, 30)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Juego de la vida')

    # Cambiar el icono
    icono = pygame.image.load("Imagenes/play1.png")
    pygame.display.set_icon(icono)

    bg = 126, 120, 119
    screen.fill(bg)
    
    # Calcular las dimensiones de las celdas
    ctr, nxC, nyC = 58, 200, 100
    dimCW = (width - ctr) / nxC
    dimCH = height / nyC

    r, g, b = 62, 1, 74

    # Inicializar el estado del juego
    gameState = imageT(nxC, nyC)
    cambiarPosPuntero = False
    pauseExect = False
    posPuntero = 161
    tiempoClick = 0
    velocidad = 0
    reloj = 0
    
    while True:

        screen.fill(bg)
        time.sleep(velocidad)



        ### ------------------ Cambiar escenario ------------------ ###

        if reloj == 225:

            r,g, b = 5, 64, 0
            nxC, nyC = 200, 100
            dimCH = height / nyC
            dimCW = (width - ctr) / nxC
            gameState = imageE(nxC, nyC)

        elif reloj == 337:

            r,g, b = 12, 0, 89
            nxC, nyC = 200, 96
            dimCH = height / nyC
            dimCW = (width - ctr) / nxC
            gameState = imageA(nxC, nyC)

        elif reloj == 507:

            r,g, b = 46, 0, 6
            nxC, nyC = 200, 100
            dimCH = height / nyC
            dimCW = (width - ctr) / nxC
            gameState = imageM(nxC, nyC)

        elif reloj == 698:

            r,g, b = 0, 43, 11
            nxC, nyC = 200, 100
            dimCH = height / nyC
            dimCW = (width - ctr) / nxC
            gameState = imageO(nxC, nyC)
            
        elif reloj == 750:

            # Cambiar canción
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Canciones/SiHayAlgo.mp3")
            pygame.mixer.music.play()
            r,g, b = 61, 1, 42
            nxC, nyC = 600, 250
            dimCH = height / nyC
            dimCW = (width - ctr) / nxC
            gameState = imageTodo(nxC, nyC)

        elif reloj == 810:
            pygame.quit()
            exit()
                    


        # Copiar el estado del juego
        newGameState = np.copy(gameState)

        # Obtener la posicicón del mouse
        posX, posY = pygame.mouse.get_pos()



        ### ------------------ Capturar eventos ------------------ ###

        for event in pygame.event.get():

            ##  Detener la actualización de las celdas ##
            if event.type == pygame.KEYDOWN:
                pauseExect = not pauseExect
                if pauseExect:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            ## Detectar cuando se hace click ##
            mouseClick = pygame.mouse.get_pressed()
            
            if sum(mouseClick) > 0:    

                ## Cambiar manualmente el estado de las celdas
                if posX < width - ctr:
                    celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
                    newGameState[celX, celY] = not mouseClick[2]

                ## Resetear 
                elif (width-60 < posX and posX < width) and (70 < posY and posY < 127) and (cambiarPosPuntero == False):
                    nxC, nyC = 200, 100
                    r, g, b = 62, 1, 74
                    dimCH = height / nyC
                    dimCW = (width - ctr) / nxC
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("Canciones/chachacha.mp3")
                    pygame.mixer.music.play()
                    pygame.mixer.music.pause()
                    gameState = np.zeros((nxC, nyC))
                    newGameState = imageT(nxC, nyC)
                    pauseExect = True
                    reloj = 0

                ## Play
                if (width-60 < posX and posX < width) and (0 < posY and posY < 57) and (cambiarPosPuntero == False):
                    pygame.mixer.music.unpause()
                    pauseExect = False

                ## Cambiar velocidad
                if (width-41 < posX and posX < width-16):
                    if (posPuntero < posY and posY < posPuntero+20):
                        if time.time() - tiempoClick < 0.5:
                            cambiarPosPuntero = True
                        tiempoClick = time.time()
                    else:
                        cambiarPosPuntero = True

            ## Detectar cuando se suelta el click ##
            if event.type == pygame.MOUSEBUTTONUP:  
                cambiarPosPuntero = False

            ## Cerrar la ventana ##
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



        ### ------------------ Cambiar botones ------------------ ###

        botton(screen, "Imagenes/fondo.png", width-57, 0, 57, height)

        if (cambiarPosPuntero == True) and (161 < posY and posY < 415):
            posPuntero = posY
            velocidad = (posPuntero - 161) * 0.3/254
        elif (cambiarPosPuntero == True) and (posY < 161):
            posPuntero = 161
            velocidad = (posPuntero - 161) * 0.3/254
        elif (cambiarPosPuntero == True) and (415 < posY):
            posPuntero = 415
            velocidad = (posPuntero - 161) * 0.3/254
        
        botton(screen, "Imagenes/contenedor.png", width-54, 150, 50, 300)
        botton(screen, "Imagenes/barraGris.png", width-41, 161, 25, abs(posPuntero - 160))
        botton(screen, "Imagenes/puntero.png", width-41, posPuntero, 25, 20)

        # Play
        if (width-60 < posX and posX < width) and (0 < posY and posY < 57):
            botton(screen, "Imagenes/play2.png", width-57, 0, 57, 57)
            botton(screen, "Imagenes/reset1.png", width-57, 70, 57, 57)
        # Reset
        elif (width-60 < posX and posX < width) and (70 < posY and posY < 127):
            botton(screen, "Imagenes/play1.png", width-57, 0, 57, 57)
            botton(screen, "Imagenes/reset2.png", width-57, 70, 57, 57)
        else:
            botton(screen, "Imagenes/play1.png", width-57, 0, 57, 57)
            botton(screen, "Imagenes/reset1.png", width-57, 70, 57, 57)



        ### ------------------ Actualización de estados ------------------ ###
        actualizarColum()



        ### ------------------ Actualiza el estado de las celdas ------------------ ###
        gameState = np.copy(newGameState)
        pygame.display.flip()



        if not pauseExect:
            reloj = reloj + 1
    