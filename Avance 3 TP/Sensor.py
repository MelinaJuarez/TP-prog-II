from Evento import Evento
import AppDataBase


class Sensor:
    def __init__(self, TipoDeEvento, coordenadas):
        self.__TipoDeEvento = TipoDeEvento
        self.__coordenadas = coordenadas
        AppDataBase.sensores.append(self)

    def reportarEvento(self, fecha, hora):
        newEvento = Evento(self.__TipoDeEvento, self.__coordenadas, fecha, hora)
        return newEvento
