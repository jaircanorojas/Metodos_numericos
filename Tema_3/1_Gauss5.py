import numpy as np

# Sistema 4x4 aleatorio pero con diagonal dominante para asegurar convergencia
A_4x4 = np.array([[10, -1, 2, 0],
                  [-1, 11, -1, 3],
                  [2, -1, 10, -1],
                  [0, 3, -1, 8]], dtype=float)

b_4x4 = np.array([6, 25, -11, 15], dtype=float)

sol_4x4 = np.linalg.solve(A_4x4, b_4x4)

print("--- Ejercicio 5: Sistema 4x4 ---")
print(f"Solución del sistema: {sol_4x4}")