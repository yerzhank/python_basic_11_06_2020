import time
timesec = input('Введите время в секундах:')
if timesec.isdigit():
    print(time.strftime('%H:%M:%S', time.gmtime(int(timesec))))
else:
    print('Неверный формат ввода!')