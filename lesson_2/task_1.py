# Создать список и заполнить его элементами различных типов
# данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

any_list = ['start', 78, 55.4, True, 'end']
for i in any_list:
    print(type(i))