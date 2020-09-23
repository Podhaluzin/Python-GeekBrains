try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    c = a / b
    print("Частное: %.2f" % c)
except ValueError:
    print("Нельзя вводить строки")
except ZeroDivisionError:
    print("Нельзя делить на ноль")