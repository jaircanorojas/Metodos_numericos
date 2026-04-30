import numpy as np

def diff_3_puntos(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

f = np.exp # f(x) = e^x, f'(x) = e^x
x0 = 1.0
pasos_h = [0.1, 0.01, 0.001, 0.0001]
real = np.exp(1.0)

print(f"{'h':<10} | {'Aproximación':<15} | {'Error':<15}")
print("-" * 45)
for h in pasos_h:
    aprox = diff_3_puntos(f, x0, h)
    print(f"{h:<10} | {aprox:<15.8f} | {abs(real - aprox):<15.8e}")