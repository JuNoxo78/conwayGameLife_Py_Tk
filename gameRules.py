import numpy as np
from scipy.signal import convolve2d

FILAS = 30
COLUMNAS = 50

historia = [np.zeros((FILAS, COLUMNAS), dtype=int)]
index_iteration = 0

kernel = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])

def siguiente_generacion(universo):
    global index_iteration

    if index_iteration == len(historia) - 1 :
        # Contar los vecinos vivos usando convolución
        vecinos_vivos = convolve2d(universo, kernel, mode='same', boundary='wrap')

        # Aplicar las reglas del Juego de la Vida
        nueva_generacion = np.where((universo == 1) & ((vecinos_vivos == 2) | (vecinos_vivos == 3)), 1, 0)
        nueva_generacion = np.where((universo == 0) & (vecinos_vivos == 3), 1, nueva_generacion)
        historia.append(nueva_generacion)
        index_iteration += 1
        return nueva_generacion
    index_iteration += 1
    return historia[index_iteration]

def anterior_generacion():
    global index_iteration
    if index_iteration == 0:
        return historia[index_iteration]
    else:
        index_iteration -= 1
    return historia[index_iteration]