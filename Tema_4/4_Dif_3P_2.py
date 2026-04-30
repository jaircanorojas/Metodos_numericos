import numpy as np

def calcular_velocidad(distancia, tiempo):
    v = np.zeros(len(distancia))
    h = tiempo[1] - tiempo[0]
    # Aplicar 3 puntos a los datos intermedios
    for i in range(1, len(distancia) - 1):
        v[i] = (distancia[i+1] - distancia[i-1]) / (2 * h)
    return v

# Datos: Tiempo (s) y Posición (m)
t = np.array([0, 1, 2, 3, 4])
pos = np.array([0, 2, 8, 18, 32]) # Representa d = 2t^2

velocidades = calcular_velocidad(pos, t)
print("--- Aplicación Cinética (Velocidad) ---")
print(f"Tiempos: {t}")
print(f"Velocidades calculadas (m/s): {velocidades}")