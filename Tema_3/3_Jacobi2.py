def es_diagonal_dominante(A):
    D = np.abs(np.diag(A))
    S = np.sum(np.abs(A), axis=1) - D
    return np.all(D > S)

A2 = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 4]], dtype=float)
dominante = es_diagonal_dominante(A2)
print(f"Ejercicio 2: ¿Es diagonal dominante? {dominante}")