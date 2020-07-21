var_list = []
elements_count = input('Введите количество элементов списка:')
i = 0
if elements_count.isdigit():
    while i < int(elements_count):
        var_tmp = input('Введите ' + str(i) + ' й элемент списка: ')
        var_list.append(var_tmp)
        i += 1
    j = 0
    for item in range(int(len(var_list)/2)):
        var_list[j], var_list[j+1] = var_list[j+1], var_list[j]
        j += 2
    print(var_list)
else:
    print('Не правильный ввод!')
