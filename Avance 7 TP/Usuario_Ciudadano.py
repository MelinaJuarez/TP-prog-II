from Error import SolicitudError, ContactError, NoContactError, UserError
import AppDataBase
from Evento import Evento

import csv
from abc import ABC
import AppDataBase
from Error import RegisterError


class CiudadanoUsuario:
    def __init__(self, nombre, CUIL, celular, clave):
        self.__nombre = nombre
        self.__celular = celular
        self.__CUIL = CUIL
        self.__solicitudes_recibidas = []
        self.__contactos = []
        self.__solicitudes_denegadas = 0
        self.__clave = clave

    def get_nombre(self):
        return self.__nombre

    def get_clave(self):
        return self.__clave

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
                if ciudadano not in self.get_solicitudes_recibidas():  # acordate que cambian de lugar el contacto y el self de enviarSolicitud
                    self.__solicitudes_recibidas.append(ciudadano)
                    ciudadano.get_solicitudes_recibidas()
                else:
                    raise SolicitudError()
            else:
                raise ContactError()
        except SolicitudError as s:
            return s.get_mensaje()
        except ContactError as c:
            return c.get_mensaje()

    def enviarSolicitud(self, celular_o_cuil):
        try:
            for c in AppDataBase.ciudadanos_usuarios:
                if c.get_numero() == celular_o_cuil or c.get_CUIL() == celular_o_cuil:
                    ciudadano = c
                    return ciudadano.agregar_solicitud(self)
            else:
                raise UserError()
        except UserError as u:
            return u.get_mensaje()

    def getSolicitudesRechazadas(self):
        return self.__solicitudes_denegadas

    def agregarSolicitudesRechazadas(self):
        self.__solicitudes_denegadas += 1
        return self.__solicitudes_denegadas

    def denegarSolicitud(self, ciudadano):
        self.__solicitudes_recibidas.remove(ciudadano)
        ciudadano.agregarSolicitudesRechazadas()
        if ciudadano.getSolicitudesRechazadas() == 5:
            """AppDataBase.administradores_usuarios[0].bloquearCiudadano(ciudadano)"""
            AppDataBase.ciudadanos_a_bloquear.append(ciudadano)

    def agregar_contacto(self, ciudadano):
        """Complementa a aceptarSolicitud"""
        self.__contactos.append(ciudadano)
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)

    def aceptarSolicitud(self, ciudadano):
        ciudadano.agregar_contacto(self)
        self.__contactos.append(ciudadano)

    def reportarEvento(self, detalle, tipodeevento, coordenadas_tupla, fecha_y_hora, contactos):
        try:
            if len(contactos) == 0:
                newEvento = Evento(detalle, tipodeevento, coordenadas_tupla, fecha_y_hora)
                self.asistirEvento(newEvento)
                return newEvento
            else:
                for c in contactos:
                    if c in self.get_contactos():
                        newEvento = Evento(detalle, tipodeevento, coordenadas_tupla, fecha_y_hora)
                        self.asistir_y_compartirEvento(newEvento, contactos)
                        return newEvento
                    else:
                        raise NoContactError()
        except NoContactError as n:
            return n.get_mensaje()

    def asistir_y_compartirEvento(self, evento, contactos):
        """Complementa a Reportar Evento, permitiendo vincular una cantidad de contactos definida por el usuario"""
        self.asistirEvento(evento)
        for c in contactos:
            c.asistirEvento(evento)

    def asistirEvento(self, evento):
        evento.sumarPersona()
