proceeds = float(input('Введите сумму выручки:'))
cost = float(input('Введите сумму издвержки:'))
profit = proceeds - cost
if proceeds > cost:
    print('Фирма работает с прибылью : ' + str(profit))
    emp_count = int(input('Введите количество сотрудников: '))
    profit_per_one = profit / emp_count
    print('Прибыль в расчете на ордного сотрудника : ' + str (profit_per_one))
elif proceeds < cost:
    print('Фирма работает с убытком : ' + str(profit))