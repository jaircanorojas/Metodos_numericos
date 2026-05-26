# Tema 6: Solución de Ecuaciones Diferenciales

En este tema se estudian los métodos numéricos para aproximar soluciones de ecuaciones diferenciales ordinarias (EDO) de la forma $dy/dx = f(x, y)$. Estas técnicas son fundamentales en ingeniería para modelar sistemas dinámicos.

---

## 1. Métodos de un Paso (Euler y Runge-Kutta)

### Concepto
Estos métodos utilizan la información de un solo punto previo $(x_i, y_i)$ para estimar el valor del siguiente punto. El método de Runge-Kutta de 4to orden (RK4) es el estándar por su precisión de cuarto orden.

### Algoritmo
1. **Cálculo de pendientes**: Se determinan cuatro pendientes intermedias ($k_1, k_2, k_3, k_4$).
2. **Sustitución**: Se promedian las pendientes para dar el paso final:
   $$y_{i+1} = y_i + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

### Implementación
* [Código Base: Runge-Kutta 4to Orden](./RK4_Master.py)

### Ejercicios
* [Ejercicio 1.1: Comparativa de error Euler vs RK4](./ejercicio_6_1_1.py)
* [Ejercicio 1.2: Ley de enfriamiento de Newton](./ejercicio_6_1_2.py)
* [Ejercicio 1.3: Vaciado de un tanque cilíndrico](./ejercicio_6_1_3.py)
* [Ejercicio 1.4: Circuito RC con fuente constante](./ejercicio_6_1_4.py)
* [Ejercicio 1.5: Caída libre con resistencia del aire](./ejercicio_6_1_5.py)

---

## 2. Métodos de Pasos Múltiples

### Concepto
Aprovechan la información de varios puntos anteriores para predecir el siguiente valor, usualmente mediante esquemas de **Predictor-Corrector**.

### Algoritmo
1. **Predicción**: Se usa una fórmula explícita (Adams-Bashforth) para predecir $y_{i+1}$.
2. **Corrección**: Se usa una fórmula implícita (Adams-Moulton) para refinar el valor.

### Implementación
* [Código Base: Adams-Bashforth-Moulton](./Predictor_Corrector_Master.py)

### Ejercicios
* [Ejercicio 2.1: Implementación de 4 pasos](./ejercicio_6_2_1.py)
* [Ejercicio 2.2: Análisis de estabilidad](./ejercicio_6_2_2.py)
* [Ejercicio 2.3: Comparación con métodos de un paso](./ejercicio_6_2_3.py)
* [Ejercicio 2.4: Error de truncamiento local](./ejercicio_6_2_4.py)
* [Ejercicio 2.5: Aplicación en cinética química](./ejercicio_6_2_5.py)

---

## 3. Sistemas de Ecuaciones Diferenciales Ordinarias

### Concepto
Se resuelve un conjunto de EDOs simultáneas de primer orden aplicando métodos como RK4 de forma vectorial.

### Algoritmo
1. **Definición Vectorial**: Se define un vector de estado $\mathbf{y} = [y_1, y_2, \dots, y_n]^T$.
2. **Cálculo Vectorial**: Se obtienen los vectores $\mathbf{k}_n$ evaluando el sistema completo.

### Implementación
* [Código Base: Sistemas de EDOs con RK4](./Sistemas_EDO_Master.py)

### Ejercicios
* [Ejercicio 3.1: Modelo Depredador-Presa](./ejercicio_6_3_1.py)
* [Ejercicio 3.2: Sistema Masa-Resorte Amortiguado](./ejercicio_6_3_2.py)
* [Ejercicio 3.3: Péndulo simple no lineal](./ejercicio_6_3_3.py)
* [Ejercicio 3.4: Reacciones químicas acopladas](./ejercicio_6_3_4.py)
* [Ejercicio 3.5: Circuito RLC de segundo orden](./ejercicio_6_3_5.py)
