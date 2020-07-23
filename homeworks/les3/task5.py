def func_sum(s: str) -> int:
    spec_flag = 0
    my_lst = s.split(' ')
    result_sum = 0
    for itm in my_lst:
        if (ord(itm) > 96) and (ord(itm) < 123):
            pass
        elif (ord(itm) >= 48) and (ord(itm) <= 57):
            result_sum = result_sum + int(itm)
        else:
            spec_flag = 1
            return result_sum, spec_flag
    return result_sum, spec_flag


while True:
    user_str = input('Введите строку через пробел:')
    sum_val, flag = func_sum(user_str)
    print(sum_val)
    if flag == 1:
        break


