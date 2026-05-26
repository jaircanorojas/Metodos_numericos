import numpy as np
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Predictor_Corrector_Master import predictor_corrector

# EDO: dy/dx = y (Solución real: e^x)
def f(x, y): return y

x0, y0, h, n = 0, 1, 0.1, 20
x, y = predictor_corrector(f, x0, y0, h, n)

print(f"--- Ejercicio 2.1 ---")
print(f"Valor en x=2.0: {y[-1]:.4f}")
print(f"Valor real (e^2): {np.exp(2):.4f}")