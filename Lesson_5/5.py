'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
#
Task 5.
'''
# summ = 0
new_summ = 0
with open('sum_digits.txt', 'w+') as f_obj:
    print('input numbers')
    a = input()
    f_obj.write(a)
    for line in f_obj:
        summ = line.split(' ')
    print(line)
    
    #     new_summ = int(summ)
    #     new_summ += summ
    # print(new_summ)
# print(a)
