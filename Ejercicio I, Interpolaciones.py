#Ejercicio I Interpolaciones 
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, BarycentricInterpolator, KroghInterpolator

# Datos
x = np.array([1, 2, 3, 5, 7, 8])
y = np.array([3, 6, 19, 99, 291, 444])

# --- 1. Interpolación Lineal (f(3), f(5)) ---
x_lineal = [3, 5]
y_lineal = [19, 99]
poly_lineal = lagrange(x_lineal, y_lineal)
print("Interpolación lineal en x=4:", poly_lineal(4))

# --- 2. Interpolación Cuadrática (f(2), f(3), f(5)) ---
x_cuad = [2, 3, 5]
y_cuad = [6, 19, 99]
poly_cuad = lagrange(x_cuad, y_cuad)
print("Interpolación cuadrática en x=4:", poly_cuad(4))

# --- 3. Interpolación de Newton (grado 4) con scipy ---
x_newton = [2, 3, 5, 7, 8]
y_newton = [6, 19, 99, 291, 444]
newton_poly = KroghInterpolator(x_newton, y_newton)
print("Interpolación Newton orden 4 en x=4:", newton_poly(4))

# --- Graficar ---
x_vals = np.linspace(1, 8, 300)
plt.plot(x, y, 'o', label='Datos originales')
plt.plot(x_vals, poly_cuad(x_vals), label='Interpolación cuadrática')
plt.plot(x_vals, newton_poly(x_vals), label='Interpolación de Newton')
plt.axvline(x=4, linestyle='--', color='gray', label='x = 4')
plt.title('Interpolaciones cuadrática y Newton')
plt.legend()
plt.grid()
plt.show()
