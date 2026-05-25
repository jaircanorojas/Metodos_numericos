import numpy as np
from Lagrange_Master import interpolacion_lagrange

# Temperatura vs Resistencia (Ohms)
temp = np.array([20, 50, 80, 110])
resistencia = np.array([105.2, 118.5, 132.8, 147.1])

t_objetivo = 75
resultado = interpolacion_lagrange(temp, resistencia, t_objetivo)

print(f"Ejercicio 2.4 - Resistencia a {t_objetivo}°C: {resultado:.2f} Ohms")