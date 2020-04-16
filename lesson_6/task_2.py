# Реализовать класс Road ( дорога), в котором определить атрибуты:
# length ( длина), width(ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины
# полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, user_length, user_width):
        self._length = user_length
        self._width = user_width

    def get_mass(self):
        weight = 5
        thick = 1
        x = self._length * self._width * weight * thick
        return f'Mass {x} tonn'


result = Road(int(input("length: ")), int(input("width: ")))
print(result.get_mass())
