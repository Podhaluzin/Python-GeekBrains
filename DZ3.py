class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения '))
                self.my_list.append(val)
                print(f'Текущий список {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                stop = input(f'Напиши stop для выхода ')

                if stop == 'stop' or stop == 'stop':
                    print(try_except.my_input())
                else:
                    return f'Пока'

try_except = Error(1)
print(try_except.my_input())