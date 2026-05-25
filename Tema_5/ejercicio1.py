import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Newton_Master import diferencias_divididas, evaluar_newton

# Datos: x=1, x=4, x=6 (para logaritmo base 10)
x_datos = np.array([1.0, 4.0, 6.0])
y_datos = np.log10(x_datos)

# 1. Interpolación lineal (usando primeros 2 puntos)
b_lineal = diferencias_divididas(x_datos[:2], y_datos[:2])
res_lineal = evaluar_newton(b_lineal, x_datos[:2], 2.5)

# 2. Interpolación cuadrática (usando los 3 puntos)
b_cuad = diferencias_divididas(x_datos, y_datos)
res_cuad = evaluar_newton(b_cuad, x_datos, 2.5)

print(f"--- Ejercicio 1 ---")
print(f"Estimación lineal log10(2.5): {res_lineal:.4f}")
print(f"Estimación cuadrática log10(2.5): {res_cuad:.4f}")
print(f"Valor real: {np.log10(2.5):.4f}")