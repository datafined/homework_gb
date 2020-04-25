# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumbers:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.x = 'a + b * n'

    def __add__(self, other):
        print(f'Сумма равна')
        return f'x = {self.a + other.a} + {self.b + other.b} * n'

    def __mul__(self, other):
        print(f'Произведение равно')
        return f'x = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * n'

    def __str__(self):
        return f'x = {self.a} + {self.b} * n'


first_arg = ComplexNumbers(-5, -6)
second_arg = ComplexNumbers(24, 24)
print(first_arg)
print(first_arg + second_arg)
print(first_arg * second_arg)
