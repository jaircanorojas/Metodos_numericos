def regla_falsa(f, a, b, tol=1e-5):
    if f(a) * f(b) >= 0: return None
    for _ in range(100):
        xr = b - (f(b) * (a - b)) / (f(a) - f(b))
        if abs(f(xr)) < tol: break
        if f(a) * f(xr) < 0: b = xr
        else: a = xr
    return xr

f = lambda x: x**2 - 2
print(f"Implementación Base: {regla_falsa(f, 1, 2)}")