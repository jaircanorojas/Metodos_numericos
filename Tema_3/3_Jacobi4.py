A4 = np.array([[5, -1, 0, 0], [-1, 5, -1, 0], [0, -1, 5, -1], [0, 0, -1, 5]], dtype=float)
b4 = np.array([4, 3, 3, 4], dtype=float)
sol4, _ = jacobi(A4, b4, np.zeros(4), 1e-6, 50)
print(f"Ejercicio 4: Solución 4x4: {sol4}")