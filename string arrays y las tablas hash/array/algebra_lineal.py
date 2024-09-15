# archivo: algebra_lineal.py
import numpy as np

# Resolver un sistema de ecuaciones lineales
A = np.array([[2, 1], [1, 2]])
b = np.array([5, 4])
x = np.linalg.solve(A, b)
print(x)