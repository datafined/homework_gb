# Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input('Введите число: '))
x = -1
while number > 10:
    a = number % 10
    number = number // 10
    if a > x:
         x = a
print(f'Самой большой цифрой в веденном числе является {x}')
