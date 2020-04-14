# Реализовать функцию my_func(), которая принимает три
# позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.


def my_func(a, b, c):
    max_1 = int(max(a, b, c))
    min_1 = int(min(a, b, c))
    max_2 = (a + b + c) - (max_1 + min_1)
    max_abs = max_1 + max_2
    return max_abs


print(my_func(1, 2, 3))
