# archivo: regex_avanzado.py
import re

texto = "El número de teléfono es (123) 456-7890. El correo es ejemplo@correo.com"

# Extraer número de teléfono con formato
patron_telefono = r"\(\d{3}\)\s\d{3}-\d{4}"
resultado_telefono = re.search(patron_telefono, texto)
if resultado_telefono:
    print(resultado_telefono.group())

# Extraer múltiples direcciones de correo electrónico
patron_email = r"\S+@\S+"
resultado_email = re.findall(patron_email, texto)
print(resultado_email)