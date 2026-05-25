import numpy as np
from Lagrange_Master import interpolacion_lagrange

# Puntos de sin(x) en radianes
x = np.array([0, np.pi/4, np.pi/2])
y = np.sin(x)

x_target = np.pi/6 # 30 grados
estimado = interpolacion_lagrange(x, y, x_target)

print(f"Ejercicio 2.2 - sin(pi/6) estimado: {estimado:.4f}")
print(f"Valor real: {np.sin(x_target):.4f}")