import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = []
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            if self.sides_count > 0 :
                for i in range(0, self.sides_count):
                    self.__sides.append(1)
            else:
                self.__sides = []
        self.__color = None
        self.filled = True
        self.set_color(color[0], color[1], color[2])
        # print(f'======================================')
        # print('Объект:', type(self))
        # print('Количество сторон:', self.sides_count, " значение сторон:", self.__sides)
        # print(f'Цвет: {self.__color}, заливка:{self.filled}')
        # print(f'======================================')

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r in range (0, 255) and g in range (0, 255) and b in range (0, 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        result = True
        if len(sides) == self.sides_count:
            for side in sides:
                if type(side) is not int:
                    result = False
        else:
            result = False
        return result

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr = 0
        for side in self.__sides:
            perimetr += side
        return perimetr


    def set_sides(self, *new_sides):
        # print(f'Объект: {type(self)} Стороны текущие: {self.__sides}, стороны новые: {new_sides},  количество сторон: {len(new_sides)}')
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius * self.__radius


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        if (sides[0] + sides[1]) <= sides[2] or (sides[1] + sides[2]) <= sides[0] or (sides[2] + sides[0]) <= sides[1]: # условие корректности треугольника
            sides = (1, 1, 1)
        super().__init__(color, *sides)

    def get_square(self):
        pp = self.__len__() / 2
        return math.sqrt(pp * (pp - self.get_sides()[0]) * (pp - self.get_sides()[1]) * (pp - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        sides = (side,)
        for i in range(1, self.sides_count):
            sides = sides + (side,)
        self.__sides = list(sides)
        super().__init__(color, *sides)

    def get_volume(self):
        volume = self.__sides[0] * self.__sides[0] * self.__sides[0]
        return volume



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
print(cube1.get_sides())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

tr = Triangle((10,10,20), 10,20,30)
print(tr.get_sides())
print(tr.__len__())
print(tr.get_square())