import math

# Ejercicio 4: x^10 - 1 = 0
f = lambda x: x**10 - 1
x0, x1 = 0.0, 1.5
tol = 0.0001

print("--- Método de la Secante: Ejercicio 4 ---")
for i in range(100):
    denominador = f(x1) - f(x0)
    if denominador == 0: break
    x_nuevo = x1 - f(x1) * (x1 - x0) / denominador
    if abs(x_nuevo - x1) < tol: break
    x0, x1 = x1, x_nuevo

print(f"La raíz aproximada es: {x1:.6f}")