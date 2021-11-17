from abc import ABC
import UsersBase
from CiudadanoUsuario import CiudadanoUsuario

class Persona(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre


class Ciudadano(Persona):
    def __init__(self, nombre, cuil, celular):
        super().__init__(nombre)
        self.__cuil = cuil
        self.__celular = celular

    def registrarse(self):
        pass  # hacemos manejo de exception je y validamos



usuario_ciudadano = CiudadanoUsuario(super().get_nombre(), self.__cuil, self.__celular)
UsersBase.ciudadanos_usuarios.append(usuario_ciudadano)
