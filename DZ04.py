class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} тронулась'
    def stop(self):
        return f'{self.name} остановилась'
    def turn_right(self):
        return f'{self.name} повернула направо'
    def turn_left(self):
        return f'{self.name} повернула налево'
    def show_speed(self):
        return f'Текущая скорость {self.name} является {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} является {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше для городского автомобиля'
        else:
            return f'Скорость {self.name} нормальная для городского автомобиля'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} является {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена для рабочей машины'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'

mitsubishi = SportCar(100, 'Синяя', 'Митсубиси', False)
toyota = TownCar(30, 'Черная', 'Тайота', False)
lexus = WorkCar(70, 'Красный', 'Лексус', True )
rover = PoliceCar(110, 'Синий',  'Ренж-Ровер', True)
print(lexus.turn_left())
print(f'Когда {toyota.turn_right()}, затем {mitsubishi.stop()}')
print(f'{lexus.go()}со скоростью {lexus.show_speed()}')
print(f'{lexus.name} является {lexus.color}')
print(f'{mitsubishi.name} полицейский автомобиль {mitsubishi.is_police}')
print(f'{lexus.name}  полицейский автомобиль {lexus.is_police}')
print(mitsubishi.show_speed())
print(toyota.show_speed())
print(rover.police())
print(rover.show_speed())