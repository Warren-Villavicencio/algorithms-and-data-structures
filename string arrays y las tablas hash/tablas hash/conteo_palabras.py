# Archivo: conteo_palabras.py

def contar_palabras(texto):
    """Cuenta la frecuencia de cada palabra en un texto.

    Args:
        texto: El texto a analizar.

    Returns:
        Un diccionario (tabla hash) donde las claves son las palabras y los valores
        son las frecuencias.
    """

    conteo = {}  # Inicializamos un diccionario vacío
    palabras = texto.split()  # Separamos el texto en palabras

    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    return conteo

# Ejemplo de uso:
texto = "Este es un ejemplo de conteo de palabras. Las palabras se cuentan."
resultado = contar_palabras(texto)
print(resultado)