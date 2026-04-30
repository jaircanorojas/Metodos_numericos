# Balanceo de Propano: C3H8 + O2 -> CO2 + H2O
# Carbono: 3a = c  => 3a - c = 0
# Hidrógeno: 8a = 2d => 8a - 2d = 0
# Oxígeno: 2b = 2c + d => 2b - 2c - d = 0
# Fijamos a = 1 para resolver el sistema
A5 = np.array([[0, -1, 0], [0, 0, -2], [2, -2, -1]])
b5 = np.array([-3, -8, 0]) # Pasamos el término de 'a' al otro lado

sol_quimica = np.linalg.solve(A5, b5)
print(f"Ejercicio 5: Coeficientes para a=1 -> b={sol_quimica[0]}, c={sol_quimica[1]}, d={sol_quimica[2]}")