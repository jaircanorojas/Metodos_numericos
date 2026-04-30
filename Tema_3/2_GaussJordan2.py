def inversa_gauss_jordan(A):
    n = A.shape[0]
    I = np.eye(n)
    # Aumentamos con la matriz identidad
    ab = np.column_stack((A, I)).astype(float)
    
    for i in range(n):
        ab[i] = ab[i] / ab[i, i]
        for j in range(n):
            if i != j:
                ab[j] -= ab[j, i] * ab[i]
    return ab[:, n:]

A2 = np.array([[1, 2], [3, 4]])
print(f"Matriz Inversa Ejercicio 2:\n{inversa_gauss_jordan(A2)}")