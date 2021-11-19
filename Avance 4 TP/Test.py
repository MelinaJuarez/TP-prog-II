import csv
import unittest
import AppDataBase
import Map
from Evento import Evento
from Persona_y_Ciudadano import Persona
from Error import RegisterError, NoContactError, ContactError, SolicitudError
from Administrador import Administrador
from Sensor import Sensor


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
        self.__solicitudes_denegadas = 0

    def get_nombre(self):
        return self.__nombre

    def get_contactos(self):
        return self.__contactos

    def get_solicitudes_recibidas(self):
        return self.__solicitudes_recibidas

    """def agregar_solicitud_recibida(self, ciudadano):
        self.__solicitudes_recibidas.append(ciudadano)
        return self.__solicitudes_recibidas"""

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
                    ciudadano.__solicitudes_recibidas.append(self)
                    return ciudadano.get_solicitudes_recibidas()
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


    def getSolicitudesRechazadas(self):
        return self.__solicitudes_denegadas

    def agregarSolicitudesRechazadas(self):
        self.__solicitudes_denegadas += 1
        return self.__solicitudes_denegadas

    def denegarSolicitud(self, ciudadano):
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            ciudadano.agregarSolicitudesRechazadas()
        if ciudadano.getSolicitudesRechazadas() == 5:
            AppDataBase.administradores_usuarios[1].bloquearCiudadano(ciudadano)

    def fakedenegarSolicitud(self, ciudadano):
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            return ciudadano.agregarSolicitudesRechazadas()
        if ciudadano.getSolicitudesRechazadas() == 5:
            AppDataBase.administradores_usuarios[1].bloquearCiudadano(ciudadano)
            return f"{ciudadano} ha sido bloqueado/a"

    def agregar_contacto(self, ciudadano):
        """Complementa a aceptarSolicitud"""
        if ciudadano in self.__solicitudes_recibidas:
            self.__solicitudes_recibidas.remove(ciudadano)
            self.__contactos.append(ciudadano)
        else:
            self.__contactos.append(ciudadano)

    def aceptarSolicitud(self, ciudadano):
        self.__contactos.append(ciudadano)
        ciudadano.agregar_contacto(self)
        return self.__contactos

    def reportarEvento(self, tipodeevento, coordenadas_tupla, fecha, hora, *contactos):
        try:
            for c in contactos:
                if c in self.get_contactos():
                    newEvento = Evento(tipodeevento, coordenadas_tupla, fecha, hora)
                    if len(contactos) != 0:
                        self.asistir_y_compartirEvento(newEvento, *contactos)
                else:
                    raise NoContactError()
        except NoContactError as n:
            n.get_mensaje()

    def asistir_y_compartirEvento(self, evento, *contactos):
        """Complementa a Reportar Evento, permitiendo vincular una cantidad de contactos definida por el usuario"""
        self.asistirEvento(evento)
        for c in contactos:
            c.asistirEvento(evento)

    def asistirEvento(self, evento):
        evento.sumarPersona()


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
        Anastasio = Ciudadano("Anastasio", 74126, 102358)
        Marti_Usuario = Marti.registrarse()
        Felix_Usuario = Felix.registrarse()
        Jose_Usuario = Jose.registrarse()
        Anastasio_Usuario = Anastasio.registrarse()
        Marti_Usuario.enviarSolicitud(123456)
        Felix_Usuario.aceptarSolicitud(Marti_Usuario)
        Jose_Usuario.enviarSolicitud(654987)
        Jose_Usuario.enviarSolicitud(45612)
        Felix_Usuario.aceptarSolicitud(Jose_Usuario)
        Marti_Usuario.enviarSolicitud(Anastasio_Usuario)
        self.assertEqual("El contacto ya existe dentro de tus contactos", Felix_Usuario.enviarSolicitud(654987))
        self.assertEqual("Ya enviaste una solicitud a este contacto", Jose_Usuario.enviarSolicitud(654987))
        self.assertEqual("El contacto ya existe dentro de tus contactos", Jose_Usuario.enviarSolicitud(45612))

    def test_fake_denegar_solicitud(self):
        Marti = Ciudadano("Marti", 78945, 654987)
        Felix = Ciudadano("Felix", 45612, 123456)
        Jose = Ciudadano("Josefina", 95115, 753357)
        Charly = Ciudadano("Charly", 41036, 840369)
        Gertrudis = Ciudadano("Gertrudis", 41206, 985206)
        Anastasio = Ciudadano("Anastasio", 74126, 102358)
        Rodri = Ciudadano("Rodrigo", 45035, 741650)
        Marti_Usuario = Marti.registrarse()
        Felix_Usuario = Felix.registrarse()
        Jose_Usuario = Jose.registrarse()
        Charly_Usuario = Charly.registrarse()
        Gertrudis_Usuario = Gertrudis.registrarse()
        Anastasio_Usuario = Anastasio.registrarse()
        Rodri_Usuario = Rodri.registrarse()
        Marti_Usuario.enviarSolicitud(123456)
        Marti_Usuario.enviarSolicitud(753357)
        Marti_Usuario.enviarSolicitud(840369)
        Marti_Usuario.enviarSolicitud(985206)
        Felix_Usuario.fakedenegarSolicitud(Marti_Usuario)
        Jose_Usuario.fakedenegarSolicitud(Marti_Usuario)
        Charly_Usuario.fakedenegarSolicitud(Marti_Usuario)
        Gertrudis_Usuario.fakedenegarSolicitud(Marti_Usuario)
        self.assertEqual("Martina Sipowicz ha sido bloqueado/a", Marti_Usuario.enviarSolicitud(102358))

if __name__ == '__main__':
    unittest.main()
