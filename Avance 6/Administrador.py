from TipodeEvento import TipoDeEvento
import AppDataBase


class Administrador:
    __Ciudadanos = AppDataBase.ciudadanos_usuarios
    __CuidadanosBloqueados = AppDataBase.ciudadanos_bloqueados_usuarios
    __Admins = AppDataBase.administradores_usuarios

    def __init__(self, nombre, clave):
        self.__nombre = nombre
        self.__clave = clave
        AppDataBase.administradores_usuarios.append(self)

    def __repr__(self):
        return f"{self.__nombre}"

    def get_nombre(self):
        return self.__nombre

    def get_clave(self):
        return self.__clave

    def set_nombre(self, nombre):
        self.__nombre = nombre
        return self.__nombre

    def set_clave(self, clave):
        self.__clave = clave
        return self.__clave

    def bloquearCiudadano(self, Ciudadano):
        self.__class__.__Ciudadanos.remove(Ciudadano)
        self.__class__.__CuidadanosBloqueados.append(Ciudadano)

    def desbloquearCiudadano(self, Ciudadano):
        self.__class__.__CuidadanosBloqueados.remove(Ciudadano)

    def crearAdmin(self, nombre, clave):
        newAdmin = Administrador(nombre, clave)
        return newAdmin

    def editarAdmin(self, admin, nombre, clave):
        admin.set_nombre(nombre)
        admin.set_clave(clave)

    def borrarAdmin(self, Administrador):
        try:
            if Administrador in AppDataBase.administradores_usuarios:
                self.__class__.__Admins.remove(Administrador)
            else:
                raise Exception
        except Exception:
            return "No se ha encontrado al administrador"


    def crearTipoDeEvento(self, tipodeevento):
        nueva_categoria = TipoDeEvento(tipodeevento)
        return nueva_categoria
