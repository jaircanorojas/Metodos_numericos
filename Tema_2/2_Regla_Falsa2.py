import math

# Ejercicio 2: Polinomio de grado 3
# f(x) = 2x^3 - 4x^2 + 3x - 6 en el intervalo [1, 3]
f = lambda x: 2*x**3 - 4*x**2 + 3*x - 6
a, b, tol = 1.0, 3.0, 0.0001

print("--- Método de Regla Falsa: Ejercicio 2 ---")
for i in range(100):
    xr = b - (f(b) * (a - b)) / (f(a) - f(b))
    if abs(f(xr)) < tol:
        break
    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr
print(f"La raíz aproximada es: {xr}")