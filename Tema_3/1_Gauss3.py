import numpy as np

# Sistema derivado de mallas eléctricas
# Ecuaciones:
#  10*I1 - 2*I2 - 3*I3 = 10
# -2*I1 + 8*I2 - 1*I3 = -5
# -3*I1 - 1*I2 + 6*I3 = 0

A_circuit = np.array([[10, -2, -3],
                      [-2, 8, -1],
                      [-3, -1, 6]], dtype=float)

b_circuit = np.array([10, -5, 0], dtype=float)

corrientes = np.linalg.solve(A_circuit, b_circuit)

print("--- Ejercicio 3: Análisis de Circuitos ---")
for i, current in enumerate(corrientes, 1):
    print(f"Corriente I{i}: {current:.4f} Amperios")