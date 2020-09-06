import sys

result = 0
while True:
    line = input("Введи число и нажми Enter, или q для выхода: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f"Ответ {result}. Программа завершена")
                exit(0)
            else:
                print(f"Сумма ваших чисел равна {result}.", file=sys.stderr)
                exit(1)
print(result)
exit()