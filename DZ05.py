proceed = int(input("Введите значение выручки: "))
outlay = int(input("Введите значение задержки: "))
if proceed > outlay:
    profitability = proceed-outlay
    rent = profitability/proceed
    print(f"Отлично, у вас есть {profitability} рентабельность")
    worker = int(input("Сколько чсчеловек работает: "))
    print(f"{profitability/worker} на одного работника")
elif proceed == outlay:
    print("Не плохо")
else:
    print("Всё ужасно")