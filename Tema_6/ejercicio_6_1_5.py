import numpy as np
from RK4_Master import rk4

# dv/dt = g - (c/m)*v
g, c, m = 9.81, 12.5, 70 # Paracaidista de 70kg
def paracaidas(t, v): return g - (c/m) * v

t, v = rk4(paracaidas, 0, 0, 2, 10)
print(f"Velocidad alcanzada a los 20s: {v[-1]:.2f} m/s")