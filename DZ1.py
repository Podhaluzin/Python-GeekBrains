class Data:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def extract(cls, d_m_y):
        my_date = []

        for i in d_m_y.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неверный год'
            else:
                return f'Неверный месяц'
        else:
            return f'Неверный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.d_m_y)}'

today = Data('22 - 09 - 2020')
print(today)
print(Data.valid(11, 11, 2022))
print(Data.extract('22 - 09 - 2022'))
print(today.valid(11, 13, 2011))
print(today.extract('22 - 099 - 2020'))