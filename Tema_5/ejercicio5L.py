import numpy as np
from Lagrange_Master import interpolacion_lagrange

# Tiempo (s) vs Altura (m)
tiempo = np.array([0, 1.5, 3.0, 4.5, 6.0])
altura = np.array([0, 42.5, 70.2, 85.4, 90.0])

t_eval = 2.0
h_estimada = interpolacion_lagrange(tiempo, altura, t_eval)

print(f"Ejercicio 2.5 - Altura a los {t_eval}s: {h_estimada:.2f} metros")