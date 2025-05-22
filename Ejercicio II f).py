#Ejercicio II f)
# Estimar el salario para 15, 30 y 50 años de experiencia
experiencia_nueva = np.array([[15], [30], [50]])
salario_estimado = modelo.predict(experiencia_nueva)

# Imprimir los resultados
for anios, salario in zip(experiencia_nueva.flatten(), salario_estimado):
    print(f"Experiencia: {anios} años => Salario estimado: ${salario:,.2f}")
