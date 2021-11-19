from Error import SolicitudError, ContactError
import AppDataBase
from Evento import Evento


import csv
from abc import ABC
import AppDataBase
from Error import RegisterError


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
                if i == 0:
                    raise RegisterError()
        except RegisterError as r:
            return r.get_mensaje()


class CiudadanoUsuario:
    def __init__(self, celular, CUIL, nombre):
        self.__nombre = nombre
        self.__celular = celular
        self.__CUIL = CUIL
        self.__solicitudes_recibidas = []
        self.__contactos = []  # podríamos llamar a esto "contactos"
        self.__solicitudes_denegadas = []

    def get_nombre(self):
        return self.__nombre

    def get_contactos(self):
        return self.__contactos

    def get_solicitudes_recibidas(self):
        return self.__solicitudes_recibidas

    def get_CUIL(self):
        return self.__CUIL

    def get_numero(self):
        return self.__celular

    def __repr__(self):
        return f"{self.get_nombre()}"

    def ver_eventos(self):
        lista_de_eventos = AppDataBase.eventos
        return lista_de_eventos

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

    def enviarSolicitud(self, celular):  # Acá iría un Except donde se evalua si el ciudadano existe en la dataset
        for c in AppDataBase.ciudadanos_usuarios:
            if c.get_numero() == celular:
                ciudadano = c
                print("Lo encontré")
                return ciudadano.agregar_solicitud(self)

    def getCantidadSolicitudesRechazadas(self):
        return len(self.__solicitudes_denegadas)

    def denegarSolicitud(self, ciudadano):
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            self.__solicitudes_denegadas.append(ciudadano)
        if ciudadano.getCantidadSolicitudesRechazadas() == 5:
            AppDataBase.administradores_usuarios[1].bloquearCiudadano(ciudadano)

    def agregar_contacto(self, ciudadano):
        """Complementa a aceptarSolicitud"""
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            self.__contactos.append(ciudadano)

    def aceptarSolicitud(self, ciudadano):
        self.__contactos.append(ciudadano)
        ciudadano.agregar_contacto(self)

    def reportarEvento(self, tipodeevento, coordenadas_tupla, fecha, hora, *contactos):
        newEvento = Evento(tipodeevento, coordenadas_tupla, fecha, hora)
        if len(contactos) != 0:
            self.asistir_y_compartirEvento(newEvento, *contactos)

    def asistir_y_compartirEvento(self, evento, *contactos):
        """Complementa a Reportar Evento, permitiendo vincular una cantidad de contactos definida por el usuario"""
        self.asistirEvento(evento)
        for c in contactos:
            c.asistirEvento(evento)

    def asistirEvento(self, evento):
        evento.sumarPersona()
