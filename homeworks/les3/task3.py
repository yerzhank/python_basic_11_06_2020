def my_func(a, b, c):
    my_list = [a, b, c]
    min = my_list[0]
    i = 0
    while i < int(len(my_list)):
        if my_list[i] < min:
            min = my_list[i]
        i += 1
    # Находим и исключаем минимальный элемент
    my_list.remove(min)
    return sum(my_list)


print(my_func(8, 4, 7))
