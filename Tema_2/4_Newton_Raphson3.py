import math

# Ejercicio 3: x - cos(x) = 0
# f(x) = x - cos(x)
# df(x) = 1 + sin(x)
f = lambda x: x - math.cos(x)
df = lambda x: 1 + math.sin(x)
x0 = 0.5
tol = 0.000001 # Mayor precisión para ver la velocidad

print("--- Método de Newton-Raphson: Ejercicio 3 ---")
for i in range(100):
    x1 = x0 - f(x0) / df(x0)
    print(f"Iteración {i+1}: x = {x1:.8f}")
    if abs(x1 - x0) < tol:
        break
    x0 = x1

print(f"\nRaíz encontrada con alta precisión: {x1:.8f}")