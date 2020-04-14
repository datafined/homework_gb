# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести
# фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


with open('for_task_3.txt', encoding='utf-8') as f:
    for line in f:
        new_list = line.split()
        if int(new_list[1]) < 20000:
            print(f'Зарплата сотрудника {new_list[0]} составляет {new_list[1]}')
        else:
            continue

with open('for_task_3.txt', encoding='utf-8') as f:
    new_list_2 = []
    i = 0
    x = 0
    ind = 0
    for line in f:
        a = line.split()
        new_list_2.append(int(a[1]))
        i += 1
    print(f'Средняя зарплата на сотрудника составляет {sum(new_list_2) / i} рублей')

