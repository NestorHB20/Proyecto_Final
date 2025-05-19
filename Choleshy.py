import numpy as np

def cholesky_decomposition(A):
    n = A.shape[0]
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1):
            sum_k = sum(L[i, k] * L[j, k] for k in range(j))
            if i == j:
                L[i, j] = np.sqrt(A[i, i] - sum_k)
            else:
                L[i, j] = (A[i, j] - sum_k) / L[j, j]
    return L

# -----------------------
# Sistema 1
# -----------------------

A1 = np.array([[4, -2, 1],
               [-2, 4, -2],
               [-1, 2, 4]])

# Verificar si es simétrica y positiva definida
print("Sistema 1:")
if np.allclose(A1, A1.T) and np.all(np.linalg.eigvals(A1) > 0):
    L1 = cholesky_decomposition(A1)
    print("Matriz L (Cholesky):")
    print(L1)
    print("L * L.T =")
    print(L1 @ L1.T)
else:
    print("La matriz no es simétrica o no es positiva definida. No se puede aplicar Cholesky.")
print("-------------------------------------------")

# -----------------------
# Sistema 2
# -----------------------

A2 = np.array([[1, 1, 1],
               [1, 2, 5],
               [1, 4, 25]])

print("Sistema 2:")
if np.allclose(A2, A2.T) and np.all(np.linalg.eigvals(A2) > 0):
    L2 = cholesky_decomposition(A2)
    print("Matriz L (Cholesky):")
    print(L2)
    print("L * L.T =")
    print(L2 @ L2.T)
else:
    print("La matriz no es simétrica o no es positiva definida. No se puede aplicar Cholesky.")
print("-------------------------------------------")

# -----------------------
# Sistema 3
# -----------------------

A3 = np.array([[1, 2, 1],
               [3, 8, 1],
               [0, 4, 1]])

print("Sistema 3:")
if np.allclose(A3, A3.T) and np.all(np.linalg.eigvals(A3) > 0):
    L3 = cholesky_decomposition(A3)
    print("Matriz L (Cholesky):")
    print(L3)
    print("L * L.T =")
    print(L3 @ L3.T)
else:
    print("La matriz no es simétrica o no es positiva definida. No se puede aplicar Cholesky.")
print("-------------------------------------------")
