import numpy as np

def eliminacion_gaussiana(A, b):
    n = len(b)
    # Matriz aumentada
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)

    # Fase de eliminación
    for i in range(n):
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, n] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    return x

# Ejemplo de uso
A = np.array([[3, 2, 1], [5, 3, 4], [1, 1, -1]])
b = np.array([1, 2, 1])
print("Solución Gauss:", eliminacion_gaussiana(A, b))