import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Newton_Master import diferencias_divididas, evaluar_newton

# Datos conocidos de e^x
x = np.array([0, 1, 2, 3])
y = np.array([1.0, 2.7182, 7.3890, 20.0855])

coefs = diferencias_divididas(x, y)
x_obj = 1.5
resultado = evaluar_newton(coefs, x, x_obj)

print(f"--- Ejercicio 2 ---")
print(f"Aproximación de e^{x_obj}: {resultado:.4f}")
print(f"Valor exacto: {np.exp(1.5):.4f}")