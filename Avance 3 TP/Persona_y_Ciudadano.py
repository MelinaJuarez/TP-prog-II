import csv
from abc import ABC
import AppDataBase
from Error import RegisterError
from Usuario_Ciudadano import CiudadanoUsuario


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
        try:
            with open("datasetAnses.csv") as csv_file:
                archivo = csv.reader(csv_file, delimiter=",")
                header = next(archivo)
                i = 0
                for row in archivo:
                    if self.__cuil == int(row[1]) and self.__celular == int(row[2]):
                        i += 1
                        usuario_ciudadano = CiudadanoUsuario(self.get_nombre(), self.__cuil, self.__celular)
                        AppDataBase.ciudadanos_usuarios.append(usuario_ciudadano)
                        return usuario_ciudadano
                if i == 0:
                    raise RegisterError()
        except RegisterError as r:
            return r.get_mensaje()
