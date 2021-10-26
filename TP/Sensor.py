from Evento import Evento


class Sensor:
    def __init__(self, TipoDeEvento, coordenadas):
        self.TipoDeEvento = TipoDeEvento
        self.coordenadas = coordenadas

    def reportarEvento(self):
        newEvento = Evento(self.TipoDeEvento, self.coordenadas)
