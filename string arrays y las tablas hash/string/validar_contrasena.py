# archivo: validar_contrasena.py
import re

def validar_contrasena(contrasena):
  """Valida si una contraseña cumple con ciertos criterios.

  Args:
    contrasena: La contraseña a validar.

  Returns:
    True si la contraseña es válida, False en caso contrario.
  """

  # Una contraseña fuerte suele tener:
  # - Al menos 8 caracteres
  # - Al menos una mayúscula
  # - Al menos una minúscula
  # - Al menos un número
  # - Al menos un carácter especial

  patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
  return re.match(patron, contrasena) is not None

# Ejemplo de uso:
contrasena = input("Ingrese su contraseña: ")
if validar_contrasena(contrasena):
  print("La contraseña es válida.")
else:
  print("La contraseña no es válida.")