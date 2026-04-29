import math

# Ejercicio 5: g(x) = 1 / (x + 1)
g = lambda x: 1 / (x + 1)
x0 = 1.0
tol = 0.0001

print("--- Método de Punto Fijo: Ejercicio 5 ---")
for i in range(100):
    x1 = g(x0)
    if abs(x1 - x0) < tol:
        break
    x0 = x1

print(f"La raíz aproximada es: {x1}")