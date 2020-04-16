# Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police ( булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
# базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 ( TownCar ) и
# 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните
# доступ к атрибутам, выведите результат. Выполните вызов методов
# и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} start going'

    def stop(self):
        return f'{self.name} is stop'

    def turn(self, where):
        self.where = where
        if self.where == 'right':
            return f'{self.name} turning right'
        elif self.where == 'left':
            return f'{self.name} turning left'

    def show_speed(self):
        return f'{self.name} speed {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 41:
            return f'{self.name} без превышения, скорость {self.speed} км/ч'
        else:
            return f'{self.name} с превышением на {self.speed - 40} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 41:
            return f'{self.name} без превышения, скорость {self.speed} км/ч'
        else:
            return f'{self.name} с превышением на {self.speed - 40} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town = TownCar(50, 'red', 'audi', False)
sport = SportCar(40, 'yellow', 'bmw', False)
work = WorkCar(40, 'blue', 'renault', False)
police = PoliceCar(40, 'white', 'ford', True)

print(town.show_speed())
print(work.show_speed())
print(police.show_speed())
print(town.go())
print(town.turn('left'))
