import numpy as np

def trapecio_compuesto(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

f = lambda x: x**2
a, b, n = 0, 2, 10 # Integral de x^2 de 0 a 2 es 2.666...
resultado = trapecio_compuesto(f, a, b, n)
print(f"Resultado Trapecio (n=10): {resultado}")