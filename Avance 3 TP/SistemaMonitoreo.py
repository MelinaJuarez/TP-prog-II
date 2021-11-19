import csv
import AppDataBase
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class SistemaMonitoreo:
    __sensores = AppDataBase.sensores
    __eventos = AppDataBase.eventos
    __usuarios_ciudadanos = AppDataBase.ciudadanos_usuarios

    def __init__(self, nombre):
        self.__nombre = nombre

    def get_eventos(self):
        return self.__eventos

    def ordenar_eventos_por_barrio(self):
        coord_barrios = []
        with open("datasetAnses.csv") as csv_file:
            archivo = csv.reader(csv_file, delimiter=",")
            header = next(archivo)
            i = 0
            for row in archivo:
                while i <= len(coord_barrios):
                    if row[3] in coord_barrios[i]:
                        coord_barrios[i][2] += 1 # Si el barrio vuelve a repetirse, se le suma una persona a sus habitantes
                        i += 1
                    else:
                        mini_list = []
                        mini_list.append(row[3])
                        tup = (row[4], row[5])
                        mini_list.append(tup)
                        coord_barrios.append(mini_list)
                        cantidad_de_habitantes = 1
                        mini_list.append(cantidad_de_habitantes)
                        i += 1
            coord_barrios.sort(key=lambda x: x[2])
        for e in AppDataBase.eventos:
            coord_e = e.getCoordenadas()
            while i <= len(coord_barrios):
                if coord_e[0] <= coord_barrios[i][1][0] and coord_e[0]


    def eventos_mas_impactantes(self):
        eventos_impactantes = []
        coord_barrios = []
        with open("datasetAnses.csv") as csv_file:
            archivo = csv.reader(csv_file, delimiter=",")
            header = next(archivo)
            i = 0
            for row in archivo:
                while i <= len(coord_barrios):
                    if row[3] in coord_barrios[i]:
                        coord_barrios[i][2] += 1 # Si el barrio vuelve a repetirse, se le suma una persona a sus habitantes
                        i += 1
                    else:
                        mini_list = []
                        mini_list.append(row[3])
                        tup = (row[4], row[5])
                        mini_list.append(tup)
                        coord_barrios.append(mini_list)
                        cantidad_de_habitantes = 1
                        mini_list.append(cantidad_de_habitantes)
                        i += 1
            coord_barrios.sort(key=lambda x: x[2])
        for e in AppDataBase.eventos:
            tup = e.getCoordenadas()
            if tup[0] <= 12.5 and :





    def crear_tabla_estadistica(self):
        with open("Estadísticas.csv", "w") as file_est:
            pass

    def mapeo_de_eventos(self, fecha):
        # Coord de los eventos
        coordenada_x = []
        coordenada_y = []
        concurrencia = []

        for e in self.__eventos:
            if e.get_fecha() == fecha:
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
