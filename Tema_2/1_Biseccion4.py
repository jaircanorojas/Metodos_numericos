import math

# Ejercicio 4: Función exponencial
# f(x) = e^x - 3x en el intervalo [0, 1]
f = lambda x: math.exp(x) - 3*x
a, b, tol = 0.0, 1.0, 0.0001

print("--- Método de Bisección: Ejercicio 4 ---")
if f(a) * f(b) >= 0:
    print("Intervalo no válido para bisección.")
else:
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"La raíz aproximada es: {c}")