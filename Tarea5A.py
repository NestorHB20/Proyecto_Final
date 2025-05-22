#Tarea 5, ejercicios del inciso A
import numpy as np

# Función definida
def f(x):
    return 2 * np.cos(2 * x)

# Intervalo
a = 0
b = np.pi / 4

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

# Simpson 3/8 (6/8)
def simpson_3_8(f, a, b):
    h = (b - a) / 3
    x0 = a
    x1 = a + h
    x2 = a + 2 * h
    x3 = b
    return 3 * h / 8 * (f(x0) + 3 * f(x1) + 3 * f(x2) + f(x3))

# Resultados
print("Trapecio simple:", trapecio_simple(f, a, b))
print("Trapecio múltiple n=2:", trapecio_multiple(f, a, b, 2))
print("Trapecio múltiple n=4:", trapecio_multiple(f, a, b, 4))
print("Trapecio múltiple n=6:", trapecio_multiple(f, a, b, 6))
print("Simpson 1/3 n=2:", simpson_1_3(f, a, b, 2))
print("Simpson 1/3 n=6:", simpson_1_3(f, a, b, 6))
print("Simpson 3/8:", simpson_3_8(f, a, b))
