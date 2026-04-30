import numpy as np

f = np.log # ln(x) -> 1/x
x0 = 2.0
h = 0.1
real = 1/2

d3 = (f(x0+h) - f(x0-h)) / (2*h)
d5 = (-f(x0+2*h) + 8*f(x0+h) - 8*f(x0-h) + f(x0-2*h)) / (12*h)

print(f"Error 3 puntos: {abs(real - d3):.2e}")
print(f"Error 5 puntos: {abs(real - d5):.2e}")