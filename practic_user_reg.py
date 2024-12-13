class User:
    """
    Класс пользователя, содержит атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_conform):
        self.username = username
        if password == password_conform:
            self.password = password


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

    def is_login(self, login):
        if self.data.get(login, 0) == 0:
            return False
        else:
            return True
    def is_autorize(self, login, password):
        test = self.data.get(login, -1)
        if test == password:
            return True
        else:
            return False

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input("Приветствую! Выберите действие: \n0 - Вход\n1 - Регистрация\n")
        if choice == '1':
            user = User(input("Введите логин:"), password := input("Введите пароль:"), password2 := input("Введите подтверждение пароля:"))
            if password != password2:
                exit()
            else:
                database.add_user(user.username, user.password)

        elif choice == '0':
            login = input("Введите логин:")
            password = input("Введите пароль:")
            if database.is_autorize(login, password):
                print("Авторизация успешна!")
                exit()
            else:
                print("Не правильные имя пользователя и пароль!")
                exit()






