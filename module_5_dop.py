import time

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def log_out (self):
        self.current_user = None

    def add (self, *videos):
        for video in videos:
            if video in self.videos:
                print(f'видео с названием {video.title} уже есть')
            else:
                self.videos.append(video)

    def register(self, nickname, password, age):
        nick_not_search = True
        for user in self.users:
            if user.nickname == nickname:
                nick_not_search = False
        if nick_not_search:
            self.users.append(User(nickname, password, age))
            # print('Добавлен пользователь с именем', nickname)
            self.log_in(nickname, password) # вход через log_in, а не на прямую сменой current_user, т.к. во время инициализации могут происходить дополнительные действия
        else:
            print('Пользователь с именем', nickname, 'уже существует!')

    def get_videos(self, word):
        list = []
        for video in self.videos:
            if  word.lower() in video.title.lower():
                list.append(video.title)
        return list

    def watch_video(self, film_name):
        for video in self.videos:
            if  film_name == video.title:
                if self.current_user != None:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else: # Проигрывание видео
                        current_time = 1
                        while current_time <= video.duration:
                            print(f'Проигрывание видео "{video.title}" ({current_time} секунда из {video.duration})')
                            time.sleep(1)
                            current_time += 1
                        print(f'Конец видео')
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео')


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title # Название видео
        self.duration = duration # Продолжительность видео в секундах
        self.time_now = 0 # Секунда остановки default = 0
        self.adult_mode = adult_mode # ограничение по возрасту default = False

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}, Возраст:{self.age}'



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

