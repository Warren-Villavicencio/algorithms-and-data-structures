import numpy as np
import matplotlib.pyplot as plt

# Nivel Básico
# Crear un array de 100 números aleatorios entre 0 y 1 con distribución uniforme
random_numbers = np.random.rand(100)

# Nivel Intermedio
# Crear un array de 1000 números aleatorios con distribución normal, media 5 y desviación estándar 2
normal_distribution = np.random.normal(loc=5, scale=2, size=1000)

# Nivel Avanzado
# Crear una matriz de 5x5 con números aleatorios enteros entre 1 y 10
random_matrix = np.random.randint(1, 11, size=(5, 5))

# Nivel Experto
# Crear una muestra aleatoria de 100 elementos de una distribución binomial con 10 ensayos y probabilidad de éxito 0.5
binomial_sample = np.random.binomial(n=10, p=0.5, size=100)

# Nivel Básico
# Obtener los primeros 5 elementos del array
first_five = random_numbers[:5]

# Nivel Intermedio
# Obtener los elementos mayores a 0.5 en el array normal
greater_than_05 = normal_distribution[normal_distribution > 0.5]

# Nivel Avanzado
# Crear una máscara para seleccionar elementos pares de la matriz
even_mask = random_matrix % 2 == 0
even_elements = random_matrix[even_mask]

# Nivel Experto
# Seleccionar elementos en una región específica de la matriz
submatrix = random_matrix[1:3, 2:4]

# Nivel Básico
# Sumar 1 a todos los elementos de un array
array_plus_one = random_numbers + 1

# Nivel Intermedio
# Multiplicar elemento a elemento dos arrays
product_array = random_numbers * normal_distribution

# Nivel Avanzado
# Calcular la media de cada fila de una matriz
row_means = np.mean(random_matrix, axis=1)

# Nivel Experto
# Utilizar vectorización para operaciones eficientes
squared_array = random_numbers**2

