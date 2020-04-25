# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.


class Data:
    def __init__(self, user_date=None):
        self.user_date = str(user_date)

    @classmethod
    def exec_int(cls, user_date):
        int_date = []
        for el in user_date.split('_'):
            int_date.append(el)
        return f'{int(int_date[0])}, {int(int_date[1])}, {int(int_date[2])}'

    @staticmethod
    def validation_method(user_date):
        to_valid = []
        for el in user_date.split('_'):
            to_valid.append(el)
        if int(to_valid[0]) < 1 or int(to_valid[0]) > 31:
            return f'Wrong day'
        if int(to_valid[1]) < 0 or int(to_valid[1]) > 12:
            return f'Wrong month'
        if int(to_valid[1]) < 1:
            return f'Wrong year'
        else:
            return f'All is right'


d = Data()
print(d.exec_int('31_01_2020'))
print(d.validation_method('31_01_2020'))
