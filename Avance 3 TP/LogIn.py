print('WELCOME USER , Please Enter Your Login Information')


class Login:
    def __init__(self, cuil, celular, clave):
        self.__cuil = cuil
        self.__username = celular
        self.__password = clave

    def login_check(self):
        key1 = self.__username
        value1 = self.__password

        if key1 in self.__data and value1 == self.__data[key1]:
            print(f'\nWelcome Back {self.__username}')

        else:
            print("\nWrong Username Or Password")
            ask = input("\nAre You A New User? Y/N : ")

            if ask == "y":
                self.new_user()

            if ask == 'n':
                check_username = input("\nUsername : ")
                check_password = input("Password : ")

                key, value = check_username, check_password

                if key in self.__data and value == self.__data[key]:
                    print(f"\nWELCOME {check_username}!!")

    def new_user(self):
        new_username = input('\nPlease Enter A New Username : ')
        new_password = input('Please Enter A New Password : ')

        self.__data[new_username] = new_password

        check_username = input("\nUsername : ")
        check_password = input("Password : ")

        key, value = check_username , check_password

        if key in self.__data and value == self.__data[key]:
            print(f"\nWELCOME {check_username}!!")
        else:
            self.login_check()


main = Login()
main.login_check()
