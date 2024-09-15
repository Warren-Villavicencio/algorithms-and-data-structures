# archivo: slicing.py
import numpy as np

# Crear un array
array = np.arange(10)

# Seleccionar elementos del segundo al cuarto (sin incluir el quinto)
subarray = array[1:4]
print(subarray)