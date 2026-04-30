import numpy as np

# Función de densidad lineal rho(x)
def rho(x): return x**2 + 1

a, b = 0, 3
masa = cuadratura_gaussiana_2p(rho, a, b)
# Momento M = integral de x * rho(x)
def momento_f(x): return x * rho(x)
momento = cuadratura_gaussiana_2p(momento_f, a, b)

x_centro = momento / masa
print(f"Centro de masa calculado en x = {x_centro:.4f}")