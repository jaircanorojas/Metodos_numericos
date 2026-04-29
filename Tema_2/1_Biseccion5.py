import math

# Ejercicio 5: Función logarítmica
# f(x) = ln(x) - x + 2 en el intervalo [2, 4]
f = lambda x: math.log(x) - x + 2
a, b, tol = 2.0, 4.0, 0.0001

print("--- Método de Bisección: Ejercicio 5 ---")
if f(a) * f(b) >= 0:
    print("Error: f(a) y f(b) deben tener diferentes signos.")
else:
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"La raíz aproximada es: {c}")