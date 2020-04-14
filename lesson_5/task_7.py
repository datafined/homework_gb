# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать .


with open('for_task_7.txt', 'r', encoding='utf-8') as f:
    i = 0
    amount = 0
    for el in f.readlines():
        coast = (int(el.strip().split()[2])) - (int(el.strip().split()[3]))
        if coast > 0:
            print(f'Прибыль фирмы {el.strip().split()[0]} составляет '
                  f'{coast}')
            amount += (int(el.strip().split()[3]))
            i += 1
        else:
            print(f'Убыток фирмы {el.strip().split()[0]} составляет '
                  f'{abs(coast)}')
    print(f'Средняя прибыль {i} компаний составляет: {amount / i}')