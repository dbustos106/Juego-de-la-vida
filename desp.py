import numpy as np
from Letras.arco import imageArco

gameState = imageArco(200, 150)
coords = np.argwhere(gameState == 1)

# Simetría en x, manteniendo y
coords[:, 0] = coords[:, 0].min() + coords[:, 0].max() - coords[:, 0]

for x, y in coords:
    print(f"gameState[{x}, {y}] = 1")