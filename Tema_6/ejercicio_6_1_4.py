import numpy as np
from RK4_Master import rk4

# dVc/dt = (V_fuente - Vc) / (R * C)
R, C, V_fuente = 1000, 0.001, 10 # 1k ohm, 1mF, 10V
def circuito_rc(t, Vc): return (V_fuente - Vc) / (R * C)

t, Vc = rk4(circuito_rc, 0, 0, 0.1, 50)
print(f"Voltaje del capacitor a los 5s: {Vc[-1]:.4f} V")