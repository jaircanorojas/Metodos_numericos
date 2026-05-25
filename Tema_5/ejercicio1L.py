import numpy as np
from Lagrange_Master import interpolacion_lagrange

# Datos de una función cuadrática desconocida
x = np.array([1, 3, 5])
y = np.array([2, 10, 26])

x_interp = 4
resultado = interpolacion_lagrange(x, y, x_interp)

print(f"Ejercicio 2.1 - Valor en x={x_interp}: {resultado}")