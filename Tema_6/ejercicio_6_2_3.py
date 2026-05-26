import numpy as np
from Predictor_Corrector_Master import predictor_corrector

# EDO: dy/dx = 4x^3
def f(x, y): return 4 * x**3

x, y = predictor_corrector(f, 0, 0, 0.1, 10) # x final = 1.0

print(f"--- Ejercicio 2.3 ---")
print(f"Resultado Predictor-Corrector: {y[-1]:.4f}")
print(f"Resultado Real (x^4): {1.0**4:.4f}")