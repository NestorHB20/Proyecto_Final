import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([5.04, 8.12, 10.64, 13.18, 16.20, 20.04])

# Cálculo de coeficientes de regresión lineal (mínimos cuadrados)
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
sum_xy = np.sum(x * y)

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a0 = (sum_y - a1 * sum_x) / n

print(f"Función de regresión lineal: f(x) = {a0:.4f} + {a1:.4f}x")

# Generar valores para la recta de regresión
x_line = np.linspace(min(x), max(x), 100)
y_line = a0 + a1 * x_line

# Gráfica
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x_line, y_line, color='red', label='Recta de regresión')
plt.title('Regresión Lineal por Mínimos Cuadrados')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

