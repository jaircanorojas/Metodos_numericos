import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    # Matriz aumentada
    ab = np.column_stack((A, b)).astype(float)
    
    for i in range(n):
        # Escalar el pivote a 1
        ab[i] = ab[i] / ab[i, i]
        # Hacer ceros en toda la columna (arriba y abajo)
        for j in range(n):
            if i != j:
                factor = ab[j, i]
                ab[j] -= factor * ab[i]
    return ab[:, -1]

A1 = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b1 = np.array([8, -11, -3])
print(f"Solución Ejercicio 1: {gauss_jordan(A1, b1)}")