import numpy as np

f = lambda x: np.sin(x)
a, b, n = 0, np.pi, 6
# Simpson suele ser mucho más exacto con pocos intervalos
print(f"Simpson: {simpson_13(f, a, b, n)}")
# (Función trapecio manual rápida)
h = (b-a)/n
x = np.linspace(a, b, n+1)
trap = (h/2) * (f(x[0]) + 2*np.sum(f(x[1:-1])) + f(x[-1]))
print(f"Trapecio: {trap}")