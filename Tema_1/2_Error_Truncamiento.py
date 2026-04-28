import math

# EJEMPLO 2: Error de Truncamiento
# Ocurre al usar una serie finita (como Taylor) para aproximar una función infinita.

def error_truncamiento():
    print("--- Ejemplo 2: Error de Truncamiento (e^x) ---")
    x = 1
    valor_real = math.exp(x) # Valor "exacto" de la librería
    
    # Aproximación usando solo los primeros 3 términos de la serie de Taylor
    # e^x ≈ 1 + x + (x^2 / 2!)
    valor_aprox = 1 + x + (x**2 / 2)
    
    print(f"Valor real de e^1: {valor_real}")
    print(f"Valor aproximado (truncado): {valor_aprox}")
    print(f"Error de truncamiento: {abs(valor_real - valor_aprox)}")

if __name__ == "__main__":
    error_truncamiento()