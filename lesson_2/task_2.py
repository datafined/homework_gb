# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить
# на своем месте. Для заполнения списка элементов необходимо
# использовать функцию input().

new_list = []
user_list = []
n = 1
m = 0

quantity = int(input('Введите количество: '))
for i in range(quantity):
    new_el = input('Введите элемент: ')
    user_list.append(new_el)

if (len(user_list) % 2) == 0:
    while n < len(user_list):
        new_list.append(user_list[n])
        new_list.append(user_list[m])
        n += 2
        m += 2
    print(new_list)
elif len(user_list) == 1:
    print(user_list)
else:
    while n < len(user_list) - 1:
        new_list.append(user_list[n])
        new_list.append(user_list[m])
        n += 2
        m += 2
        if len(new_list) == len(user_list) - 1:
            new_list.append(user_list[-1])
    print(new_list)
