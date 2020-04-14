# Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо
# числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введен после нескольких
# чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

stop = False
result = 0


while not stop:
    user_enter = input('Введите числа через пробел, для выхода введите "#": ')
    for number in user_enter.split():
        if number.lower() == '#':
            stop = True
            break
        result += float(number)
    print(int(result))