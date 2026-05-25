import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Newton_Master import diferencias_divididas, evaluar_newton

x_puntos = np.array([1, 2, 3, 4, 5])
y_puntos = np.array([0.5, 2.0, 4.5, 8.0, 12.5]) # f(x) = 0.5x^2

for grado in range(1, 4):
    x_sub = x_puntos[:grado+1]
    y_sub = y_puntos[:grado+1]
    b = diferencias_divididas(x_sub, y_sub)
    pred = evaluar_newton(b, x_sub, 2.5)
    print(f"Grado {grado}: Predicción en x=2.5 es {pred:.2f}")