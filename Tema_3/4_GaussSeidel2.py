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
    return x, k + 1

# Sistema con diagonal débil (puede no converger)
A = np.array([[1, 2, 10], [10, 1, 1], [1, 10, 1]], dtype=float)
b = np.array([13, 12, 12], dtype=float)
x0 = np.zeros(len(b))

solucion, iteraciones = gauss_seidel(A, b, x0, 1e-5, 20)

print("--- Ejercicio 2: Impacto del Orden ---")
print(f"Resultado tras {iteraciones} iteraciones: {solucion}")
print("Nota: Si los valores son gigantes o NaN, el sistema divergió.")