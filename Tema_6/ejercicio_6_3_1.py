import numpy as np
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Sistemas_EDO_Master import rk4_sistemas

# y[0] = Presas (x), y[1] = Depredadores (y)
def modelo_biologico(t, y):
    a, b, c, d = 1.2, 0.6, 0.8, 0.3
    d_presas = a*y[0] - b*y[0]*y[1]
    d_depredadores = -c*y[1] + d*y[0]*y[1]
    return [d_presas, d_depredadores]

t, sol = rk4_sistemas(modelo_biologico, 0, [2, 1], 0.1, 100)

print(f"--- Ejercicio 3.1 ---")
print(f"Población final -> Presas: {sol[-1,0]:.2f}, Depredadores: {sol[-1,1]:.2f}")