import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Coord de los eventos
coordenada_x = []
coordenada_y = []

# Graficar coordenadas
fig = plt.figure()
ax = fig.add_subplot(111)
sc = ax.scatter(x=coordenada_x, y=coordenada_y)

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
cbar.set_label("Concurrencia", loc='top')

# Guardar grafico
filename = r"C:\Users\Melina\PycharmProjects\TP.png"
plt.savefig(filename)

# Mostrar grafico
plt.show()

