from abc import ABC


class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
