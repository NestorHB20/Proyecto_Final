import numpy as np

# -----------------------
# Sistema 1
# -----------------------

A1 = np.array([[4, -2, 1],
               [-2, 4, -2],
               [-1, 2, 4]])
b1 = np.array([11, -16, 17])

# Determinantes para Cramer
Delta1 = np.linalg.det(A1)

A1x = A1.copy()
A1x[:,0] = b1
Delta1x = np.linalg.det(A1x)

A1y = A1.copy()
A1y[:,1] = b1
Delta1y = np.linalg.det(A1y)

A1z = A1.copy()
A1z[:,2] = b1
Delta1z = np.linalg.det(A1z)

x1 = Delta1x / Delta1
y1 = Delta1y / Delta1
z1 = Delta1z / Delta1

print("Sistema 1:")
print("Delta =", Delta1)
print("Delta_x =", Delta1x)
print("Delta_y =", Delta1y)
print("Delta_z =", Delta1z)
print("Solución por Cramer:", [x1, y1, z1])
print("-----------------------------------")

# -----------------------
# Sistema 2
# -----------------------

A2 = np.array([[1, 1, 1],
               [1, 2, 5],
               [1, 4, 25]])
b2 = np.array([6, 12, 36])

Delta2 = np.linalg.det(A2)

A2x = A2.copy()
A2x[:,0] = b2
Delta2x = np.linalg.det(A2x)

A2y = A2.copy()
A2y[:,1] = b2
Delta2y = np.linalg.det(A2y)

A2z = A2.copy()
A2z[:,2] = b2
Delta2z = np.linalg.det(A2z)

x2 = Delta2x / Delta2
y2 = Delta2y / Delta2
z2 = Delta2z / Delta2

print("Sistema 2:")
print("Delta =", Delta2)
print("Delta_x =", Delta2x)
print("Delta_y =", Delta2y)
print("Delta_z =", Delta2z)
print("Solución por Cramer:", [x2, y2, z2])
print("-----------------------------------")

# -----------------------
# Sistema 3
# -----------------------

A3 = np.array([[1, 2, 1],
               [3, 8, 1],
               [0, 4, 1]])
b3 = np.array([2, 12, 2])

Delta3 = np.linalg.det(A3)

A3x = A3.copy()
A3x[:,0] = b3
Delta3x = np.linalg.det(A3x)

A3y = A3.copy()
A3y[:,1] = b3
Delta3y = np.linalg.det(A3y)

A3z = A3.copy()
A3z[:,2] = b3
Delta3z = np.linalg.det(A3z)

x3 = Delta3x / Delta3
y3 = Delta3y / Delta3
z3 = Delta3z / Delta3

print("Sistema 3:")
print("Delta =", Delta3)
print("Delta_x =", Delta3x)
print("Delta_y =", Delta3y)
print("Delta_z =", Delta3z)
print("Solución por Cramer:", [x3, y3, z3])
print("-----------------------------------")
