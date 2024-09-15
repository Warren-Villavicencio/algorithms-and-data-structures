# Archivo: tabla_hash_encadenamiento.py

class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self):
        self.tamaño = 10
        self.tabla = [None] * self.tamaño

    def _hash(self, clave):
        # Función hash simple (puedes usar funciones más sofisticadas)
        return hash(clave) % self.tamaño

    def insertar(self, clave, valor):
        indice = self._hash(clave)
        nodo = Nodo(clave, valor)

        if self.tabla[indice] is None:
            self.tabla[indice] = nodo
        else:
            nodo.siguiente = self.tabla[indice]
            self.tabla[indice] = nodo

# ... (métodos para buscar y eliminar)