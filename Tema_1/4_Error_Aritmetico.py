# EJEMPLO 4: Error en Operaciones Aritméticas
# Demuestra la "cancelación catastrófica" al restar números muy cercanos.

def error_aritmetico():
    print("--- Ejemplo 4: Cancelación por Resta ---")
    # Números muy cercanos entre sí
    x = 1.23456789012345
    y = 1.23456789012344
    
    resultado_esperado = 0.00000000000001
    resultado_python = x - y
    
    print(f"Valor x: {x}")
    print(f"Valor y: {y}")
    print(f"Resultado real esperado: {resultado_esperado}")
    print(f"Resultado obtenido:      {resultado_python}")

if __name__ == "__main__":
    error_aritmetico()