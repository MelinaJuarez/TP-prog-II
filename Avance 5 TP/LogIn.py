import csv
import AppDataBase
from Persona_y_Ciudadano import Ciudadano
from Administrador import Administrador

ciudadanos_usuarios = AppDataBase.ciudadanos_usuarios
usuarios = []
claves = []
celulares = []
CUILs = []

administradores = AppDataBase.administradores_usuarios
ad_nombres = []
ad_claves = []

Tipos_de_eventos = []
sensores = AppDataBase.sensores

"""with open("Usuarios.csv", "w") as file_us:
    file_us = csv.writer(file_us, delimiter=",")
    header = ["Usuarios", "Clave"]
    file_us.writerow(header)"""

with open("Usuarios.csv", "r") as file_us_r:
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
            ad_claves.append(int(row[1]))

print('¡Bienvenido! Por favor, ingresa tu información para iniciar sesión')


class Login:
    def __init__(self):
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
                    print(f'\nIngreso como el siguiente administrador: {check_username}')
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
        print("7: Volver")

        eleccion = int(input(f"\nIngrese la opción a seguir: "))

        if eleccion == 1:
            ciudadanos = AppDataBase.ciudadanos_a_bloquear

            if ciudadanos != []:
                print("\nCiudadanos a bloquear:")
                i=0
                for c in ciudadanos:
                    print(f"{i+1}: {c}")

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
                    print(f"{i+1}: {c}")

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

            e = input("Si desea volver, marque v: ")

            if e != "v":
                nombre = input("\nIngrese el nombre que se le dará al nuevo admin: ")
                clave = int(input("\nIngrese la clave que se le dará al nuevo admin: "))

                admin.crearAdmin(nombre, clave)
                self.opciones_admin(admin)
            else:
                self.opciones_admin(admin)

        if eleccion == 4:
            if len(administradores) >= 1 :
                print("\nAdministradores:")
                i=0
                for a in administradores:
                    print(f"{i+1}: {a}")

                eleccion_a = int(input(f"\nIngrese el n° correspondiente al administrador a borrar o 0 para volver: "))

                if eleccion_a != 0:
                    admin.bloquearCiudadano(administradores[eleccion_a-1])
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
                    print(f"{i+1}: {a}")

                eleccion_a = int(input(f"\nIngrese el n° correspondiente al administrador a editar o 0 para volver: "))

                if eleccion_a != 0:
                    nombre = input(f"\nIngrese el nuevo nombre del administrador a editar: ")
                    clave = int(input(f"\nIngrese la nueva clave del administrador a editar: "))

                    admin.editarAdmin(administradores[eleccion_a-1], nombre, clave)

                    print(f"{administradores[eleccion_a-1]} ha sido modificado. Su nuevo nombre es {nombre} y su nueva clave es {clave}")
                    self.opciones_admin(admin)
                else:
                    self.opciones_admin(admin)

        if eleccion == 6:
            nueva_categoria = input("\nIngrese el nombre de la nueva categoría o v para volver: ")
            if nueva_categoria != "v":
                admin.crearTipoDeEvento(nueva_categoria)
                Tipos_de_eventos.append(nueva_categoria)
                self.opciones_admin(admin)
            else:
                self.opciones_admin(admin)

        if eleccion == 7:
            self.__init__()


    def login_check_us(self):
        key1 = self.__username
        value1 = self.__password

        if key1 in usuarios and value1 in claves and usuarios.index(key1) == claves.index(value1):
            print(f'\nBienvenido/a otra vez, {self.__username}')
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

        with open("Usuarios.csv", "r") as file_us_r:
            file_us_rd = csv.reader(file_us_r, delimiter=",")
            next(file_us_rd)
            for row in file_us_rd:
                if len(row) != 0:
                    usuarios.append(row[0])
                    claves.append(int(row[1]))
                    CUILs.append(int(row[3]))
                    celulares.append(int(row[2]))

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
        print("4: Cambiar de cuenta")

        eleccion = int(input("\nElige tu opción a seguir: "))

        if eleccion == 1:
            self.enviar_solicitud(usuario_actual)

        if eleccion == 2:
            self.revisar_solicitudes(usuario_actual)

        if eleccion == 3:
            self.reportar_evento(usuario_actual)

        if eleccion == 4:
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
            print(f"{i+1}: {s}")

        eleccion_usuario = int(input("\nElige un usuario: "))

        print("\n¿Qué desear hacer?")
        print("1: Aceptar solicitud")
        print("2: Denegar solicitud")
        print("3: Cambiar usuario elegido")
        print("4: Volver")

        eleccion = int(input("\nElige tu opción a seguir: "))

        if eleccion == 1:
            usuario_actual.aceptarSolicitud(solicitudes_recibidas[eleccion_usuario-1])
            print(f"¡Ahora {solicitudes_recibidas[eleccion_usuario-1]} y tú son amigos!")

        if eleccion == 2:
            usuario_actual.denegarSolicitud(solicitudes_recibidas[eleccion_usuario-1])
            print(f"{solicitudes_recibidas[eleccion_usuario-1]} ha sido rechazado/a")

        if eleccion == 3:
            eleccion_usuario = int(input("\nElige un usuario: "))

        if eleccion == 4:
            self.opciones_usuario(usuario_actual)

    def reportar_evento(self, usuario_actual):

        print("\nCategorías disponibles")
        i=0
        for t in Tipos_de_eventos:
            print(f"{i+1}: {t}")

        eleccion_t = int(input("Indique de qué tipo de evento se trata o 0 para volver: "))

        if eleccion_t != 0:

            print("\n¿Con quién te encuentras?")
            print("1: Solo")
            i=1
            for c in usuario_actual.get_contactos():
                print(f"{i+1}: {c}")
            eleccion_c = int(input("\nIngrese su elección: "))
            coordenadas_x = int(input("\nIngrese las coordenadas x del evento: "))
            coordenadas_y = int(input("Ingrese las coordenadas y del evento: "))
            tup = (coordenadas_x, coordenadas_y)
            tipodeevento = Tipos_de_eventos[eleccion_t-1]
            fecha = int(input("\nIngrese la fecha del evento: "))
            hora = int(input("Ingrese la hora del evento: "))

            if eleccion_c != 1:
                usuario_actual.reportarEvento(tipodeevento, tup, fecha, hora)
                #tenes que aplicarlo a datetime y de paso armar la tabla de eventos
                #podríamos hacer que en usuarios haya una columna que diga si está bloqueado o no

    def cambiar_de_cuenta(self):
        self.__init__()


main = Login()
"""main.login_check()"""
