products = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
            (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
            (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
            ]

cnt_tuple = len(products)
i = 0
my_dict = {0: products[0][1]}

result_dict = {}
keys = []
values = []
result_values = []
for key in my_dict[0].keys():
    keys.append(key)
    while i < cnt_tuple:
        my_dict[i] = products[i][1]
        values.append(my_dict[i][key])
        i += 1
    result_values = values.copy()
    result_dict[key] = result_values
    values.clear()
    i = 0
print(result_dict)

