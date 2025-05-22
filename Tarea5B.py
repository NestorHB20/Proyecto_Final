#Tarea5, ejecicios inciso B
import numpy as np

# Función del inciso b
def f_b(x):
    return -x**2 - x/2 + 4

# Intervalo
a = 0.5
b = 1.5

# Trapecio simple
def trapecio_simple(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))

# Trapecio múltiple
def trapecio_multiple(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    suma = f(x[0]) + f(x[-1]) + 2 * np.sum(f(x[1:-1]))
    return h / 2 * suma

# Simpson 1/3
def simpson_1_3(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    suma = f(x[0]) + f(x[-1]) + 4 * np.sum(f(x[1:n:2])) + 2 * np.sum(f(x[2:n-1:2]))
    return h / 3 * suma

# Simpson 6/8
def simpson_6_8(f, a, b):
    h = (b - a) / 6
    x = np.linspace(a, b, 7)
    coef = [1, 5, 1, 6, 1, 5, 1]
    return (3 * h / 8) * np.dot(coef, f_b(x))

# Resultados
print("Trapecio simple:", trapecio_simple(f_b, a, b))
print("Trapecio múltiple n=2:", trapecio_multiple(f_b, a, b, 2))
print("Trapecio múltiple n=4:", trapecio_multiple(f_b, a, b, 4))
print("Trapecio múltiple n=6:", trapecio_multiple(f_b, a, b, 6))
print("Simpson 1/3 n=2:", simpson_1_3(f_b, a, b, 2))
print("Simpson 1/3 n=6:", simpson_1_3(f_b, a, b, 6))
print("Simpson 6/8:", simpson_6_8(f_b, a, b))
