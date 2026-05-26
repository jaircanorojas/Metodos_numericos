import numpy as np
from Sistemas_EDO_Master import rk4_sistemas

# theta'' + (g/L)*sin(theta) = 0
g, L = 9.81, 1.0
def pendulo(t, y):
    d_theta = y[1]
    d_omega = -(g/L) * np.sin(y[0])
    return [d_theta, d_omega]

# Solución para un ángulo inicial de 45 grados (pi/4)
t, sol = rk4_sistemas(pendulo, 0, [np.pi/4, 0], 0.05, 40)

print(f"--- Ejercicio 3.3 ---")
print(f"Ángulo final (rad): {sol[-1,0]:.4f}")