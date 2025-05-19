import numpy as np

def doolittle(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # U
        for k in range(i, n):
            U[i, k] = A[i, k] - sum(L[i, j] * U[j, k] for j in range(i))
        # L
        L[i, i] = 1
        for k in range(i+1, n):
            L[k, i] = (A[k, i] - sum(L[k, j] * U[j, i] for j in range(i))) / U[i, i]
    
    return L, U

# ---------------------------
# Sistema 1
# ---------------------------

A1 = np.array([[4, -2, 1],
               [-2, 4, -2],
               [-1, 2, 4]])

L1, U1 = doolittle(A1)
print("Sistema 1:")
print("Matriz L:")
print(L1)
print("Matriz U:")
print(U1)
print("---------------------------------")

# ---------------------------
# Sistema 2
# ---------------------------

A2 = np.array([[1, 1, 1],
               [1, 2, 5],
               [1, 4, 25]])

L2, U2 = doolittle(A2)
print("Sistema 2:")
print("Matriz L:")
print(L2)
print("Matriz U:")
print(U2)
print("---------------------------------")

# ---------------------------
# Sistema 3
# ---------------------------

A3 = np.array([[1, 2, 1],
               [3, 8, 1],
               [0, 4, 1]])

L3, U3 = doolittle(A3)
print("Sistema 3:")
print("Matriz L:")
print(L3)
print("Matriz U:")
print(U3)
print("---------------------------------")
