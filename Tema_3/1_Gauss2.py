def solve_with_pivot(A, b):
    # Concatenamos para manejar la matriz aumentada
    ab = np.column_stack((A, b)).astype(float)
    n = len(b)

    for i in range(n):
        # Pivoteo parcial: buscamos el máximo en la columna actual
        max_row = np.argmax(abs(ab[i:, i])) + i
        ab[[i, max_row]] = ab[[max_row, i]]
        
        # Eliminación hacia adelante
        for j in range(i + 1, n):
            factor = ab[j, i] / ab[i, i]
            ab[j, i:] -= factor * ab[i, i:]

    # Sustitución regresiva
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (ab[i, -1] - np.dot(ab[i, i+1:n], x[i+1:n])) / ab[i, i]
    return x

# Ejemplo de prueba
A2 = np.array([[0, 2, 1], [1, -1, 1], [3, 2, -1]], dtype=float)
b2 = np.array([4, 5, 1], dtype=float)

solucion = solve_with_pivot(A2, b2)
print("\n--- Ejercicio 2: Pivoteo Parcial ---")
print(f"Solución calculada: {solucion}")