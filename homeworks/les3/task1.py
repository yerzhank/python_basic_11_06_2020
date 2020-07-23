def func_div(a, b):
    return a / b


user_a = int(input('Введите А:'))
user_b = int(input('Введите B:'))
try:
    result = func_div(user_a, user_b)
    print(result)
except ZeroDivisionError as e:
    print(e)
