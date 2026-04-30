def jacobi_con_error(A, b, x0, tol, max_iter):
    x = x0
    errores = []
    for i in range(max_iter):
        x_new = (b - np.dot(A - np.diag(np.diag(A)), x)) / np.diag(A)
        err = np.linalg.norm(x_new - x, ord=np.inf)
        errores.append(err)
        if err < tol: break
        x = x_new
    return errores

A3 = np.array([[3, -1], [1, 4]], dtype=float); b3 = np.array([2, 5], dtype=float)
historial = jacobi_con_error(A3, b3, np.zeros(2), 1e-5, 20)
print(f"Ejercicio 3: Errores por iteración: {historial}")