# Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


file = open('for_task_1.txt', 'w')
file.write('first string\nsecond string\nthird string\n')
file.close()
