class Evento:
    __Cantidad_de_Personas = 0

    def __init__(self, TipoDeEvento, Coordenada):
        self.__TipoDeEvento = TipoDeEvento
        self.__Coordenada = Coordenada

    def sumarPersona(self):
        self.__Cantidad_de_Personas += 1

    def getPersona(self):
        return self.__Cantidad_de_Personas

    def getCoordenadas(self):
        return self.__Coordenada
