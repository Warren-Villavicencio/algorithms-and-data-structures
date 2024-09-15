# archivo: estadisticas.py
import numpy as np

# Crear un array
datos = np.random.randn(100)

# Calcular la media, desviación estándar y varianza
media = np.mean(datos)
desviacion_estandar = np.std(datos)
varianza = np.var(datos)
print(media, desviacion_estandar, varianza)