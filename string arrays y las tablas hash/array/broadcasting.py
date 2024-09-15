# archivo: broadcasting.py
import numpy as np

# Crear un array y un escalar
a = np.array([[1,2,3], [4,5,6]])
b = 2

# Sumar un escalar a cada elemento del array
c = a + b
print(c)