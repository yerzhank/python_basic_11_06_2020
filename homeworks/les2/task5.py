my_list = [7, 5, 3, 3, 2]
new_rate = int(input('Введите новый элемент рейтинга: '))
my_list.append(new_rate)
print(sorted(my_list, reverse=True))
