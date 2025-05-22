#Ejercicio II c)
import pandas as pd

# Leer datos desde el CSV
url = 'https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv'
datos = pd.read_csv(url)

# Asignar columnas a variables independientes y dependientes
x = datos['Experience Years']   # abscisas (x_i)
y = datos['Salary']             # ordenadas (f(x_i))

# Mostrar los primeros valores para verificar
print("Primeras 5 observaciones de x (años de experiencia):")
print(x.head())

print("\nPrimeras 5 observaciones de y (salarios):")
print(y.head())
