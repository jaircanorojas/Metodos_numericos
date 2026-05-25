import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Newton_Master import diferencias_divididas, evaluar_newton

# Temperatura (C) vs Viscosidad (10^-3 Pa*s)
temp = np.array([0, 10, 20, 30, 40])
visc = np.array([1.787, 1.307, 1.002, 0.797, 0.653])

b = diferencias_divididas(temp, visc)
t_objetivo = 25 # Queremos saber a 25 grados
resultado = evaluar_newton(b, temp, t_objetivo)

print(f"--- Ejercicio 5 ---")
print(f"La viscosidad estimada a {t_objetivo}°C es: {resultado:.4f} x 10^-3 Pa*s")