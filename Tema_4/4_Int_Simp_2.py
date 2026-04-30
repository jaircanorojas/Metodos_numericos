import numpy as np

# Carga distribuida simplificada q(x)
def q(x): return x**2 + 2*x

L = 5 # Longitud de la viga
integral_carga = simpson_13(q, 0, L, 20)
print(f"Carga total acumulada en la viga: {integral_carga}")