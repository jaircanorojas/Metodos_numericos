import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)

    for i in range(n):
        # Normalizar fila del pivote
        Ab[i] = Ab[i] / Ab[i, i]
        # Eliminar otros elementos de la columna
        for j in range(n):
            if i != j:
                factor = Ab[j, i]
                Ab[j] -= factor * Ab[i]
    
    return Ab[:, n]

# Ejemplo de uso
A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])
print("Solución Gauss-Jordan:", gauss_jordan(A, b))