import numpy as np
import matplotlib.pyplot as plt

def diferencias_divididas(x, y):
    """
    Calcula la tabla de diferencias divididas de Newton.
    """
    n = len(y)
    tabla = np.zeros([n, n])
    tabla[:, 0] = y  # La primera columna es Y
    
    for j in range(1, n):
        for i in range(n - j):
            tabla[i, j] = (tabla[i+1, j-1] - tabla[i, j-1]) / (x[i+j] - x[i])
            
    return tabla[0, :] # Retorna los coeficientes b0, b1, b2...

def evaluar_newton(coef, x_puntos, x_objetivo):
    """
    Evalúa el polinomio de Newton en un valor x_objetivo.
    """
    n = len(coef)
    resultado = coef[0]
    producto = 1.0
    for i in range(1, n):
        producto *= (x_objetivo - x_puntos[i-1])
        resultado += coef[i] * producto
    return resultado

# --- Ejemplo de Uso (Basado en Chapra) ---
if __name__ == "__main__":
    # Datos de ejemplo: aproximar ln(x)
    x_datos = np.array([1, 4, 6])
    y_datos = np.array([0, 1.386294, 1.791759])
    
    # Obtener coeficientes
    b = diferencias_divididas(x_datos, y_datos)
    
    # Valor a interpolar
    x_interp = 2
    y_interp = evaluar_newton(b, x_datos, x_interp)
    
    print(f"Coeficientes de Newton: {b}")
    print(f"Valor interpolado en x={x_interp}: {y_interp}")

    # Graficación
    x_graf = np.linspace(min(x_datos)-1, max(x_datos)+1, 100)
    y_graf = [evaluar_newton(b, x_datos, xi) for xi in x_graf]

    plt.figure(figsize=(10, 6))
    plt.plot(x_graf, y_graf, label="Polinomio de Newton", color='blue')
    plt.scatter(x_datos, y_datos, color='red', label="Puntos conocidos")
    plt.plot(x_interp, y_interp, 'go', label=f"Interpolación (x={x_interp})")
    plt.title("Interpolación de Newton - Diferencias Divididas")
    plt.legend()
    plt.grid(True)
    plt.show()