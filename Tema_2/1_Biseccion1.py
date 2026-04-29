import math

# Ejercicio 1: Polinomio cuadrático
# f(x) = x^2 + 5x + 6 en el intervalo [-3.5, -2.5]
f = lambda x: x**2 + 5*x + 6
a, b, tol = -3.5, -2.5, 0.0001

print("--- Método de Bisección: Ejercicio 1 ---")
if f(a) * f(b) >= 0:
    print("El método no se puede aplicar: f(a) y f(b) deben tener signos opuestos.")
else:
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"La raíz aproximada es: {c}")