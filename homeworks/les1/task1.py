firstname = 'Иван'
lastname = 'Петров'
age = 18
weight = 70.5
print('Фамилия: ' + lastname)
print('Имя:' + firstname)
print('Возраст:' + str(age))
print('Вес:' + str(weight))

question = input('Сколько дней Вы изучаете Python?')
if question.isdigit():
    print(question)
else:
    print('Неверный формат ввода!')
