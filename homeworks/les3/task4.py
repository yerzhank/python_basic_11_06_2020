def my_func_v1(x: float, y: int) -> float:
    return x ** y


def my_func_v2(x: float, y: int) -> float:
    i = -1
    result = 1
    while i >= y:
        i -= 1
        result = result / x
    return result


print(my_func_v1(2.5, -3))
print(my_func_v2(2.5, -3))
