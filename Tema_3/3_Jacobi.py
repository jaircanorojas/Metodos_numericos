import numpy as np

def jacobi(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.astype(float)
    
    for k in range(max_iter):
        x_nuevo = np.zeros(n)
        for i in range(n):
            suma = sum(A[i, j] * x[j] for j in range(n) if i != j)
            x_nuevo[i] = (b[i] - suma) / A[i, i]
        
        if np.linalg.norm(x_nuevo - x, ord=np.inf) < tol:
            return x_nuevo
        x = x_nuevo
    return x

# Ejemplo de uso
A = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]])
b = np.array([7, -8, 6])
x0 = np.zeros(3)
print("Solución Jacobi:", jacobi(A, b, x0, 0.0001, 100))