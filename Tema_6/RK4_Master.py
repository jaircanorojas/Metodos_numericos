import numpy as np

def rk4(f, x0, y0, h, n):
    """
    Método de Runge-Kutta de 4to Orden para una EDO.
    f: dy/dx = f(x, y)
    """
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0], y[0] = x0, y0

    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + 0.5*h, y[i] + 0.5*k1*h)
        k3 = f(x[i] + 0.5*h, y[i] + 0.5*k2*h)
        k4 = f(x[i] + h, y[i] + k3*h)

        y[i+1] = y[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        x[i+1] = x[i] + h

    return x, y