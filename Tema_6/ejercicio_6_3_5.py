import numpy as np
from Sistemas_EDO_Master import rk4_sistemas

# E = L*i' + R*i + (1/C)*q  donde i = q'
L, R, C, E = 0.5, 10, 0.001, 12
def circuito_rlc(t, y):
    dq = y[1] # Corriente i
    di = (E - R*y[1] - (1/C)*y[0]) / L
    return [dq, di]

t, sol = rk4_sistemas(circuito_rlc, 0, [0, 0], 0.01, 100) # Carga inicial 0

print(f"--- Ejercicio 3.5 ---")
print(f"Corriente final en el inductor: {sol[-1,1]:.4f} A")