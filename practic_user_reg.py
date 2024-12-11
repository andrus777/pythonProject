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

if __name__ == '__main__':
    database = Database()
    user = User(input("Введите логин:"), input("Введите пароль:"), input("Введите подтверждение пароля:"))
    database.add_user(user.username, user.password)
