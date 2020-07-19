a = 2
b = 3
i = 1
isTrue = True
while (isTrue):
    a = a + a * 0.10
    i += 1
    print(str(i) + 'й день:' + str(round(a, 2)))
    if a >= b:
        break
