user_choice = input('Нажмите ENTER, для запуска скрипта')
if user_choice == '':
    from itertools import cycle
    my_list = [True, 'ABC', 123, None]
    i = 0
    for el in cycle(my_list):
        if i == 12:
            break
        else:
            print(el)
            i += 1  
