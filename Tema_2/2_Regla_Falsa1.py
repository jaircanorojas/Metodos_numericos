import math

# Ejercicio 1: Raíz de x^2 - 2
# f(x) = x^2 - 2 en el intervalo [1, 2]
f = lambda x: x**2 - 2
a, b, tol = 1.0, 2.0, 0.0001

print("--- Método de Regla Falsa: Ejercicio 1 ---")
if f(a) * f(b) >= 0:
    print("No hay cambio de signo en el intervalo.")
else:
    for i in range(100):
        # Fórmula de la posición falsa
        xr = b - (f(b) * (a - b)) / (f(a) - f(b))
        
        if abs(f(xr)) < tol:
            break
            
        if f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr
    print(f"La raíz aproximada es: {xr}")