import math

# Ejercicio 2: ln(x) + x - 5 = 0
f = lambda x: math.log(x) + x - 5
x0, x1 = 3.0, 4.0
tol = 0.0001

print("--- Método de la Secante: Ejercicio 2 ---")
for i in range(100):
    denominador = f(x1) - f(x0)
    if denominador == 0: break
    x_nuevo = x1 - f(x1) * (x1 - x0) / denominador
    if abs(x_nuevo - x1) < tol: break
    x0, x1 = x1, x_nuevo

print(f"La raíz aproximada es: {x1:.6f}")