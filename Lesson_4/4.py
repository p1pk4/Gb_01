'''
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. 
#
Элементы вывести в порядке их следования в исходном списке. 
#
Для выполнения задания обязательно использовать генератор.
#
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
#
Task 4.
'''


mlist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]



new_list = [] 
s = [new_list.append(x) for x in mlist if x not in new_list]
print(list(new_list)) 

# x = [elem[0] for elem in groupby(mlist)]
# print(tuple(x))

# # print(list(set(mlist)))
# b = []
# a = [int(item) for item in mlist]
# # print(a)

# for item in mlist:
#     if mlist[0] != mlist[item]:
        
#         b.append(item)
#         print(list(b))
