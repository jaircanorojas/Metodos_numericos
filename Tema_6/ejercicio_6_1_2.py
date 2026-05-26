import numpy as np
from RK4_Master import rk4

# dT/dt = -k * (T - Ta)
# k=0.1, Temp ambiente (Ta)=20, Temp inicial=80
k, Ta = 0.1, 20
def enfriamiento(t, T): return -k * (T - Ta)

t, T = rk4(enfriamiento, 0, 80, 2, 10) # 20 minutos de simulación
print(f"Temperatura a los 20 min: {T[-1]:.2f}°C")