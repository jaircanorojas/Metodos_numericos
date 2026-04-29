import math

# Ejercicio 1: Newton en polinomios
# f(x) = x^3 - x - 1
# Derivada df(x) = 3x^2 - 1
f = lambda x: x**3 - x - 1
df = lambda x: 3*x**2 - 1
x0 = 1.0  # Estimación inicial
tol = 0.0001

print("--- Método de Newton-Raphson: Ejercicio 1 ---")
for i in range(100):
    # Fórmula: x_nuevo = x - f(x)/f'(x)
    x1 = x0 - f(x0) / df(x0)
    
    if abs(x1 - x0) < tol:
        break
    x0 = x1

print(f"La raíz aproximada es: {x1:.6f}")