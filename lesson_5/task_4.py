# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.


my_dict = {'One': 'Один', 'Two': 'Два',
           'Three': 'Три', 'Four': 'Четыре'}

with open('for_task_4.txt', 'r', encoding='utf-8') as f:
    read_f = f.readlines()

for i in read_f:
    num = i.split()[0]
    i = i.replace(num, my_dict[num])
    with open('for_task_4_new.txt', 'a', encoding='utf-8') as f:
        print(''.join(i.splitlines()), file=f)
