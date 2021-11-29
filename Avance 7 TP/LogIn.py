import csv
import AppDataBase
import datetime as dt
from SistemaMonitoreo import SistemaMonitoreo
from Persona_y_Ciudadano import Ciudadano
from Administrador import Administrador
from Error import CategoriaError, AdminNameError

ciudadanos_usuarios = AppDataBase.ciudadanos_usuarios
usuarios = []
claves = []
celulares = []
CUILs = []

administradores = AppDataBase.administradores_usuarios
ad_nombres = ["Admin"]
ad_claves = [000]

Tipos_de_eventos = []
eventos = AppDataBase.eventos
sensores = AppDataBase.sensores


print('¡Bienvenido! Por favor, ingresa tu información para iniciar sesión')


class Login:
    def __init__(self):

        """with open("Usuarios.csv", "r") as file_us_r:
            file_us_r = csv.reader(file_us_r, delimiter=",")
            next(file_us_r)
            for row in file_us_r:
                if len(row) != 0:
                    usuarios.append(row[0])
                    claves.append(int(row[1]))
                    CUILs.append(int(row[3]))
                    celulares.append(int(row[2]))

        with open("Administradores.csv", "r") as file_ad_r:
            file_ad_r = csv.reader(file_ad_r, delimiter=",")
            next(file_ad_r)
            for row in file_ad_r:
                if len(row) != 0:
                    ad_nombres.append(row[0])
                    ad_claves.append(int(row[1]))"""

        print("¿Cómo desea ingresar?")
        print("1: Como administrador")
        print("2: Como un usuario")
        print("3: Como un sensor")

        eleccion = int(input("\nIndique según las opciones: "))

        if eleccion == 2:
            self.__username = input("Nombre de usuario: ")
            self.__password = int(input("Clave: "))
            self.login_check_us()

        elif eleccion == 1:
            if administradores == []:
                admin = Administrador("Admin", 000)

                print("\nEres el primer administrador. Tu nombre y clave por defecto serán:")
                print("Nombre: Admin")
                print("Clave: 000")
                print("\nPodrás editarlas en las opciones posteriores a ingresar")

                self.__username = input("\nNombre de usuario: ")
                self.__password = int(input("Clave: "))

                self.login_check_ad()

            else:
                self.__username = input("\nNombre de usuario: ")
                self.__password = int(input("Clave: "))
                self.login_check_ad()

    def login_check_ad(self):
        key1 = self.__username
        value1 = self.__password

        if key1 in ad_nombres and value1 in ad_claves and ad_nombres.index(key1) == ad_claves.index(value1):
            print(f'\nIngreso como el siguiente administrador: {self.__username}')
            admin = administradores[ad_nombres.index(key1)]
            self.opciones_admin(admin)
        else:
            print("\nNombre de usuario o clave incorrecta. Pruebe con otros datos o revise mayúsculas y minúsculas.")
            print("\n1: Probar nuevamente")
            print("2: Volver")

            eleccion = int(input("\nIngrese la opción a seguir: "))

            if eleccion == 1:
                check_username = input("\nNombre de usuario: ")
                check_password = input("Clave: ")

                key, value = check_username, check_password

                if key in usuarios and value in claves and usuarios.index(key) == claves.index(value):
                    print(f'\nIngresó como el siguiente administrador: {check_username}')
                    admin = administradores[ad_nombres.index(key1)]
                    self.opciones_admin(admin)

            elif eleccion == 2:
                self.__init__()

    def opciones_admin(self, admin):
        print("\n¿Qué deseas hacer?")
        print("1: Bloquear ciudadano")
        print("2: Desbloquear ciudadano")
        print("3: Crear administrador")
        print("4: Borrar Administrador")
        print("5: Editar Administrador")
        print("6: Crear categoría de evento")
        print("7: Ver mapa")
        print("8: Ver tablero de estadística de eventos")
        print("9: Volver")

        eleccion = int(input(f"\nIngrese la opción a seguir: "))
        sm = SistemaMonitoreo()

        if eleccion == 1:
            ciudadanos = AppDataBase.ciudadanos_a_bloquear

            if ciudadanos != []:
                print("\nCiudadanos a bloquear:")
                i=0
                for c in ciudadanos:
                    i+=1
                    print(f"{i}: {c}")

                eleccion_c = int(input(f"\nIngrese el n° correspondiente al ciudadano a bloquear o 0 para volver: "))

                if eleccion_c != 0:
                    admin.bloquearCiudadano(ciudadanos[eleccion_c-1])
                    self.opciones_admin(admin)
                else:
                    self.opciones_admin(admin)
            else:
                print("\nAfortunadamente, ningún ciudadano ha sido rechazado 5 veces hasta el momento ¡Genial!")
                self.opciones_admin(admin)

        if eleccion == 2:
            ciudadanos = AppDataBase.ciudadanos_bloqueados_usuarios

            if ciudadanos != []:
                print("\nCiudadanos bloqueados:")
                i=0
                for c in ciudadanos:
                    i+=1
                    print(f"{i}: {c}")

                eleccion_c = int(input(f"\nIngrese el n° correspondiente al ciudadano a desbloquear o 0 para volver: "))

                if eleccion_c != 0:
                    admin.desbloquearCiudadano(ciudadanos[eleccion_c-1])
                    self.opciones_admin(admin)
                else:
                    self.opciones_admin(admin)
            else:
                print("\nNingún ciudadano ha sido bloqueado hasta el momento")
                self.opciones_admin(admin)

        if eleccion == 3:

            e = input("Si desea volver, marque v, sino, marque cualquier otra tecla: ")

            if e != "v":
                nombre = input("\nIngrese el nombre que se le dará al nuevo admin: ")
                clave = int(input("\nIngrese la clave que se le dará al nuevo admin: "))
                try:
                    with open("Administradores.csv", "r") as file_ad_r:
                            file_ad_r = csv.reader(file_ad_r, delimiter=",")
                            data = [row for row in file_ad_r if len(row) != 0]
                            for row in file_ad_r:
                                if len(row) != 0:
                                    if row[0] == str(nombre):
                                        raise AdminNameError()
                            else:
                                with open("Administradores.csv", "w") as file_ad_w:
                                    file_ad_w = csv.writer(file_ad_w, delimiter=",")
                                    for row in data:
                                        if len(row) != 0:
                                            file_ad_w.writerow(row)
                                    file_ad_w.writerow([nombre, clave])
                                admin.crearAdmin(nombre, clave)
                                ad_nombres.append(nombre)
                                ad_claves.append(clave)
                                self.opciones_admin(admin)
                except AdminNameError as A:
                    print(A.get_mensaje())
                    self.opciones_admin(admin)
            else:
                self.opciones_admin(admin)

        if eleccion == 4:
            if len(administradores) >= 1:
                print("\nAdministradores:")
                i=0
                for a in administradores:
                    i+=1
                    print(f"{i}: {a}")

                eleccion_a = int(input(f"\nIngrese el n° correspondiente al administrador a borrar o 0 para volver: "))

                if eleccion_a != 0:
                    ad = administradores[eleccion_a-1]
                    admin.borrarAdmin(ad)
                    with open("Administradores.csv", "r") as file_ad_r:
                        file_ad_r = csv.reader(file_ad_r, delimiter=",")
                        filtered_data = [] # la data sin la row del admin a borrar
                        for row in file_ad_r:
                            if len(row) != 0:
                                if row[0] != str(ad.get_nombre()):
                                    filtered_data.append(row)

                    with open("Administradores.csv", "w") as file_ad_w:
                        file_ad_w = csv.writer(file_ad_w, delimiter=",")
                        for row in filtered_data:
                            if len(row) != 0:
                                file_ad_w.writerow(row)

                    self.opciones_admin(admin)
                else:
                    self.opciones_admin(admin)

            else:
                print("\nUsted es el único administrador. No puede eliminarse a si mismo")
                self.opciones_admin(admin)

        if eleccion == 5:
            if len(administradores) >= 1 :
                print("\nAdministradores:")
                i=0
                for a in administradores:
                    i+=1
                    print(f"{i}: {a}")

                eleccion_a = int(input(f"\nIngrese el n° correspondiente al administrador a editar o 0 para volver: "))

                if eleccion_a != 0:
                    nombre = input(f"\nIngrese el nuevo nombre del administrador a editar: ")
                    clave = int(input(f"\nIngrese la nueva clave del administrador a editar: "))

                    admin.editarAdmin(administradores[eleccion_a-1], nombre, clave)
                    for a in ad_nombres:
                        if a == administradores[eleccion_a-1].get_nombre():
                            ad_nombres[ad_nombres.index(a)] = nombre
                    for a in ad_claves:
                        if a == administradores[eleccion_a-1].get_clave():
                            ad_claves[ad_claves.index(a)] = clave

                    print(f"{administradores[eleccion_a-1]} ha sido modificado. Su nuevo nombre es {nombre} y su nueva clave es {clave}")
                    self.opciones_admin(admin)
                else:
                    self.opciones_admin(admin)

        if eleccion == 6:
            nueva_categoria = input("\nIngrese el nombre de la nueva categoría o v para volver: ")
            if nueva_categoria != "v":
                try:
                    with open("Categorías_Eventos.csv", "r") as file_cat_r:
                        file_cat_r = csv.reader(file_cat_r, delimiter=",")
                        data = [row for row in file_cat_r if len(row) != 0]
                        for row in data:
                            if row[0] == str(nueva_categoria):
                                raise CategoriaError()
                        else:
                            with open("Categorías_Eventos.csv", "w") as file_cat_w:
                                file_cat_w = csv.writer(file_cat_w, delimiter=",")
                                for row in data:
                                    if len(row) != 0:
                                        file_cat_w.writerow(row)
                                file_cat_w.writerow([nueva_categoria])

                            admin.crearTipoDeEvento(nueva_categoria)
                            Tipos_de_eventos.append(nueva_categoria)
                            self.opciones_admin(admin)

                except CategoriaError as C:
                    print(C.get_mensaje())
                    self.opciones_admin(admin)
            else:
                self.opciones_admin(admin)

        if eleccion == 7:
            sm.mapeo_de_eventos(dt.datetime.now())
            self.opciones_admin(admin)

        if eleccion == 8:
            eventos_imp = sm.eventos_mas_impactantes()
            eventos_concurrencia = sorted(eventos, key= lambda x: x.getPersonas(), reverse=True)

            with open("Tablero_Estadística.csv", "r") as file_est_r:
                file_est_r = csv.reader(file_est_r, delimiter=",")
                data = [row for row in file_est_r if len(row) != 0]

            with open("Tablero_Estadística.csv", "w") as file_est_w:
                file_est_w = csv.writer(file_est_w, delimiter=",")
                for row in data:
                    if len(row) != 0:
                        file_est_w.writerow(row)
                for e in eventos:
                    file_est_w.writerow([eventos_imp.index(e)+1, eventos_concurrencia.index(e)+1, e.get_detalle(), e.get_tipodeevento(), e.getCoordenadas()[0], e.getCoordenadas()[1], e.get_Fecha_y_Hora(), e.getPersonas()])

            with open("Tablero_Estadística.csv", "r") as file_est_r:
                file_est_r = csv.reader(file_est_r, delimiter=",")
                for row in file_est_r:
                    print(row)

            self.opciones_admin(admin)

        if eleccion == 9:
            self.__init__()

    def login_check_us(self):
        key1 = self.__username
        value1 = self.__password

        if key1 in usuarios and value1 in claves and usuarios.index(key1) == claves.index(value1):
            print(f'\nBienvenido/a otra vez, {self.__username}')
            print(ciudadanos_usuarios)
            print(usuarios)
            usuario = ciudadanos_usuarios[usuarios.index(key1)]
            self.opciones_usuario(usuario)
        else:
            print("\nNombre de usuario o clave incorrecta. Pruebe con otros datos o revise mayúsculas y minúsculas.")
            ask = input("\n¿Es un nuevo usuario? S/N : ")

            if ask.lower() == "s":
                self.nuevo_usuario()

            if ask.lower() == 'n':
                check_username = input("\nNombre de usuario: ")
                check_password = input("Clave: ")

                key, value = check_username, check_password

                if key in usuarios and value in claves and usuarios.index(key) == claves.index(value):
                    print(f"\n¡¡Bienvenido/a otra vez, {check_username}!!")
                    usuario = ciudadanos_usuarios[usuarios.index(key1)]
                    self.opciones_usuario(usuario)
                else:
                    self.login_check_us()

    def nuevo_usuario(self):
        print("¡Nos alegra ver nuevas caras! Ven, vamos a registrarte")
        nuevo_nombre = input("\nPor favor, ingrese su nombre completo: ")
        nuevo_Cuil = int(input("Ingrese su CUIL: "))
        nuevo_celular = int(input("Ingrese su n° de celular: "))

        print("Estos datos serán usados para la validación de su cuenta.")

        nuevo_usuario_nombre = input('\nPor favor, ingrese su nombre de usuario: ')
        nueva_clave = int(input('Ingrese su clave: '))

        nuevoCiudadano = Ciudadano(nuevo_nombre, nuevo_Cuil, nuevo_celular)
        nuevoUsuario = nuevoCiudadano.registrarse(nuevo_usuario_nombre, nueva_clave)

        try:
            mensaje_validacion = f"Tu nombre de usuario será: {nuevoUsuario.get_nombre()}, y tu clave: {int(nueva_clave)}"
            print(mensaje_validacion)
            print("Inicia sesión para comprobar que ya tienes una cuenta")
        except:
            print("No pudimos validar tu cuenta con los datos dados. Intente nuevamente...")
            self.nuevo_usuario()

        with open("Usuarios.csv", "r") as file_us_r:
            file_us_rd = csv.reader(file_us_r, delimiter=",")
            data = [row for row in file_us_rd if len(row) != 0]

        with open("Usuarios.csv", "w") as file_us:
            file_us = csv.writer(file_us, delimiter=",")
            for row in data:
                if len(row) != 0:
                    file_us.writerow(row)
            file_us.writerow([nuevo_usuario_nombre, nueva_clave, nuevo_celular, nuevo_Cuil])

        usuarios.append(nuevo_usuario_nombre)
        claves.append(nueva_clave)
        celulares.append(nuevo_celular)
        CUILs.append(nuevo_Cuil)
        """with open("Usuarios.csv", "r") as file_us_r:
            file_us_rd = csv.reader(file_us_r, delimiter=",")
            next(file_us_rd)
            for row in file_us_rd:
                if len(row) != 0:
                    usuarios.append(row[0])
                    claves.append(int(row[1]))
                    CUILs.append(int(row[3]))
                    celulares.append(int(row[2]))"""

        check_username = input("\nNombre de usuario: ")
        check_password = int(input("Clave: "))

        key, value = check_username, check_password

        if key in usuarios and value in claves and usuarios.index(key) == claves.index(value):
            print(f"\n¡¡¡Bienvenido/a {check_username}!!")
            self.opciones_usuario(nuevoUsuario)
        else:
            self.login_check_us()

    def opciones_usuario(self, usuario_actual):
        print("\n¿Qué deseas hacer?")
        print("1: Enviar solicitud")
        print("2: Revisar solicitudes recibidas")
        print("3: Reportar evento")
        print("4: Ver mapa")
        print("5: Ver tablero de estadística de eventos")
        print("6: Ver contactos")
        print("7: Cambiar de cuenta")

        eleccion = int(input("\nElige tu opción a seguir: "))

        sm = SistemaMonitoreo()

        if eleccion == 1:
            self.enviar_solicitud(usuario_actual)

        if eleccion == 2:
            self.revisar_solicitudes(usuario_actual)

        if eleccion == 3:
            self.reportar_evento(usuario_actual)

        if eleccion == 4:
            sm.mapeo_de_eventos(dt.datetime.now())
            self.opciones_usuario(usuario_actual)

        if eleccion == 5:
            eventos_imp = sm.eventos_mas_impactantes()
            eventos_concurrencia = sorted(eventos, key=lambda x: x.getPersonas(), reverse=True)

            with open("Tablero_Estadística.csv", "r") as file_est_r:
                file_est_r = csv.reader(file_est_r, delimiter=",")
                data = [row for row in file_est_r if len(row) != 0]

            with open("Tablero_Estadística.csv", "w") as file_est_w:
                file_est_w = csv.writer(file_est_w, delimiter=",")
                for row in data:
                    if len(row) != 0:
                        file_est_w.writerow(row)
                for e in eventos:
                    file_est_w.writerow([eventos_imp.index(e)+1, eventos_concurrencia.index(e)+1, e.get_detalle(), e.get_tipodeevento(), e.getCoordenadas()[0], e.getCoordenadas()[1], e.get_Fecha_y_Hora(), e.getPersonas()])

            with open("Tablero_Estadística.csv", "r") as file_est_r:
                file_est_r = csv.reader(file_est_r, delimiter=",")
                for row in file_est_r:
                    if len(row) != 0:
                        print(f" {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} |")

            self.opciones_usuario(usuario_actual)

        if eleccion == 6:
            contactos = usuario_actual.get_contactos()
            for c in contactos:
                print(c)
            self.cambiar_de_cuenta()

        if eleccion == 7:
            self.cambiar_de_cuenta()

    def enviar_solicitud(self, usuario_actual):
        print("\n¿A quién deseas enviar una solicitud?")
        print(ciudadanos_usuarios)
        print(AppDataBase.ciudadanos_usuarios)
        celular_o_cuil = int(input("Indique el cuil/celular del usuario: "))

        if usuario_actual.enviarSolicitud(celular_o_cuil) != None:
            print(f"\n{usuario_actual.enviarSolicitud(celular_o_cuil)}")
        else:
            print("\n Deberás esperar a que tu solicitud sea respondida")

        self.opciones_usuario(usuario_actual)

    def revisar_solicitudes(self, usuario_actual):

        solicitudes_recibidas = usuario_actual.get_solicitudes_recibidas()

        print("\nHas recibido las solicitudes de:")

        i = 0
        for s in solicitudes_recibidas:
            i+=1
            print(f"{i}: {s}")

        eleccion_usuario = int(input("\nElige un usuario: "))

        print("\n¿Qué desear hacer?")
        print("1: Aceptar solicitud")
        print("2: Denegar solicitud")
        print("3: Cambiar usuario elegido")
        print("4: Volver")

        eleccion = int(input("\nElige tu opción a seguir: "))

        if eleccion == 1:
            print(f"¡Ahora {solicitudes_recibidas[eleccion_usuario-1]} y tú son amigos!")
            usuario_actual.aceptarSolicitud(solicitudes_recibidas[eleccion_usuario-1])

            self.opciones_usuario(usuario_actual)

        if eleccion == 2:
            print(f"{solicitudes_recibidas[eleccion_usuario-1]} ha sido rechazado/a")
            usuario_actual.denegarSolicitud(solicitudes_recibidas[eleccion_usuario-1])

            self.opciones_usuario(usuario_actual)

        if eleccion == 3:
            eleccion_usuario = int(input("\nElige un usuario: "))
            self.revisar_solicitudes(usuario_actual)

        if eleccion == 4:
            self.opciones_usuario(usuario_actual)

    def reportar_evento(self, usuario_actual):

        print("\nCategorías disponibles")
        i=0
        for t in Tipos_de_eventos:
            i+=1
            print(f"{i}: {t}")

        eleccion_t = int(input("Indique de qué tipo de evento se trata o 0 para volver: "))

        if eleccion_t != 0:

            print("\n¿Con quién te encuentras?")
            print("1: Solo")
            i=1
            for c in usuario_actual.get_contactos():
                i+=1
                print(f"{i}: {c}")

            eleccion_c = input("\nIngrese su elección o v para volver (si se trata de más de una persona, seleccione números separados por comas): ")

            if eleccion_c == "v":
                self.opciones_usuario(usuario_actual)

            detalle = input("\nIngrese una breve descripción o título del evento: ")
            coordenadas_x = int(input("Ingrese las coordenadas x del evento: "))
            coordenadas_y = int(input("Ingrese las coordenadas y del evento: "))
            tup = (coordenadas_x, coordenadas_y)

            tipodeevento = Tipos_de_eventos[eleccion_t-1]

            fecha_y_hora = dt.datetime.now()

            if eleccion_c != "1":
                invitados = []
                lista_eleccion = list(eleccion_c.split(","))
                for i in lista_eleccion:
                    invitados.append(usuario_actual.get_contactos()[int(i)-2])

                evento = usuario_actual.reportarEvento(detalle, tipodeevento, tup, fecha_y_hora, invitados)
                with open("Tablero_Eventos.csv", "r") as file_ev_r:
                    file_ev_r = csv.reader(file_ev_r, delimiter=",")
                    data = [row for row in file_ev_r if len(row) != 0]

                with open("Tablero_Eventos.csv", "w") as file_ev_w:
                    file_ev_w = csv.writer(file_ev_w, delimiter=",")
                    for row in data:
                        if len(row) != 0:
                            file_ev_w.writerow(row)
                    file_ev_w.writerow([detalle, tipodeevento, coordenadas_x, coordenadas_y, fecha_y_hora, evento.getPersonas()])
                print(f"Ha reportado el evento {detalle} del tipo {tipodeevento}, lugar: ({coordenadas_x}, {coordenadas_y}), a las {fecha_y_hora}")
                self.opciones_usuario(usuario_actual)

            if eleccion_c == "1":
                evento = usuario_actual.reportarEvento(detalle, tipodeevento, tup, fecha_y_hora, [])
                with open("Tablero_Eventos.csv", "r") as file_ev_r:
                    file_ev_r = csv.reader(file_ev_r, delimiter=",")
                    data = [row for row in file_ev_r if len(row) != 0]

                with open("Tablero_Eventos.csv", "w") as file_ev_w:
                    file_ev_w = csv.writer(file_ev_w, delimiter=",")
                    for row in data:
                        if len(row) != 0:
                            file_ev_w.writerow(row)
                    file_ev_w.writerow([detalle, tipodeevento, coordenadas_x, coordenadas_y, fecha_y_hora, evento.getPersonas()])
                print(f"Ha reportado el evento {detalle} del tipo {tipodeevento}, lugar: ({coordenadas_x}, {coordenadas_y}), a las {fecha_y_hora}")
                self.opciones_usuario(usuario_actual)
        else:
            self.opciones_usuario(usuario_actual)

                #tenes que armar la tabla de eventos
                #podríamos hacer que en usuarios haya una columna que diga si está bloqueado o no

    def cambiar_de_cuenta(self):
        self.__init__()


main = Login()
"""main.login_check()"""
