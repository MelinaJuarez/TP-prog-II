from Error import SolicitudError, ContactError


class SistemaMonitoreo:
    __sensores = []
    __eventos = []
    __usuarios_ciudadanos = []

    def __init__(self, nombre):
        self.nombre = nombre

#  Falta desarrollar
