'''
Представлен список чисел. 
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. 
Для формирования списка использовать генератор.
#
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
#
Task 2.

'''

a_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

out = [i for i in range(20, 241, 20)]

print(next(out))

# print(type(my_list))



# # Создаем список
# alist = [4, 16, 64, 256]

# # Вычислим квадратный корень, используя генерацию списка
# out = [a**(1/2) for a in alist]
# print(out)
# print(type(out))
# # Используем выражение генератора, чтобы вычислить квадратный корень
# out = (a**(1/2) for a in alist)
# print(out)
# print(next(out))
# print(next(out))
# print(next(out))
# print(next(out))
# print(type(out))
# # print(next(out))