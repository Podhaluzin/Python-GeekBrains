a = float(input("Введите первое значение: "))
b = float(input("Введите второе значение: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)