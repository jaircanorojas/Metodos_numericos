import numpy as np
import matplotlib.pyplot as plt

def interpolacion_lagrange(x_puntos, y_puntos, x_objetivo):
    """
    Calcula el valor interpolado usando el método de polinomios de Lagrange.
    """
    n = len(x_puntos)
    resultado = 0
    
    for i in range(n):
        # Calcular el polinomio base L_i(x)
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x_objetivo - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        
        # Sumar el término y_i * L_i al resultado final
        resultado += y_puntos[i] * L_i
        
    return resultado

# --- Ejemplo de prueba ---
if __name__ == "__main__":
    x_test = np.array([0, 2, 4])
    y_test = np.array([1, 5, 17]) # f(x) = x^2 + 1
    
    val = 3
    print(f"Interpolación en x={val}: {interpolacion_lagrange(x_test, y_test, val)}")