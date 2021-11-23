from abc import ABC


class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre


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

    def agregar_solicitud(self, contacto):
        self.__solicitudes_recibidas.append(contacto)

    def enviarSolicitud(self, contacto):
        contacto.agregar_solicitud(self)
        return contacto.get_solicitudes_recibidas()

    def asistirEvento(self, evento):
        evento.sumarPersona()

    def compartirEvento(self, evento, *contactos):
        self.asistirEvento(evento)
        for c in contactos:
            c.asistirEvento(evento)


Pepe = Ciudadano(458693, 753159, "P")
Meli = Ciudadano(695482, 123123, "M")
Juan = Ciudadano(635241, 321321, "J")
# print(Meli.enviarSolicitud(Juan))


class Evento:
    __Cantidad_de_Personas = 0

    def __init__(self, TipoDeEvento, Coordenada):
        self.__TipoDeEvento = TipoDeEvento
        self.__Coordenada = Coordenada

    def sumarPersona(self):
        self.__Cantidad_de_Personas += 1

    def getPersonas(self):
        return self.__Cantidad_de_Personas

    def getCoordenadas(self):
        return self.__Coordenada


Ev1 = Evento("Fiesta", 123123)
Ev2 = Evento("Fiesta", 258369)
Ev3 = Evento("Feria", 456456)
Meli.asistirEvento(Ev1)
Juan.asistirEvento(Ev1)

Juan.asistirEvento(Ev2)

print(Ev1.getPersonas())
print(Ev2.getPersonas())
Pepe.compartirEvento(Ev3, Meli, Juan)

print(Ev3.getPersonas())
