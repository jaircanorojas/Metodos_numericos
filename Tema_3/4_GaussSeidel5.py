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

# Matriz de conectividad de tuberías
A = np.array([[4, -1, -1, 0], 
               [-1, 4, 0, -1], 
               [-1, 0, 4, -1], 
               [0, -1, -1, 4]], dtype=float)
b = np.array([100, 50, 50, 0], dtype=float)
x0 = np.zeros(4)

presiones, it = gauss_seidel(A, b, x0, 1e-4, 100)

print("--- Ejercicio 5: Presiones en Tuberías ---")
print(f"Presión en cada nodo: {presiones}")
print(f"Convergencia en {it} iteraciones.")