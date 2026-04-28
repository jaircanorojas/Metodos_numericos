# EJEMPLO 5: Conversión de Decimal a Binario
# Ver cómo la precisión de un número decimal se pierde al convertirse
# a formato hexadecimal/binario de punto flotante.

def decimal_a_binario():
    print("--- Ejemplo 5: Representación de Punto Flotante ---")
    numero = 0.1
    
    # .hex() nos muestra la representación interna real en la memoria
    representacion_hex = numero.hex()
    
    print(f"Número decimal: {numero}")
    print(f"Representación en memoria (Hexadecimal): {representacion_hex}")
    print("Nota: El 0.1 no tiene una representación binaria exacta finita.")

if __name__ == "__main__":
    decimal_a_binario()