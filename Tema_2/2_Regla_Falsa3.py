import math

# Ejercicio 3: Función trigonométrica
# f(x) = cos(x) - x en el intervalo [0, 1]
f = lambda x: math.cos(x) - x
a, b, tol = 0.0, 1.0, 0.0001

print("--- Método de Regla Falsa: Ejercicio 3 ---")
for i in range(100):
    xr = b - (f(b) * (a - b)) / (f(a) - f(b))
    if abs(f(xr)) < tol:
        break
    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr
print(f"La raíz aproximada es: {xr}")