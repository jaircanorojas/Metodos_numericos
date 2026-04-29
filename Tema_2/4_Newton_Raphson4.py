import math

# Ejercicio 4: sin(x) - 0.5 = 0
# f(x) = sin(x) - 0.5
# df(x) = cos(x)
f = lambda x: math.sin(x) - 0.5
df = lambda x: math.cos(x)
x0 = 1.0
tol = 0.0001

print("--- Método de Newton-Raphson: Ejercicio 4 ---")
for i in range(100):
    x1 = x0 - f(x0) / df(x0)
    if abs(x1 - x0) < tol:
        break
    x0 = x1

print(f"La raíz aproximada es: {x1:.6f}")