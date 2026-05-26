import numpy as np
import matplotlib.pyplot as plt
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RK4_Master import rk4

# EDO: dy/dx = -2x^3 + 12x^2 - 20x + 8.5
def f(x, y): return -2*x**3 + 12*x**2 - 20*x + 8.5

# Euler simple para comparar
def euler(f, x0, y0, h, n):
    x, y = np.zeros(n+1), np.zeros(n+1)
    x[0], y[0] = x0, y0
    for i in range(n):
        y[i+1] = y[i] + f(x[i], y[i]) * h
        x[i+1] = x[i] + h
    return x, y

x0, y0, h, n = 0, 1, 0.5, 8
xe, ye = euler(f, x0, y0, h, n)
xr, yr = rk4(f, x0, y0, h, n)

plt.plot(xe, ye, 'r--', label='Euler')
plt.plot(xr, yr, 'b-', label='RK4')
plt.title("Comparativa: Euler vs Runge-Kutta 4")
plt.legend(); plt.grid(); plt.show()