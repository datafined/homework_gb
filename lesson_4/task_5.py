#  Реализовать формирование списка, используя функцию range() и возможности
#  генератора. В список должны войти четные числа от 100 до 1000
#  (включая границы). Необходимо получить результат вычисления произведения
#  всех элементов списка.
# Подсказка: использовать функцию reduce()
import sys
from functools import reduce

number = [item for item in range(100, 1001) if not item % 2]
summary = reduce(lambda x, y: x * y, number)
print(summary)
