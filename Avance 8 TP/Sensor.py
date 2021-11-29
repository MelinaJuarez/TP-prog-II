from Evento import Evento
import AppDataBase


class Sensor:
    def __init__(self, TipoDeEvento, coordenadas):
        self.__TipoDeEvento = TipoDeEvento
        self.__coordenadas = coordenadas
        AppDataBase.sensores.append(self)

    def get_tipo_de_evento(self):
        return self.__TipoDeEvento

    def get_ubicacion(self):
        return self.__coordenadas

    def reportarEvento(self, fecha_y_hora):
        newEvento = Evento("Reporte de sensor", self.__TipoDeEvento, self.__coordenadas, fecha_y_hora)
        return newEvento
