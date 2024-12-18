import math
class Figure:
    sides_count = 0
    def __init__(self, filled):
        self.__sides = []
        for side in filled:
            self.__sides.append(side)
        self.__color = (0, 0, 0)

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
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1
    def __init__(self, filled):
        super().__init__(self, filled)
        self.__radius = self.__len__() / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius * self.__radius



class Triangle(Figure):
    sides_count = 3
    def __init__(self, filled):
        super().__init__(self, filled)

    def get_square(self):
        pp = self.__len__() / 2
        return math.sqrt(pp * (pp - self.__sides[0]) * (pp - self.__sides[1]) * (pp - self.__sides[2]))


class Cube(Figure):
    sides_count = 12
    def __init__(self, cube_side):
        super().__init__(self, cube_side)
        self.__sides = []
        for i in range (1, 12):
            self.__sides.append(cube_side)

    def get_volume(self):
        return self.__sides[0] * self.__sides[0] * self.__sides[0]


