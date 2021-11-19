import csv
import unittest
import AppDataBase
from Evento import Evento
from Persona_y_Ciudadano import Persona
from Error import RegisterError
from Administrador import Administrador
from Sensor import Sensor


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
    def __init__(self, nombre, cuil, celular):
        super().__init__(nombre)
        self.__cuil = cuil
        self.__celular = celular

    def fake_registrarse(self):
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
                        return "Registrado con éxito"
                if i == 0:
                    raise RegisterError()
        except RegisterError as r:
            return r.get_mensaje()

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


class CiudadanoUsuario:
    def __init__(self, nombre, CUIL, celular):
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

    def enviarSolicitud(self, celular_o_cuil):  # Acá iría un Except donde se evalua si el ciudadano existe en la dataset
        for c in AppDataBase.ciudadanos_usuarios:
            if c.get_numero() == celular_o_cuil or c.get_CUIL() == celular_o_cuil:
                ciudadano = c
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

    def reportarEvento(self, tipodeevento, coordenadas, fecha, hora, *contactos):
        newEvento = Evento(tipodeevento, coordenadas, fecha, hora)
        if len(contactos) != 0:
            self.compartirEvento(newEvento, *contactos)

    def compartirEvento(self, evento, *contactos):
        """Complementa a Reportar Evento, permitiendo vincular una cantidad de contactos definida por el usuario"""
        self.asistirEvento(evento)
        for c in contactos:
            c.asistirEvento(evento)

    def asistirEvento(self, evento):
        evento.sumarPersona()


class SistemaMonitoreo:
    __sensores = []
    __eventos = AppDataBase.eventos
    __usuarios_ciudadanos = AppDataBase.ciudadanos_usuarios

    def __init__(self, nombre):
        self.__nombre = nombre

    def mapeo_de_eventos(self, fecha):
        for e in self.__eventos:
            if e.get_fecha() == fecha:
                tup = e.getCoordenadas()
                Map.coordenada_x.append(tup[0])
                Map.coordenada_y.append(tup[1])
        return Map.plt.show()


class MyTestCase(unittest.TestCase):
    def test_registrarse(self):
        Marti = Ciudadano("Marti", 78945, 654987)
        Felix = Ciudadano("Felix", 45612, 123456)
        Jose = Ciudadano("Josefina", 95115, 753357)
        Pedro = Ciudadano("Pedro", 55555, 121212)
        self.assertEqual("Registrado con éxito", Marti.fake_registrarse())
        self.assertEqual("Registrado con éxito", Felix.fake_registrarse())
        self.assertEqual("Registrado con éxito", Jose.fake_registrarse())
        self.assertEqual("Los datos ingresados no son válidos.", Pedro.fake_registrarse())

    def test_enviar_solicitud(self):
        Marti = Ciudadano("Marti", 78945, 654987)
        Felix = Ciudadano("Felix", 45612, 123456)
        Jose = Ciudadano("Josefina", 95115, 753357)
        Marti_Usuario = Marti.registrarse()
        Felix_Usuario = Felix.registrarse()
        Jose_Usuario = Jose.registrarse()
        Marti_Usuario.enviarSolicitud(123456)
        Felix_Usuario.aceptarSolicitud(Marti_Usuario)
        Jose_Usuario.enviarSolicitud(654987)
        Jose_Usuario.enviarSolicitud(45612)
        Felix_Usuario.aceptarSolicitud(Jose_Usuario)
        self.assertEqual("El contacto ya existe dentro de tus contactos", Felix_Usuario.enviarSolicitud(654987))
        self.assertEqual("Ya enviaste una solicitud a este contacto", Jose_Usuario.enviarSolicitud(654987))
        self.assertEqual("El contacto ya existe dentro de tus contactos", Jose_Usuario.enviarSolicitud(45612))


if __name__ == '__main__':
    unittest.main()
