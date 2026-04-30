import numpy as np

# W = Integral de Fuerza respecto a distancia
def fuerza(x): return 20 * np.sin(x) + 50

a, b, n = 0, 10, 100 # De 0 a 10 metros
trabajo = trapecio_compuesto(fuerza, a, b, n)
print(f"Trabajo total calculado: {trabajo} Joules")