import numpy as np
from Lagrange_Master import interpolacion_lagrange

# Usando los mismos datos que el Ejercicio 1 de Newton
x = np.array([1.0, 4.0, 6.0])
y = np.log10(x)

res_lagrange = interpolacion_lagrange(x, y, 2.5)

print(f"Ejercicio 2.3 - Resultado con Lagrange: {res_lagrange:.4f}")
print("Verifica con el Ejercicio 1.1 de Newton, ¡deben ser iguales!")