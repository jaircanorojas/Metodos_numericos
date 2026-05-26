import numpy as np

def predictor_corrector(f, x0, y0, h, n):
    """
    Método de Adams-Bashforth-Moulton de 4to orden.
    """
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0], y[0] = x0, y0
    
    # RK4 para obtener los primeros 3 puntos necesarios
    for i in range(3):
        k1 = f(x[i], y[i])
        k2 = f(x[i]+0.5*h, y[i]+0.5*k1*h)
        k3 = f(x[i]+0.5*h, y[i]+0.5*k2*h)
        k4 = f(x[i]+h, y[i]+k3*h)
        y[i+1] = y[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        x[i+1] = x[i] + h

    # Bucle Principal de Pasos Múltiples
    for i in range(3, n):
        # Predictor (Adams-Bashforth)
        f_i = f(x[i], y[i])
        f_i1 = f(x[i-1], y[i-1])
        f_i2 = f(x[i-2], y[i-2])
        f_i3 = f(x[i-3], y[i-3])
        
        y_pred = y[i] + (h/24)*(55*f_i - 59*f_i1 + 37*f_i2 - 9*f_i3)
        x[i+1] = x[i] + h
        
        # Corrector (Adams-Moulton)
        f_new = f(x[i+1], y_pred)
        y[i+1] = y[i] + (h/24)*(9*f_new + 19*f_i - 5*f_i1 + f_i2)
        
    return x, y