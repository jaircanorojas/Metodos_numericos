import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Newton_Master import diferencias_divididas, evaluar_newton

# Datos de una medición de presión (psi) vs tiempo (s) irregular
tiempo = np.array([0, 2, 5, 6, 9])
presion = np.array([10, 14, 22, 28, 45])

b = diferencias_divididas(tiempo, presion)
print(f"--- Ejercicio 4 ---")
print(f"Presión estimada a los 4 segundos: {evaluar_newton(b, tiempo, 4):.2f} psi")