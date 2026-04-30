import numpy as np

def jacobi(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x_new[i] = (b[i] - suma) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1
        x = x_new
    return x, max_iter

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

A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]], dtype=float)
b = np.array([6, 25, -11], dtype=float)
x0 = np.zeros(len(b))

_, it_j = jacobi(A, b, x0, 1e-5, 100)
_, it_gs = gauss_seidel(A, b, x0, 1e-5, 100)

print("--- Ejercicio 4: Comparación ---")
print(f"Iteraciones Jacobi: {it_j}")
print(f"Iteraciones Gauss-Seidel: {it_gs}")