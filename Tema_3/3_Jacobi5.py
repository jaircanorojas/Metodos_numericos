# Usamos un vector inicial cercano a la solución real
x_cercano = np.array([0.5, 2.0, -1.0]) 
# Reutilizamos el sistema del Ejercicio 1
sol5, it5 = jacobi(A1, b1, x_cercano, 1e-5, 100)

print(f"Ejercicio 5: Con vector inicial específico, tardó {it5} iteraciones.")