# Archivo: regex.py
import re

texto = "Mi número de teléfono es 123-456-7890 y mi correo es ejemplo@correo.com"
numeros_telefono = re.findall(r'\d{3}-\d{3}-\d{4}', texto)
direcciones_email = re.findall(r'\S+@\S+', texto)
print(numeros_telefono)
print(direcciones_email)