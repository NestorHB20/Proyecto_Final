#Tarea 5, ejercicio 2 Derivada numerica
import numpy as np

# Definición de la función y derivada real
def f(x):
    return -x**2 - x/2 + 4

def df_analitica(x):
    return -2*x - 0.5

# Parámetros
xi = 0
h = 0.2  # puedes cambiar a 0.1 si deseas
real = df_analitica(xi)

# Métodos numéricos
adelante = (f(xi + h) - f(xi)) / h
atras = (f(xi) - f(xi - h)) / h
centrada = (f(xi + h) - f(xi - h)) / (2*h)

# Errores relativos
def error_relativo(aprox, real):
    return abs((real - aprox) / real) * 100

# Resultados
print(f"Derivada analítica: {real:.5f}")
print(f"Hacia adelante: {adelante:.5f} | Error: {error_relativo(adelante, real):.2f}%")
print(f"Hacia atrás:    {atras:.5f} | Error: {error_relativo(atras, real):.2f}%")
print(f"Centrada:       {centrada:.5f} | Error: {error_relativo(centrada, real):.2f}%")
