# archivo: formateo_multiple.py

nombre = "Ana"
edad = 30
ciudad = "Madrid"

# Formateo con f-strings
mensaje = f"Hola, mi nombre es {nombre}. Tengo {edad} años y vivo en {ciudad}."
print(mensaje)

# Formateo con el método format()
mensaje2 = "Hola, mi nombre es {}. Tengo {} años y vivo en {}.".format(nombre, edad, ciudad)
print(mensaje2)