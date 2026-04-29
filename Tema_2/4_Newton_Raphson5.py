import math

# Ejercicio 5: e^(-x) - x = 0
# f(x) = e^(-x) - x
# df(x) = -e^(-x) - 1
f = lambda x: math.exp(-x) - x
df = lambda x: -math.exp(-x) - 1
x0 = 0.0
tol = 0.0001

print("--- Método de Newton-Raphson: Ejercicio 5 ---")
for i in range(100):
    x1 = x0 - f(x0) / df(x0)
    if abs(x1 - x0) < tol:
        break
    x0 = x1

print(f"La raíz aproximada es: {x1:.6f}")