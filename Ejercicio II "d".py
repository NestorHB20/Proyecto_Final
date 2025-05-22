#Ejercicio II d)
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Leer los datos
url = 'https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv'
datos = pd.read_csv(url)

# Asignar variables
X = datos[['Experience Years']]  # scikit-learn requiere 2D para la variable independiente
y = datos['Salary']

# Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Obtener parámetros de la recta: pendiente (a1) y ordenada al origen (a0)
a1 = modelo.coef_[0]
a0 = modelo.intercept_

print(f"Pendiente (a1): {a1:.2f}")
print(f"Ordenada al origen (a0): {a0:.2f}")
print(f"Función de regresión: f(x) = {a1:.2f} * x + {a0:.2f}")

# Generar predicciones
y_pred = modelo.predict(X)

# Graficar puntos y recta de regresión
plt.scatter(X, y, color='blue', label='Datos originales')
plt.plot(X, y_pred, color='red', label='Recta de regresión')
plt.xlabel('Experiencia en años')
plt.ylabel('Salario')
plt.title('Regresión Lineal: Experiencia vs Salario')
plt.legend()
plt.grid(True)
plt.show()
