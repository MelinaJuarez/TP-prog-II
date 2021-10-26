from Persona import Persona


class Ciudadano(Persona):
    def __init__(self, celular, CUIL, nombre):
        super().__init__(nombre)
        self.__celular = celular
        self.__CUIL = CUIL
        self.__solicitudes_recibidas = []
        self.__contactos = []  # podríamos llamar a esto "contactos"
        self.__solicitudes_denegadas = []

    def get_solicitudes_recibidas(self):
        return self.__solicitudes_recibidas

    def agregar_solicitud(self, ciudadano):
        self.__solicitudes_recibidas.append(ciudadano)

    def enviarSolicitud(self, ciudadano):
        ciudadano.agregar_solicitud(self)

    def denegarSolicitud(self, ciudadano):
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            self.__solicitudes_denegadas.append(ciudadano)

    def aceptarSolicitud(self, ciudadano):
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            self.__contactos.append(ciudadano)

    def compartirEvento(self, evento, *contactos):
        self.asistirEvento(evento)
        for c in contactos:
            c.asistirEvento(evento)

    def getCantidadSolicitudesRechazadas(self):
        return len(self.__solicitudes_denegadas)

    def asistirEvento(self, evento):
        evento.sumarPersona()
