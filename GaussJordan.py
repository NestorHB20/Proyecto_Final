import numpy as np

# -------------------
# Sistema 1
# -------------------

A1 = np.array([[4, -2, 1],
               [-2, 4, -2],
               [-1, 2, 4]])

b1 = np.array([11, -16, 17])

x1 = np.linalg.solve(A1, b1)
print("Solución del sistema 1:", x1)

# -------------------
# Sistema 2
# -------------------

A2 = np.array([[1, 1, 1],
               [1, 2, 5],
               [1, 4, 25]])

b2 = np.array([6, 12, 36])

x2 = np.linalg.solve(A2, b2)
print("Solución del sistema 2:", x2)

# -------------------
# Sistema 3
# -------------------

A3 = np.array([[1, 2, 1],
               [3, 8, 1],
               [0, 4, 1]])

b3 = np.array([2, 12, 2])

x3 = np.linalg.solve(A3, b3)
print("Solución del sistema 3:", x3)
