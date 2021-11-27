class Barrio:
    def __init__(self, nombre, CoordenadaXExtremoNorOeste, CoordenadaYExtremoNorOeste, CoordenadaXExtremoSurOeste, CoordenadaYExtremoSurOeste, CoordenadaXExtremoNorEste, CoordenadaYExtremoNorEste, CoordenadaXExtremoSurEste, CoordenadaYExtremoSurEste):
        self.__nombre = nombre
        self.__CoordenadaXExtremoNorOeste = CoordenadaXExtremoNorOeste
        self.__CoordenadaYExtremoNorOeste = CoordenadaYExtremoNorOeste
        self.__CoordenadaXExtremoSurOeste = CoordenadaXExtremoSurOeste
        self.__CoordenadaYExtremoSurOeste = CoordenadaYExtremoSurOeste
        self.__CoordenadaXExtremoNorEste = CoordenadaXExtremoNorEste
        self.__CoordenadaYExtremoNorEste = CoordenadaYExtremoNorEste
        self.__CoordenadaXExtremoSurEste = CoordenadaXExtremoSurEste
        self.__CoordenadaYExtremoSurEste = CoordenadaYExtremoSurEste
        # coord para delimitar un área

    def __repr__(self):
        return self.__nombre

    def getNombre(self):
        return self.__nombre

    def getCoordenadasExtremoNorOeste(self):
        tup = (self.__CoordenadaXExtremoNorOeste, self.__CoordenadaYExtremoNorOeste)
        return tup

    def getCoordenadasExtremoSurOeste(self):
        tup = (self.__CoordenadaXExtremoSurOeste, self.__CoordenadaYExtremoSurOeste)
        return tup

    def getCoordenadasExtremoNorEste(self):
        tup = (self.__CoordenadaXExtremoNorEste, self.__CoordenadaYExtremoNorEste)
        return tup

    def getCoordenadasExtremoSurEste(self):
        tup = (self.__CoordenadaXExtremoSurEste, self.__CoordenadaYExtremoSurEste)
        return tup

