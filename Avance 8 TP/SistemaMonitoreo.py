import csv
import AppDataBase
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from Zona import Barrio


def contador_rows():
    rowcount = 0
    for row in open("datasetAnses.csv"):
        rowcount += 1
    return rowcount


class SistemaMonitoreo:

    """def __init__(self, nombre):
        self.__nombre = nombre
    """

    def __init__(self):
        self.__sensores = AppDataBase.sensores
        self.__eventos = AppDataBase.eventos
        self.__usuarios_ciudadanos = AppDataBase.ciudadanos_usuarios

    def get_eventos(self):
        return self.__eventos

    def zonas_delimitadas(self):
        barrios = []
        with open("datasetAnses.csv") as csv_file:
            archivo = csv.reader(csv_file, delimiter=",")
            header = next(archivo)
            barrios_obj = []
            barrios_nombres = []
            barrios_habitantes = []
            for row in archivo:
                barrio = Barrio(row[3], float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]))
                if barrio.getNombre() not in barrios_nombres:
                    barrios_obj.append(barrio)
                    barrios_nombres.append(barrio.getNombre())
                    barrios_habitantes.append(1)
                else:
                    i = barrios_nombres.index(barrio.getNombre())
                    barrios_habitantes[i] += 1
            for i in range(len(barrios_obj)):
                mini_list = []
                mini_list.append(barrios_obj[i])
                mini_list.append(barrios_habitantes[i])
                barrios.append(mini_list)
        return barrios

    def ordenar_eventos_de_barrio(self, barrio):
        eventos_por_barrio = []
        for e in self.__eventos:
            coord_e = e.getCoordenadas()
            if coord_e[0] <= barrio.getCoordenadasExtremoNorEste()[0] and coord_e[1] >= barrio.getCoordenadasExtremoSurEste()[1] and coord_e[0] >= barrio.getCoordenadasExtremoNorOeste()[0] and coord_e[1] <= barrio.getCoordenadasExtremoNorOeste()[1]:
                eventos_por_barrio.append(e)
        return eventos_por_barrio

    def eventos_mas_impactantes(self):
        eventos_impactantes = []
        for b in self.zonas_delimitadas():
            eventos_de_barrio = self.ordenar_eventos_de_barrio(b[0])
            eventos_impactantes += eventos_de_barrio
        habitantes_del_barrio = self.zonas_delimitadas()[1]
        eventos_impactantes.sort(key=lambda habitantes: habitantes_del_barrio, reverse=True)
        return eventos_impactantes

    def mapeo_de_eventos(self, fecha):
        # Coord de los eventos
        coordenada_x = []
        coordenada_y = []
        concurrencia = []
        for e in self.__eventos:
            if e.get_Fecha_y_Hora().strftime("%x") == fecha.strftime("%x"):
                tup = e.getCoordenadas()
                coordenada_x.append(tup[0])
                coordenada_y.append(tup[1])
                porcentaje = (e.getPersonas()/len(AppDataBase.ciudadanos_usuarios)) * 100
                concurrencia.append(porcentaje)

        # Graficar coordenadas
        fig = plt.figure()
        ax = fig.add_subplot(111)
        sc = ax.scatter(x=coordenada_x, y=coordenada_y, c= concurrencia)

        matplotlib.pyplot.grid(visible=True, which='major', axis='both')

        # Graficar mapa (Rectangulo)
        punto_origen = (0, 0)
        ancho = 25
        alto = 20
        ax.add_patch(
            patches.Rectangle(
                xy=punto_origen,
                width=ancho,
                height=alto,
                linewidth=2,
                color='black',
                fill=False))
        ax.set_title("Coordenadas de eventos")

        x = [0, 25]
        y = [10, 10]

        plt.plot(x, y, linewidth=1, color="black")

        x = [12.5, 12.5]
        y = [0, 20]

        plt.plot(x, y, linewidth=1, color="black")

        cbar = fig.colorbar(sc)
        cbar.set_label("Concurrencia (%)", loc='top')

        # Guardar grafico
        filename = r"C:\Users\Melina\PycharmProjects\TP.png"
        plt.savefig(filename)

        # Mostrar grafico
        plt.show()
        return coordenada_x, coordenada_y


"""EventIt = SistemaMonitoreo("EventIt")
print(EventIt.zonas_delimitadas())
print(EventIt.ordenar_eventos_de_barrio())"""

