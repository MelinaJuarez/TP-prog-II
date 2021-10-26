from Persona import Persona
from Error import SolicitudError, ContactError


class Ciudadano(Persona):
    def __init__(self, celular, CUIL, nombre):
        super().__init__(nombre)
        self.__celular = celular
        self.__CUIL = CUIL
        self.__solicitudes_recibidas = []
        self.__contactos = []  # podríamos llamar a esto "contactos"
        self.__solicitudes_denegadas = []

    def get_contactos(self):
        return self.__contactos

    def get_solicitudes_recibidas(self):
        return self.__solicitudes_recibidas

    def agregar_solicitud(self, ciudadano):
        """Complementa a enviarSolicitud"""
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

    def enviarSolicitud(self, ciudadano):  # Acá iría un Except donde se evalua si el ciudadano existe en la dataset
        return ciudadano.agregar_solicitud(self)

    def denegarSolicitud(self, ciudadano):
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            self.__solicitudes_denegadas.append(ciudadano)

    def agregar_contacto(self, ciudadano):
        """Complementa a aceptarSolicitud"""
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            self.__contactos.append(ciudadano)

    def aceptarSolicitud(self, ciudadano):
        self.agregar_contacto(ciudadano)
        ciudadano.agregar_contacto(self)

    def compartirEvento(self, evento, *contactos):
        self.asistirEvento(evento)
        for c in contactos:
            c.asistirEvento(evento)

    def getCantidadSolicitudesRechazadas(self):
        return len(self.__solicitudes_denegadas)

    def asistirEvento(self, evento):
        evento.sumarPersona()
