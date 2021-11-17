from TipodeEvento import TipoDeEvento
import UsersBase


class Administrador:
    __Ciudadanos = UsersBase.ciudadanos_usuarios
    __CuidadanosBloqueados = UsersBase.ciudadanos_bloqueados_usuarios
    __Admins = UsersBase.administradores_usuarios

    def __init__(self):
        UsersBase.administradores_usuarios.append(self)

    """ def __init__(self, nombre):
        super().__init__(nombre)
        UsersBase.administradores_usuarios.append(self)"""

    def bloquearCiudadano(self, Ciudadano):
        self.__class__.__Ciudadanos.remove(Ciudadano)
        self.__class__.__CuidadanosBloqueados.append(Ciudadano)

    def desbloquearCiudadano(self, Ciudadano):
        self.__class__.__CuidadanosBloqueados.remove(Ciudadano)

    def crearAdmin(self):
        newAdmin = Administrador()
        self.__class__.__Admins.append(newAdmin)

    def borrarAdmin(self, Administrador):
        Administrador.remove(Administrador)

    def crearTipoDeEvento(self, tipodeevento):
        nueva_categoria = TipoDeEvento(tipodeevento)
