#Ejercicio_1
import random

def generar_vector(N):
    if type(N) != int or N <= 0:
        return "Error: La entrada debe ser un número entero positivo."
#Ejercicio_2    
    vector = [random.randint(1, 9) for _ in range(N)]  # Genera N valores aleatorios de 1 a 9
    return vector

# Ejemplo de uso 
N = 4

try:
    N = int(N)
    resultado = generar_vector(N)
    print(resultado)
except:
    print("Error: La entrada debe ser un número entero positivo.")

#Ejercicio_3
import random

def generar_matriz(N):
    if type(N) != int or N <= 0:
        return "Error: La entrada debe ser un número entero positivo."
    
    # Generar un vector aleatorio de N valores entre 1 y 9
    vector = [random.randint(1, 9) for _ in range(N)]
    
    # Crear la matriz de NxN con los primeros N múltiplos de cada elemento del vector
    matriz = [[vector[i] * (j + 1) for j in range(N)] for i in range(N)]

    # Imprimir resultados
    print(f"Vector generado: {vector}")
    print("Matriz generada:")
    for fila in matriz:
        print(fila)

# Ejemplo de uso
N = 4

try:
    N = int(N)
    generar_matriz(N)
except:
    print("Error: La entrada debe ser un número entero positivo.")

#Ejercicio_4
import random

def generar_matriz_columnas(N):
    if type(N) != int or N <= 0:
        return "Error: La entrada debe ser un número entero positivo."
    
    # Generar un vector aleatorio de N valores entre 1 y 9
    vector = [random.randint(1, 9) for _ in range(N)]
    
    # Crear la matriz de NxN con los múltiplos en columnas
    matriz = [[vector[j] * (i + 1) for j in range(N)] for i in range(N)]

    # Imprimir resultados
    print("Vector generado:", vector)
    print("Matriz generada:")
    for fila in matriz:
        print(fila)

# Ejemplo de uso
N = 4

try:
    N = int(N)
    generar_matriz_columnas(N)
except:
    print("Error: La entrada debe ser un número entero positivo.")

#Ejercicio_5
import random

def multiplos_fila(N):
    if type(N) != int or N <= 0:
        return "Error: La entrada debe ser un número entero positivo."
    
    vector = [random.randint(1, 9) for _ in range(N)]
    matriz = [[vector[i] * (j + 1) for j in range(N)] for i in range(N)]

    print("Vector generado:", vector)
    print("Matriz generada (por filas):")
    for fila in matriz:
        print(fila)

def multiplos_columna(N):
    if type(N) != int or N <= 0:
        return "Error: La entrada debe ser un número entero positivo."
    
    vector = [random.randint(1, 9) for _ in range(N)]
    matriz = [[vector[j] * (i + 1) for j in range(N)] for i in range(N)]

    print("Vector generado:", vector)
    print("Matriz generada (por columnas):")
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    try:
        N = 4
        print("\nGenerando matriz con múltiplos por filas:")
        multiplos_fila(N)
        print("\nGenerando matriz con múltiplos por columnas:")
        multiplos_columna(N)
    except ValueError:
        print("Error: La entrada debe ser un número entero positivo.")
