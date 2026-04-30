A4 = np.array([[1, -1, 2], [2, -2, 4], [3, -3, 6]])
b4 = np.array([3, 6, 9])
r_a = np.linalg.matrix_rank(A4)
r_ab = np.linalg.matrix_rank(np.column_stack((A4, b4)))

print(f"Análisis Ejercicio 4:")
if r_a == r_ab and r_a < A4.shape[1]:
    print(f"Infinitas soluciones. Grados de libertad: {A4.shape[1] - r_a}")