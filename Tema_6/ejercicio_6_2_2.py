import numpy as np
from Predictor_Corrector_Master import predictor_corrector

# EDO: dy/dx = -10y (Decaimiento rápido)
def f(x, y): return -10 * y

# Probamos con un paso h pequeño para asegurar estabilidad
x, y = predictor_corrector(f, 0, 1, 0.05, 20)

print(f"--- Ejercicio 2.2 ---")
print(f"Aproximación en x=1.0: {y[-1]:.6f}")