import math

# Ejercicio 5: x^3 - 10 = 0 (Para hallar raíz cúbica de 10)
f = lambda x: x**3 - 10
x0, x1 = 2.0, 3.0
tol = 0.0001

print("--- Método de la Secante: Ejercicio 5 ---")
for i in range(100):
    denominador = f(x1) - f(x0)
    if denominador == 0: break
    x_nuevo = x1 - f(x1) * (x1 - x0) / denominador
    if abs(x_nuevo - x1) < tol: break
    x0, x1 = x1, x_nuevo

print(f"La raíz aproximada es: {x1:.6f}")