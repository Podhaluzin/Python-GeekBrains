number = input("Введите число: ")
n = 0
for i in number:
    while int(i) > n:
        n = int(i)
print(n)