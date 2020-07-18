n = input('Введите число:')
if n.isdigit():
    i = 0
    j = int(n)
    count = 3
    sum = 0
    while i < count:
        sum = sum + j
        j = (j * 10) + int(n)
        i += 1

    print(sum)
else:
    print('Неправильный формат ввода')
