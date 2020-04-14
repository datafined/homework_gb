# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчете на одного сотрудника.

revenue = int(input('Введите сумму выручки фирмы (в рублях): '))
costs = int(input('Введите сумму издержек фирмы (в рублях): '))
profit = ((revenue - costs) / costs) * 100  # Рентабельность рассчитывал по данной формуле.

if revenue > costs:
    print('Ваша фирма прибыльна.')
    print(f'Рентабельность составляет {profit:.1f} процента(ов).')
    quantity = int(input('Для рассчета прибыли на человека введите количество сотрудников: '))
    revenue_person = (revenue - costs) / quantity
    print(f'Прибыль фирмы в рублях в рассчете на одного сотрудника составляет {revenue_person:.0f}')
elif revenue < costs:
    print('Ваша фирма убыточна.')
else:
    print('Ваша фирма выходит в "0"')