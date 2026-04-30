import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - suma) / A[i][i]
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, k + 1
    return x, max_iter

# Sistema bien condicionado
A = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]], dtype=float)
b = np.array([-1, 2, 3], dtype=float)
x0 = np.zeros(len(b))

# Tolerancia muy estricta (10^-10)
solucion, iteraciones = gauss_seidel(A, b, x0, 1e-10, 1000)

print("--- Ejercicio 3: Tolerancia Estricta ---")
print(f"Solución: {solucion}")
print(f"Iteraciones necesarias: {iteraciones}")