import numpy as np
from Sistemas_EDO_Master import rk4_sistemas

# k1=0.5, k2=0.2
def quimica(t, y):
    k1, k2 = 0.5, 0.2
    dA = -k1 * y[0]
    dB = k1 * y[0] - k2 * y[1]
    dC = k2 * y[1]
    return [dA, dB, dC]

t, sol = rk4_sistemas(quimica, 0, [100, 0, 0], 0.1, 50) # 100 moles de A

print(f"--- Ejercicio 3.4 ---")
print(f"Concentración final -> A: {sol[-1,0]:.2f}, B: {sol[-1,1]:.2f}, C: {sol[-1,2]:.2f}")