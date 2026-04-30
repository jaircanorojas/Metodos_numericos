import numpy as np

def cuadratura_gaussiana_2p(f, a, b):
    t = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
    w = np.array([1, 1])
    # Cambio de variable
    x = ((b - a) * t + (b + a)) / 2
    return ((b - a) / 2) * np.sum(w * f(x))

f = lambda x: x**3 + x
print(f"Integral Gaussiana (0 a 1): {cuadratura_gaussiana_2p(f, 0, 1)}")