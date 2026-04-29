# Ejemplo para Punto Fijo Ej1
import math
g = lambda x: math.sqrt(x + 2)
x0 = 1
for _ in range(20):
    x0 = g(x0)
print(f"Resultado Punto Fijo: {x0}")