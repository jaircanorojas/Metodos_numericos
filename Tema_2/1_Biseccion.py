def biseccion(f, a, b, tol=1e-5):
    if f(a) * f(b) >= 0: return "Error: No hay cambio de signo."
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0: break
        if f(a) * f(c) < 0: b = c
        else: a = c
    return (a + b) / 2

f = lambda x: x**2 - 4
print(f"Implementación Base: {biseccion(f, 0, 5)}")