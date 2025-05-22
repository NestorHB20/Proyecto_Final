# procesar_salarios.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Paso 1: Leer los datos desde el enlace CSV
url = 'https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv'
data = pd.read_csv(url)

# Mostrar las primeras filas del dataset
print("Primeras filas del conjunto de datos:")
print(data.head())

# Paso 2: Extraer las columnas de interés
X = data[['Experience Years']]  # Años de experiencia
y = data['Salary']              # Salario

# Paso 3: Visualización de los datos
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Datos reales')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.title('Relación entre Experiencia y Salario')

# Paso 4: Ajuste de un modelo lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Mostrar los coeficientes
print(f"Coeficiente (pendiente): {modelo.coef_[0]:.2f}")
print(f"Intersección (ordenada al origen): {modelo.intercept_:.2f}")

# Paso 5: Dibujar la recta de regresión
y_pred = modelo.predict(X)
plt.plot(X, y_pred, color='red', linewidth=2, label='Modelo lineal')
plt.legend()
plt.grid(True)
plt.show()
