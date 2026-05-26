import numpy as np

def rk4_sistemas(f, x0, y0, h, n):
    """
    RK4 vectorial para sistemas de EDOs.
    y0: array con condiciones iniciales [y1, y2, ..., yn]
    f: función que retorna un array de derivadas
    """
    x = np.zeros(n + 1)
    # y es una matriz: filas son pasos de tiempo, columnas son variables
    y = np.zeros((n + 1, len(y0)))
    x[0] = x0
    y[0] = np.array(y0)

    for i in range(n):
        k1 = np.array(f(x[i], y[i]))
        k2 = np.array(f(x[i] + 0.5*h, y[i] + 0.5*k1*h))
        k3 = np.array(f(x[i] + 0.5*h, y[i] + 0.5*k2*h))
        k4 = np.array(f(x[i] + h, y[i] + k3*h))

        y[i+1] = y[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        x[i+1] = x[i] + h

    return x, y