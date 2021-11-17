import UsersBase

from Persona import Persona


class ContactError(Exception):
    def __init__(self):
        self.__mensaje = "El contacto ya existe dentro de tus contactos"

    def get_mensaje(self):
        return self.__mensaje


class SolicitudError(ContactError):
    def __init__(self):
        self.__mensaje = "Ya enviaste una solicitud a este contacto"

    def get_mensaje(self):
        return self.__mensaje


class Ciudadano(Persona):
    def __init__(self, celular, CUIL, nombre):
        super().__init__(nombre)
        self.__celular = celular
        self.__CUIL = CUIL
        self.__solicitudes_recibidas = []
        self.__contactos = []  # podríamos llamar a esto "contactos"
        self.__solicitudes_denegadas = []
        UsersBase.ciudadanos_usuarios.append(self)

    def __repr__(self):
        return f"{self.get_nombre()}"

    def get_contactos(self):
        return self.__contactos

    def get_numero(self):
        return self.__celular

    def get_solicitudes_recibidas(self):
        return self.__solicitudes_recibidas

    def agregar_solicitud(self, ciudadano):
        try:
            if ciudadano not in self.__contactos:
                if self not in ciudadano.get_solicitudes_recibidas():  # acordate que cambian de lugar el contacto y el self de enviarSolicitud
                    ciudadano.get_solicitudes_recibidas().append(self)
                else:
                    raise SolicitudError()
            else:
                raise ContactError()
        except SolicitudError as s:
            return s.get_mensaje()
        except ContactError as c:
            return c.get_mensaje()

#    def enviarSolicitud(self, ciudadano):
#        return ciudadano.agregar_solicitud(self)

    def enviarSolicitud(self, numero):  # Acá iría un Except donde se evalua si el ciudadano existe en la dataset
        for c in UsersBase.ciudadanos_usuarios:
            if c.get_numero() == numero:
                ciudadano = c
                return ciudadano.agregar_solicitud(self)

    def denegarSolicitud(self, ciudadano):
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            self.__solicitudes_denegadas.append(ciudadano)

    def agregar_contacto(self, ciudadano):
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            self.__contactos.append(ciudadano)

    def aceptarSolicitud(self, ciudadano):
        self.__contactos.append(ciudadano)
        ciudadano.agregar_contacto(self)

    def compartirEvento(self, evento, *contactos):
        self.asistirEvento(evento)
        for c in contactos:
            c.asistirEvento(evento)

    def getCantidadSolicitudesRechazadas(self):
        return len(self.__solicitudes_denegadas)

    def asistirEvento(self, evento):
        evento.sumarPersona()


Marti = Ciudadano(123123, 258258, "Martina")
Felix = Ciudadano(456456, 369369, "Félix")
Jose = Ciudadano(789789, 654654, "Josefina")

Felix.enviarSolicitud(123123)
Marti.aceptarSolicitud(Felix)
Jose.enviarSolicitud(123123)

print(Marti.get_contactos())
print(Felix.get_contactos())
