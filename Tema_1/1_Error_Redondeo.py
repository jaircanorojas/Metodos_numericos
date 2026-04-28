# EJEMPLO 1: Error de Redondeo
# La computadora representa números en binario, lo que causa pequeñas
# precisiones perdidas en números decimales como 0.1.

def error_redondeo():
    print("--- Ejemplo 1: Error de Redondeo ---")
    valor_objetivo = 1.0
    suma = 0.0
    
    for i in range(10):
        suma += 0.1
        
    print(f"Resultado de sumar 0.1 diez veces: {suma}")
    print(f"Diferencia real (Error): {valor_objetivo - suma}")
    print(f"¿Es exactamente 1.0?: {suma == 1.0}")

if __name__ == "__main__":
    error_redondeo()