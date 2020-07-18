n = input('Введите целое положительное число')
if n.isdigit():
    if int(n) > 0:
        print('>0')
        count_len = len(n)
        i = 0
        max = n[0]
        while (i < count_len):
            if n[i] > max:
                max = n[i]
            i += 1
        print(max)
    else:
        print('<0')
else:
    print('not ok')