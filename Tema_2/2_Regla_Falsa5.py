import math

# Ejercicio 5: Cálculo con error relativo porcentual
f = lambda x: x**3 - 20
a, b, tol = 2.0, 3.0, 0.5 # 0.5% de error deseado
xr = a
error_relativo = 100.0

print("--- Método de Regla Falsa: Ejercicio 5 (Error %) ---")
while error_relativo > tol:
    xr_anterior = xr
    xr = b - (f(b) * (a - b)) / (f(a) - f(b))
    
    if xr != 0:
        error_relativo = abs((xr - xr_anterior) / xr) * 100
        
    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr

print(f"La raíz es: {xr}")
print(f"Error relativo final: {error_relativo}%")