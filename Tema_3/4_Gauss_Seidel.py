import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.astype(float)
    
    for k in range(max_iter):
        x_viejo = np.copy(x)
        for i in range(n):
            suma = sum(A[i, j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - suma) / A[i, i]
        
        if np.linalg.norm(x - x_viejo, ord=np.inf) < tol:
            return x
    return x

# Ejemplo de uso
A = np.array([[4, 1, 2], [1, 3, 1], [1, 2, 5]])
b = np.array([16, 10, 12])
x0 = np.zeros(3)
print("Solución Gauss-Seidel:", gauss_seidel(A, b, x0, 0.0001, 100))