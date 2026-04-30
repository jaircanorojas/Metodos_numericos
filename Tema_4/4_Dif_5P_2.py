import numpy as np

# f''(x) usando 5 puntos (Segunda derivada)
def acc_5_puntos(f, x, h):
    num = -f(x+2*h) + 16*f(x+h) - 30*f(x) + 16*f(x-h) - f(x-2*h)
    return num / (12 * h**2)

f_pos = lambda t: 5*t**3 + 2*t**2  # a(t) = 30t + 4
t0 = 2.0
h = 0.01

aceleracion = acc_5_puntos(f_pos, t0, h)
print(f"Aceleración calculada en t={t0}: {aceleracion}")