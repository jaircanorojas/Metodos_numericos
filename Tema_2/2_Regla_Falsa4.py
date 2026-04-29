import math

# Ejercicio 4: Función combinada
# f(x) = x * e^x - 2 en el intervalo [0, 2]
f = lambda x: x * math.exp(x) - 2
a, b, tol = 0.0, 2.0, 0.0001

print("--- Método de Regla Falsa: Ejercicio 4 ---")
for i in range(100):
    xr = b - (f(b) * (a - b)) / (f(a) - f(b))
    if abs(f(xr)) < tol:
        break
    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr
print(f"La raíz aproximada es: {xr}")