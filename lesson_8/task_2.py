# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
# ошибкой.


class DevByZero:
    def __init__(self, divider, denom):
        self.divider = divider
        self.denom = denom

    @staticmethod
    def divide_by_null(divider, denom):
        try:
            return divider / denom
        except:
            return f'На "0" делить нельзя'


div = DevByZero(5, 20)
print(DevByZero.divide_by_null(50, 0))
print(DevByZero.divide_by_null(20, 2))
print(div.divide_by_null(100, 0))
