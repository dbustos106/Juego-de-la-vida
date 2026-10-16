import numpy as np
from Letras.i import imageI

gameState = imageI(200, 150)
coords = np.argwhere(gameState == 1)

print(f"Alto de I: {coords[:, 1].max() - coords[:, 1].min() + 1}")