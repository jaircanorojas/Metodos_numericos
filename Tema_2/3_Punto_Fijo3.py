import math

# Ejercicio 3: g(x) = (x^2 + 3) / 4
# Este ejercicio sirve para observar si el método converge según |g'(x)| < 1
g = lambda x: (x**2 + 3) / 4
x0 = 0.0
tol = 0.0001

print("--- Método de Punto Fijo: Ejercicio 3 ---")
for i in range(50):
    x1 = g(x0)
    if abs(x1 - x0) < tol:
        break
    x0 = x1
    print(f"Iteración {i+1}: {x1:.6f}")

print(f"Punto fijo encontrado: {x1}")