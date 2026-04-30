def analizar_sistema(A, b):
    ab = np.column_stack((A, b)).astype(float)
    # Si al final una fila es [0, 0, 0 | valor distinto de cero] -> Sin solución
    # Usaremos el rango para determinarlo rápidamente
    rango_a = np.linalg.matrix_rank(A)
    rango_ab = np.linalg.matrix_rank(ab)
    
    if rango_a < rango_ab:
        return "El sistema no tiene solución (Inconsistente)"
    return "Tiene solución"

A3 = np.array([[1, 1, 1], [0, 2, 2], [0, 0, 0]]) # Fila de ceros en A
b3 = np.array([5, 10, 7]) # b impide la solución
print(f"Análisis Ejercicio 3: {analizar_sistema(A3, b3)}")