# Создать текстовый файл (не программно), сохранить в нем несколько
# строк, выполнить подсчет количества строк, количества слов
# в каждой строке.


with open('for_task_2.txt') as file:
    lines = 0
    words = 0
    for line in file:
        lines += 1
        if True:
            words = len(line.split())
            print(f'Количество слов в строке {lines} - {words}')
    print(f'Общее количество строк в файле: {lines}')
