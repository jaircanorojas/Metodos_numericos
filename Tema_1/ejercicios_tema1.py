# Ejemplo de Errores: Absoluto, Relativo y Porcentual

def calcular_errores(valor_real, valor_aproximado):
    # 1. Error Absoluto
    error_abs = abs(valor_real - valor_aproximado)
    
    # 2. Error Relativo
    error_rel = error_abs / abs(valor_real)
    
    # 3. Error Porcentual
    error_perc = error_rel * 100
    
    print(f"Valor Real: {valor_real}")
    print(f"Valor Aproximado: {valor_aproximado}")
    print(f"--- Resultados ---")
    print(f"Error Absoluto: {error_abs}")
    print(f"Error Relativo: {error_rel}")
    print(f"Error Porcentual: {error_perc}%")

# Prueba con una medición de un puente (50m real, 49.98m medido)
calcular_errores(50, 49.98)