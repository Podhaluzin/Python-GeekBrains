from itertools import count
for el in count (int(input('Введите число'))):
    if el > 70:
        break
    else:
        print(el)
