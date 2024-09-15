# archivo: funciones_personalizadas.py

def invertir_string(cadena):
  """Invierte un string.

  Args:
    cadena: El string a invertir.

  Returns:
    El string invertido.
  """

  return cadena[::-1]

def contar_vocales(cadena):
  """Cuenta la cantidad de vocales en un string.

  Args:
    cadena: El string a analizar.

  Returns:
    La cantidad de vocales.
  """

  vocales = "aeiouAEIOU"
  contador = 0
  for caracter in cadena:
    if caracter in vocales:
      contador += 1
  return contador

# Ejemplo de uso:
cadena = "Hola, mundo!"
print(invertir_string(cadena))  # Imprime "!odnum ,aloH"
print(contar_vocales(cadena))  # Imprime 4