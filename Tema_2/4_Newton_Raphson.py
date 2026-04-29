def newton(f, df, x0, tol=1e-5):
    for _ in range(100):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol: return x1
        x0 = x1
    return x0

f = lambda x: x**2 - 2
df = lambda x: 2*x
print(f"Implementación Base: {newton(f, df, 1)}")