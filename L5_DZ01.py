with open('test_1.txt', 'w') as f:
    test_1 = 1
    while test_1:
        test_1 = input('Введите строку текста: ')
        f.write(f'{test_1}\n')
