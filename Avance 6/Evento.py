import AppDataBase


class Evento:

    def __init__(self, detalle, TipoDeEvento, Coordenada, Fecha_y_Hora):
        self.__detalle = detalle
        self.__TipoDeEvento = TipoDeEvento
        self.__Coordenada = Coordenada
        self.__Fecha_y_Hora = Fecha_y_Hora
        self.__Cantidad_de_Personas = 0
        AppDataBase.eventos.append(self)

    def get_detalle(self):
        return self.__detalle

    def get_Fecha_y_Hora(self):
        return self.__Fecha_y_Hora

    def sumarPersona(self):
        self.__Cantidad_de_Personas += 1

    def getPersonas(self):
        return self.__Cantidad_de_Personas

    def getCoordenadas(self):
        return self.__Coordenada
