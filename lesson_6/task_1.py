# Создать класс TrafficLight ( светофор) и определить у него
# один атрибут color ( цвет) и метод running ( запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый)— на
# ваше усмотрение. Переключение между режимами должно осуществляться
# только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляри вызвав описанный метод.
import time


class TrafficLite:
    def __init__(self, color=''):
        self.color = color

    def running(self, color=''):
        self.color = color
        while True:
            if color == '':
                print('red light')
                color = 'yellow'
                time.sleep(7)
            elif color == 'yellow':
                print('yellow light')
                color = 'green'
                time.sleep(2)
            elif color == 'green':
                print('green light')
                time.sleep(1)
                return f'Цикл окончен'


a = TrafficLite()
print(a.running())
