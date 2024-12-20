import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = []
        self.filled = True
        self.__color = (0, 0, 0)
        print("Im Figure!", type(self), self.__sides)
        self.set_color(color[0], color[1], color[2])
        self.set_sides(sides)
        print(self.__sides)

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

    def __is_valid_sides(self, sides):
        result = True
        if len(sides) == self.sides_count:
            for side in sides:
                if side.type is not int:
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
        if len(*new_sides) == self.sides_count:
            self.__sides = list(*new_sides)
        else:
            if self.sides_count > 0 :
                for i in range(1, self.sides_count):
                    self.__sides.append(1)

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
        super().__init__(color, *sides)

    def get_square(self):
        pp = self.__len__() / 2
        return math.sqrt(pp * (pp - self.__sides[0]) * (pp - self.__sides[1]) * (pp - self.__sides[2]))


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, *sides)


    def get_volume(self):
        return self.__sides[0] * self.__sides[0] * self.__sides[0]

    def set_sides(self, *new_sides):
        print(self.__sides)
        if len(*new_sides) == 1:
            side_one = list(*new_sides)[0]
            print("one", side_one, self.sides_count)
            for i in range(1, self.sides_count):
                print("Im Cube! - ", i)
                #self.__sides.append(side_one)
        else:
            if self.sides_count > 0:
                for i in range(1, self.sides_count):
                    self.__sides.append(1)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
tr = Triangle((10,10,10), 20,15,16)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

