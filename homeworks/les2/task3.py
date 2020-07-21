user_month = int(input('Введите месяц от 1 до 12:'))
if (user_month > 0) and (user_month <= 12):
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9,
             10, 11, 12]

    season = {
        'Зима': (month[0], month[1], month[11]),
        'Весна': (month[2], month[3], month[4]),
        'Лето': (month[5], month[6], month[7]),
        'Осень': (month[9], month[10], month[11])
    }

    print('Вы выбрали месяц ' + str(month[user_month - 1]))

    for key in season.keys():
        if user_month in season[key]:
            print(key)
else:
    print('Неправильный ввод!')
