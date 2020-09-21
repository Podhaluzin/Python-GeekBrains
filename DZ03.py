class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
    
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
     
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))
    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))
    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

gratings = Cell(22)
pillars = Cell(7)
print(gratings)
print(gratings + 
pillars)
print(
pillars - gratings)
print(
pillars.make_order(6))
print(gratings.make_order(15))
print(gratings / 
pillars)