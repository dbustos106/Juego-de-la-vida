import numpy as np
from Letras.z import imageZ

gameState = imageZ(200, 150)
coords = np.argwhere(gameState == 1)

# Desplazar la figura a la esquina superior izquierda (0, 0)
coords[:, 0] -= coords[:, 0].min()
coords[:, 1] -= coords[:, 1].min()

for x, y in coords:
    print(f"gameState[{x}, {y}] = 1")