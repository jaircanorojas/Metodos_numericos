import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            # Suma de los elementos ya actualizados y los anteriores
            suma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - suma) / A[i][i]
        
        # Comprobar convergencia
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, k + 1
    return x, max_iter

# Datos del sistema
A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]], dtype=float)
b = np.array([6, 25, -11], dtype=float)
x0 = np.zeros(len(b))

solucion, iteraciones = gauss_seidel(A, b, x0, 1e-5, 100)

print("--- Ejercicio 1: Gauss-Seidel Estándar ---")
print(f"Solución: {solucion}")
print(f"Iteraciones: {iteraciones}")