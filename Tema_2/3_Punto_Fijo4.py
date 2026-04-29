import math

# Ejercicio 4: Resolver x = e^(-x)
g = lambda x: math.exp(-x)
x0 = 0.0
tol = 0.0001

print("--- Método de Punto Fijo: Ejercicio 4 ---")
for i in range(100):
    x1 = g(x0)
    if abs(x1 - x0) < tol:
        break
    x0 = x1

print(f"La raíz aproximada es: {x1}")