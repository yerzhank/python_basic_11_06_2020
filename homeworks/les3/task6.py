def int_func(s: str):
    return s.title()


print(int_func('text'))
var_str = 'hello world'
my_lst = var_str.split(' ')
for itm in my_lst:
    print(int_func(itm))