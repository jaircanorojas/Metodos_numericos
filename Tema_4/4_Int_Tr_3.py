import numpy as np

f = lambda x: np.exp(x)
a, b = 0, 1
real = np.exp(1) - 1

for n in [4, 8, 16, 32]:
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    aprox = (h/2) * (f(x[0]) + 2*np.sum(f(x[1:-1])) + f(x[-1]))
    print(f"n={n:<3} | Error: {abs(real - aprox):.6e}")