'''
# Создать список и заполнить его элементами различных типов данных. 
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. 
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
#
# Task 1.
'''

my_list = [1, 2, 3, 4, 'a', ',', '213', 123.2, True]

data_type_int = 0
data_type_str = 0
data_type_float = 0
data_type_bool = 0

def data_type_print():
    print(f'В списке "my_list" тип данных "int" встречается:\t{data_type_int} раза.\n')
    print(f'В списке "my_list" тип данных "str" встречается:\t{data_type_str} раза.\n')
    print(f'В списке "my_list" тип данных "float" встречается:\t{data_type_float} раз.\n')
    print(f'В списке "my_list" тип данных "bool" встречается:\t{data_type_bool} раз.\n')
    return data_type_int, data_type_str, data_type_float, data_type_bool

for i in my_list:
    print(type(i))
    if type(i) == int:
        data_type_int += 1
    elif type(i) == str:
        data_type_str += 1
    elif type(i) == float:
        data_type_float += 1
    elif type(i) == bool:
        data_type_bool += 1
data_type_print()