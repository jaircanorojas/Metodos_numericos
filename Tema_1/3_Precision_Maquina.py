# EJEMPLO 3: Épsilon de la Máquina
# Es el número más pequeño que la computadora puede sumar a 1.0 
# sin que el resultado siga siendo 1.0.

def epsilon_maquina():
    print("--- Ejemplo 3: Épsilon de la Máquina ---")
    epsilon = 1.0
    
    while (1.0 + epsilon) > 1.0:
        epsilon_anterior = epsilon
        epsilon = epsilon / 2
        
    print(f"El Épsilon calculado es: {epsilon_anterior}")
    print(f"Comprobación: 1.0 + {epsilon} = {1.0 + epsilon}")

if __name__ == "__main__":
    epsilon_maquina()