import numpy as np

# -------------------
# Sistema 1
# -------------------

A1 = np.array([[4, -2, 1],
               [-2, 4, -2],
               [-1, 2, 4]])

b1 = np.array([11, -16, 17])

A1_inv = np.linalg.inv(A1)
x1 = A1_inv @ b1

print("Sistema 1:")
print("Matriz inversa del sistema 1:")
print(A1_inv)
print("Solución del sistema 1 por matriz inversa:", x1)
print("-----------------------------------------")

# -------------------
# Sistema 2
# -------------------

A2 = np.array([[1, 1, 1],
               [1, 2, 5],
               [1, 4, 25]])

b2 = np.array([6, 12, 36])

A2_inv = np.linalg.inv(A2)
x2 = A2_inv @ b2

print("Sistema 2:")
print("Matriz inversa del sistema 2:")
print(A2_inv)
print("Solución del sistema 2 por matriz inversa:", x2)
print("-----------------------------------------")

# -------------------
# Sistema 3
# -------------------

A3 = np.array([[1, 2, 1],
               [3, 8, 1],
               [0, 4, 1]])

b3 = np.array([2, 12, 2])

A3_inv = np.linalg.inv(A3)
x3 = A3_inv @ b3

print("Sistema 3:")
print("Matriz inversa del sistema 3:")
print(A3_inv)
print("Solución del sistema 3 por matriz inversa:", x3)
print("-----------------------------------------")
