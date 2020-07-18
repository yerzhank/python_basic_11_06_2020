age = input('Ввведите возраст:')
if age.isdigit():
    age = int(age)
    print(type(age))

    if age >= 19:
        print('Доступ разрешен XXX')
    elif age >= 16:
        print('Доступ разрешен')
    elif age >= 8:
        print('Мультики')
    else:
        print('Доступ запрещен')
else:
    print('Возраст должен быть числом!')
