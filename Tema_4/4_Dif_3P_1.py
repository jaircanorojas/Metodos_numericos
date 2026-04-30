import numpy as np

def diff_3_puntos(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Función de prueba: f(x) = sin(x), f'(x) = cos(x)
f = np.sin
x0 = np.pi / 4  # 45 grados
h = 0.01

aprox = diff_3_puntos(f, x0, h)
real = np.cos(x0)

print("--- Diferenciación de 3 Puntos ---")
print(f"Punto x0: {x0}")
print(f"Derivada aproximada: {aprox}")
print(f"Derivada real: {real}")
print(f"Error absoluto: {abs(real - aprox)}")