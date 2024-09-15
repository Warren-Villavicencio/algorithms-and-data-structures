# archivo: metodos_avanzados.py

texto = "  Hola, Mundo!  "

# Reemplazar una subcadena
nuevo_texto = texto.replace("Hola", "Adiós")
print(nuevo_texto)  # Imprime: "  Adiós, Mundo!  "

# Eliminar espacios en blanco al inicio y final
texto_limpio = texto.strip()
print(texto_limpio)  # Imprime: "Hola, Mundo!"

# Unir elementos de una lista en un string
lista = ["manzana", "banana", "cereza"]
fruta_unida = ",".join(lista)
print(fruta_unida)  # Imprime: manzana,banana,cereza