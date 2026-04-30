import numpy as np

def simpson_13(f, a, b, n):
    if n % 2 != 0: n += 1 # Asegurar n par
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    suma = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    return (h / 3) * suma

f = lambda x: x**4
print(f"Resultado Simpson 1/3: {simpson_13(f, 0, 1, 10)}")