import math

# Ejercicio 2: Resolver x = cos(x)
g = lambda x: math.cos(x)
x0 = 0.5
tol = 0.0001

print("--- Método de Punto Fijo: Ejercicio 2 ---")
for i in range(100):
    x1 = g(x0)
    if abs(x1 - x0) < tol:
        break
    x0 = x1

print(f"La raíz aproximada es: {x1}")