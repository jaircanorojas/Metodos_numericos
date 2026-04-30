import numpy as np

# Matriz de Hilbert 4x4 (clásico ejemplo de mal condicionamiento)
from scipy.linalg import hilbert

n = 4
A_mal = hilbert(n)
# Definimos b tal que la solución exacta sea [1, 1, 1, 1]
b_mal = np.sum(A_mal, axis=1)

# Calculamos el número de condición
cond_number = np.linalg.cond(A_mal)

# Resolvemos
x_calc = np.linalg.solve(A_mal, b_mal)

print("--- Ejercicio 4: Matriz Mal Condicionada ---")
print(f"Número de condición de la matriz: {cond_number:.2e}")
print(f"Solución calculada: {x_calc}")
print("> Nota: Si el número de condición es muy alto, la precisión disminuye.")