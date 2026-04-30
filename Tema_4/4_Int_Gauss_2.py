import numpy as np

f = lambda x: np.log(x + 1)
a, b = 0, 2
# Resultado exacto aprox 1.2958
res = cuadratura_gaussiana_2p(f, a, b)
print(f"Integral de ln(x+1) de 0 a 2: {res}")