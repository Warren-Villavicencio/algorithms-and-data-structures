# archivo: operaciones_matrices.py
import numpy as np

# Crear dos matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicación de matrices
C = np.dot(A, B)
print(C)

# Inversa de una matriz
inv_A = np.linalg.inv(A)
print(inv_A)