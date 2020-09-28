class Road:
    weight = 8
    thickness = 8
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def mass_calculation(self):
        return self.__length * self.__width * self.weight * self.thickness
a = Road(30000, 30)
print(a.mass_calculation())
