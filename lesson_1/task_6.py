# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил  километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена
# составит не менее b километров. Программа должна принимать значения
# параметров  и b и  выводить одно натуральное число — номер дня.
# Например:  = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input("Введите результат первого дня в километрах: "))
b = int(input("Введите желаемое количество километров: "))
day = 1
all_km = a
while all_km < b:
    a = a + 0.1 * a
    day += 1
    all_km = all_km + a
print(f'Номер дня: {day}')