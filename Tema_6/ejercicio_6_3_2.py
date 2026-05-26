import numpy as np
from Sistemas_EDO_Master import rk4_sistemas

# m*x'' + c*x' + k*x = 0  => y[0]=posicion, y[1]=velocidad
m, c, k = 1.0, 0.5, 2.0
def masa_resorte(t, y):
    d_posicion = y[1]
    d_velocidad = -(c/m)*y[1] - (k/m)*y[0]
    return [d_posicion, d_velocidad]

t, sol = rk4_sistemas(masa_resorte, 0, [1.0, 0], 0.1, 50) # Inicia en x=1m

print(f"--- Ejercicio 3.2 ---")
print(f"Posición final a los 5s: {sol[-1,0]:.4f} m")