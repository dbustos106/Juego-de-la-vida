import numpy as np
from Letras.s import imageS

gameState = imageS(200, 150)
coords = np.argwhere(gameState == 1)

# Desplazar S 300 unidades hacia la derecha (+x)
coords[:, 0] += 390

for x, y in coords:
    print(f"gameState[{x}, {y}] = 1")