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
