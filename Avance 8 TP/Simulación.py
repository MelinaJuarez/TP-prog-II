import AppDataBase
from Administrador import Administrador
from Sensor import Sensor
from SistemaMonitoreo import SistemaMonitoreo
import random
import datetime
from Persona_y_Ciudadano import Ciudadano

fecha = datetime.date(2021, 11, random.randint(1,30))
hora = datetime.time(random.randint(0,23), random.randint(0,59))
EventIt = SistemaMonitoreo("EventIt")
A1 = Administrador()
Entretenimiento = A1.crearTipoDeEvento("Entretenimiento")
Salud = A1.crearTipoDeEvento("Salud")
Seguridad = A1.crearTipoDeEvento("Seguridad")
Categorias = [Entretenimiento, Salud, Seguridad]

for i in range(10):
    s = Sensor(Categorias[random.randint(0, 2)], (random.randint(0, 24), random.randint(0, 19)))
    s.reportarEvento(fecha, hora)

Marti = Ciudadano("Marti", 78945, 654987)
Felix = Ciudadano("Felix", 45612, 123456)
Jose = Ciudadano("Josefina", 95115, 753357)
Marti_Usuario = Marti.registrarse()
Felix_Usuario = Felix.registrarse()
Jose_Usuario = Jose.registrarse()
Marti_Usuario.enviarSolicitud(123456)
Felix_Usuario.aceptarSolicitud(Marti_Usuario)
Jose_Usuario.enviarSolicitud(654987)
Jose_Usuario.enviarSolicitud(45612)
Felix_Usuario.aceptarSolicitud(Jose_Usuario)

evento1 = AppDataBase.eventos[0]
Felix_Usuario.asistir_y_compartirEvento(evento1, Marti_Usuario, Jose_Usuario)
evento5 = AppDataBase.eventos[4]
Marti_Usuario.asistir_y_compartirEvento(evento5, Jose_Usuario)
evento3 = AppDataBase.eventos[2]
Jose_Usuario.asistirEvento(evento3)
#print(EventIt.get_eventos())
EventIt.mapeo_de_eventos(fecha)

print(EventIt.zonas_delimitadas())
for b in EventIt.zonas_delimitadas():
    print(EventIt.ordenar_eventos_de_barrio(b[0]))

print(EventIt.eventos_mas_impactantes())
