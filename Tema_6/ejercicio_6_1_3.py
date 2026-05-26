import numpy as np
from RK4_Master import rk4

# dh/dt = -(A_orificio/A_tanque) * sqrt(2*g*h)
g = 9.81
r_t, r_o = 1.0, 0.05 # Radios en metros
def vaciado(t, h): 
    if h < 0: return 0
    return -(r_o**2 / r_t**2) * np.sqrt(2 * g * h)

t, h = rk4(vaciado, 0, 2.5, 10, 15) # Tanque de 2.5m de altura
print(f"Altura del agua después de 150s: {h[-1]:.4f} m")