# Реализовать функцию int_func(), принимающую слово из маленьких
# латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать
# строка из слов, разделенных пробелом. Каждое слово состоит из
# латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

# Вариант 1
def int_func(word):
    '''Использует встроенный метод .capitalize'''
    return word.capitalize()

#Вариант 2
def int_func_1(word):
    '''Без использования метода .capitalize'''
    return f'{word[0].upper()}{word[1:]}'


def int_func_2(word):
    return word.title()


print(int_func('test'))
print(int_func_1('test'))
print(int_func_2('every word begins with a capital letter'))
