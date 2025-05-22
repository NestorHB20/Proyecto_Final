#Ejercicio II b)
import pandas as pd

# URL del archivo CSV
url = 'https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv'

# Leer el archivo CSV desde la URL
datos = pd.read_csv(url)

# Mostrar los primeros registros para verificar que se cargaron correctamente
print("Datos cargados desde el archivo CSV:\n")
print(datos.head())
