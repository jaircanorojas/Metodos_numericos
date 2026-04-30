import numpy as np

def jacobi(A, b, x0, tol, max_iter):
    D = np.diag(np.diag(A))
    R = A - D
    x = x0
    for i in range(max_iter):
        x_new = np.linalg.solve(D, b - np.dot(R, x))
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

# Sistema 3x3 estándar
A1 = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]], dtype=float)
b1 = np.array([6, 25, -11], dtype=float)
x_ini = np.zeros(3)

sol, it = jacobi(A1, b1, x_ini, 1e-5, 100)
print(f"Ejercicio 1: Solución {sol} encontrada en {it} iteraciones.")