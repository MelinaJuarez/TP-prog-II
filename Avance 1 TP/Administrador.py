from Persona import Persona
from TipodeEvento import TipoDeEvento


class Administrador(Persona):
    __CuidadanosBloqueados = []
    __Admins = []

    def __init__(self, nombre):
        super().__init__(nombre)

    def bloquearCiudadano(self, Ciudadano):
        self.__class__.__CuidadanosBloqueados.append(Ciudadano)

    def desbloquearCiudadano(self, Ciudadano):
        self.__class__.__CuidadanosBloqueados.remove(Ciudadano)

    def crearAdmin(self, nombre):
        newAdmin = Administrador(nombre)
        self.__class__.__Admins.append(newAdmin)

    def borrarAdmin(self, Administrador):
        Administrador.remove(Administrador)

    def crearTipoDeEvento(self, tipodeevento):
        nueva_categoria = TipoDeEvento(tipodeevento)
