import numpy as np

def diff_5_puntos(f, x, h):
    numerador = -f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)
    return numerador / (12 * h)

f = lambda x: np.exp(x) * np.sin(x)
x0 = 0.5
h = 0.01

derivada = diff_5_puntos(f, x0, h)
print(f"Ejercicio 1 (5 Puntos): Derivada en x={x0} es {derivada}")