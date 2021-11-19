from TipodeEvento import TipoDeEvento
import AppDataBase


class Administrador:
    __Ciudadanos = AppDataBase.ciudadanos_usuarios
    __CuidadanosBloqueados = AppDataBase.ciudadanos_bloqueados_usuarios
    __Admins = AppDataBase.administradores_usuarios

    def __init__(self):
        AppDataBase.administradores_usuarios.append(self)

    def bloquearCiudadano(self, Ciudadano):
        self.__class__.__Ciudadanos.remove(Ciudadano)
        self.__class__.__CuidadanosBloqueados.append(Ciudadano)

    def desbloquearCiudadano(self, Ciudadano):
        self.__class__.__CuidadanosBloqueados.remove(Ciudadano)

    def crearAdmin(self):
        newAdmin = Administrador()
        self.__class__.__Admins.append(newAdmin)
        return newAdmin

    def borrarAdmin(self, Administrador):
        self.__class__.__Admins.remove(Administrador)

    def crearTipoDeEvento(self, tipodeevento):
        nueva_categoria = TipoDeEvento(tipodeevento)
        return nueva_categoria
