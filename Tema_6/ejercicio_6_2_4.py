import numpy as np
from Predictor_Corrector_Master import predictor_corrector

# f(x,y) = x - y
def f(x, y): return x - y

x, y = predictor_corrector(f, 0, 1, 0.1, 15)

print(f"--- Ejercicio 2.4 ---")
print(f"Estimación final en x=1.5: {y[-1]:.5f}")