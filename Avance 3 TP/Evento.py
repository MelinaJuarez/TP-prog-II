import AppDataBase


class Evento:
    __Cantidad_de_Personas = 0

    def __init__(self, TipoDeEvento, Coordenada, Fecha, Hora):
        self.__TipoDeEvento = TipoDeEvento
        self.__Coordenada = Coordenada
        self.__Fecha = Fecha
        self.__Hora = Hora
        AppDataBase.eventos.append(self)

    def get_fecha(self):
        return self.__Fecha

    def sumarPersona(self):
        self.__Cantidad_de_Personas += 1

    def getPersonas(self):
        return self.__Cantidad_de_Personas

    def getCoordenadas(self):
        return self.__Coordenada
