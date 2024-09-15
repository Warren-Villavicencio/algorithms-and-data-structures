# archivo: archivos_texto.py

def leer_archivo(nombre_archivo):
  """Lee un archivo de texto y devuelve su contenido.

  Args:
    nombre_archivo: El nombre del archivo a leer.

  Returns:
    Una lista de líneas del archivo.
  """

  with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.readlines()
  return contenido

def escribir_archivo(nombre_archivo, contenido):
  """Escribe contenido en un archivo de texto.

  Args:
    nombre_archivo: El nombre del archivo donde escribir.
    contenido: El contenido a escribir.
  """

  with open(nombre_archivo, 'w') as archivo:
    archivo.write(contenido)

# Ejemplo de uso:
contenido = leer_archivo("mi_archivo.txt")
print(contenido)

nuevo_contenido = "Esta es una nueva línea.\n"
escribir_archivo("mi_archivo.txt", nuevo_contenido)