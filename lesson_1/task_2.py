# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

all_sec = int(input('Введите количество секунд: '))
hours = all_sec // 3600
minutes = (all_sec // 60) % 60
seconds = all_sec % 60
print(f'Время в формате чч:мм:сс составляет: {hours:02}:{minutes:02}:{seconds:02}')