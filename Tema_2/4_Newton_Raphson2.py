import math

# Ejercicio 2: Calcular la raíz cúbica de 27 (x^3 - 27 = 0)
# f(x) = x^3 - 27
# df(x) = 3x^2
f = lambda x: x**3 - 27
df = lambda x: 3*x**2
x0 = 3.5
tol = 0.0001

print("--- Método de Newton-Raphson: Ejercicio 2 ---")
for i in range(100):
    x1 = x0 - f(x0) / df(x0)
    if abs(x1 - x0) < tol:
        break
    x0 = x1

print(f"La raíz aproximada es: {x1:.6f}")