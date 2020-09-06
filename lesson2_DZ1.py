n_int = 9
n_float = 5.8
n_str = "Hello"
n_list = ['a', '10']
n_tuple = ('b', '65')
n_dict = {'city': 'Orsk'}

all_list = [n_int, n_float, n_str, n_list, n_tuple, n_dict]
for i in all_list:
    print(f'{i} is {type(i)}')