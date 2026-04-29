import math

# Ejercicio 2: Función cúbica
# f(x) = x^3 - x - 2 en el intervalo [1, 2]
f = lambda x: x**3 - x - 2
a, b, tol = 1.0, 2.0, 0.0001

print("--- Método de Bisección: Ejercicio 2 ---")
if f(a) * f(b) >= 0:
    print("Error en los signos iniciales.")
else:
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"La raíz aproximada es: {c}")