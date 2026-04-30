import numpy as np

# Definimos la matriz A y el vector de resultados B
A = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]], dtype=float)

b = np.array([7.85, -19.3, 71.4], dtype=float)

# Resolvemos usando el método de eliminación de Gauss (vía NumPy)
x = np.linalg.solve(A, b)

print("--- Ejercicio 1: Sistema 3x3 ---")
print(f"Solución: {x}")