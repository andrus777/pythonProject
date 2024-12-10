import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, amount):
        """ Уменьшение здоровья игрока """
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return f'{self.name} получил {amount} урона. Текущее здоровье игрока {self.health}'

    def heal(self, amount):
        """ Восстановление здоровья игрока """
        self.health += amount
        if self.health > 100:
            self.health = 100
        return f'{self.name} восстановил {amount} здоровья. Текущее здоровье игрока {self.health}'



class Room:
    def __init__(self, description):
        self.description = description
        self.items = []
        self.enemy = None

    def add_item(self, item):
        self.items.append(item)
        return f'В комнату добавлен предмет {item}'

    def show_items(self):
        if not self.items:
            return 'В комнате предметов нет'
        else:
            return 'Предметы в комнате: ' + ", ".join(self.items)

    def set_enemy(self, enemy):
        self.enemy = enemy

    def show_enemy(self):
        """ Информация о враге и комнате """
        if self.enemy:
            return f'Вы встретили врага: {self.enemy.name}, его здоровье {self.enemy.health}'
        return 'Врагов в комнате нет'


class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        """ Уменьшение здоровья врага """
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return f'{self.name} получил {amount} урона. Текущее здоровье врага {self.health}'


hero = Player('Герой')
rooms = [
    Room('Болото'),
    Room('Цитадель'),
    Room('Арена'),
]

enemies = [
    Enemy('Скелет', 30),
    Enemy('Гоблин', 20),
    Enemy('Орк', 50)
]


while True:
    current_room = random.choice(rooms)
    current_enemy = random.choice(enemies)
    current_room.set_enemy(current_enemy)
    print(f'Вы находитесь в локации: {current_room.description}')
    print(f'Вокруг: {current_room.show_items()}')
    print(f'Враг: {current_room.show_enemy()}')

    if hero.health <= 0:
        print(f'Игра окончена. {hero.name} остался без сил')
        break

    command = input('Выберите действие: 1-бой, 2-лечение, 3-выход: ')

    if command == '1':
        while current_enemy.health > 0 and hero.health >0:
            hero_damage = random.randint(5, 15)
            enemy_damage = random.randint(10, 25)
            print(hero.take_damage(enemy_damage))
            print(current_enemy.take_damage(enemy_damage))

            if current_enemy.health <= 0:
                print(f'{current_enemy.name} повержен! Вы победили!')
                break
            if hero.health <= 0:
                print(f'Вы проиграли..')
                break
    elif command == '2':
        hero_health = random.randint(10, 50)
        print(hero.heal(hero_health))
