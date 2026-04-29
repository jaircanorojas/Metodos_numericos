import math

# Ejercicio 3: Función trascendental
# f(x) = sin(x) - 0.5 en el intervalo [0, 1]
f = lambda x: math.sin(x) - 0.5
a, b, tol = 0.0, 1.0, 0.0001

print("--- Método de Bisección: Ejercicio 3 ---")
if f(a) * f(b) >= 0:
    print("No hay cambio de signo en el intervalo.")
else:
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"La raíz aproximada es: {c}")