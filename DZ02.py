class mali:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def pal (self):
        return self.width / 10 + 2
    def kos (self):
        return self.height * 4 + 3

    @property
    def fullTkan(self):
        return str(f'Площадь ткани общая \n'
                   f' {(self.width / 10 + 2) + (self.height * 4 + 3)}')

class COAT(mali):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 10 + 2)

    def __str__(self):
        return f'Площадь ткани на пальто {self.square_c}'

class JAC(mali):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 4 + 3)

    def __str__(self):
        return f'Площадь такани на костюм {self.square_j}'

COAT = COAT(5, 7)
JAC = JAC(2, 4)
print(COAT)
print(JAC)
print(COAT.fullTkan)
print(JAC.fullTkan)
print(JAC.pal())
print(JAC.kos())