'''
# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
# Task 3.
'''

my_list = []

def my_func(a, b, c):
    """Принимает три позиционных аргумента и возвращает сумму двух наибольших аргументов.
    
    a, b, c -- аргументы задаются пользователем.
    a, b, c -- аргументы формируют список.
    total = a + b + c - min.
    """
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)
    total = a + b + c - min(my_list)
    print(total)
    
my_func(a = int(input()), b = int(input()), c = int(input()))