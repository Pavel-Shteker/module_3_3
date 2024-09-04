def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 5 вариантов
print_params()                    # без изменений
print_params(5)                   # изменим а
print_params(5, 'checkitout')     # изменим а и строка
print_params(b=25)                # изменим а и строку на цифру
print_params(c=[1, 2, 3])         # изменим с на список

values_list = [13, 'идальго', False]
values_dict = {'a': 6.66, 'b': 'сомбреро', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'строка']
print_params(*values_list_2, 42)

# работает... немыслимо.
