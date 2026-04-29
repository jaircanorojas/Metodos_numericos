def secante(f, x0, x1, tol=1e-5):
    for _ in range(100):
        if f(x1) - f(x0) == 0: break
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x_temp - x1) < tol: return x_temp
        x0, x1 = x1, x_temp
    return x1

f = lambda x: x**2 - 4
print(f"Implementación Base: {secante(f, 1, 3)}")