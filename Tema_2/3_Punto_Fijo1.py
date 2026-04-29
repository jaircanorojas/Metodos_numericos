import math

# Ejercicio 1: g(x) de una raíz cuadrada para resolver x^2 - x - 2 = 0
# Despeje: x = sqrt(x + 2)
g = lambda x: math.sqrt(x + 2)
x0 = 1.0  # Valor inicial
tol = 0.0001
max_iter = 50

print("--- Método de Punto Fijo: Ejercicio 1 ---")
for i in range(max_iter):
    x1 = g(x0)
    print(f"Iteración {i+1}: x = {x1:.6f}")
    
    if abs(x1 - x0) < tol:
        break
    x0 = x1

print(f"\nEl punto fijo aproximado es: {x1}")