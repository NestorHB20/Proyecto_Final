#Tarea 5, inciso C, Taylor
import math

# Aproximación por serie de Taylor truncada en N términos
def integral_taylor(N):
    suma = 0
    for n in range(N):
        termino = ((-1)**n) / (math.factorial(n) * (2*n + 1))
        suma += termino
    return suma

# Mostrar resultados con distintas precisiones
print("Aproximación con 3 términos:", round(integral_taylor(3), 6))
print("Aproximación con 5 términos:", round(integral_taylor(5), 6))
print("Aproximación con 10 términos:", round(integral_taylor(10), 6))
