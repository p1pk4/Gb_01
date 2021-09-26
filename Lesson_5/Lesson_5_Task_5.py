'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
#
Task 5.
'''


summ = 0
# new_summ = 0
with open('t5.txt', 'w+') as file_5:
    numbers = input('input numbers: ')
    file_5.write(numbers)

with open('t5.txt') as file_5_summ:
    content = file_5_summ.read().rstrip().split() # Делаем список из чисел.
    # print(type(content))
    print(content)
    digit_list = [int(i) for i in content if i.isdigit()]
    print(sum(digit_list))


    # for i in content:
    #     if i.isdigit():
    #         dig = int(i)
    #         print(type(i))
    #         summ = dig + dig
    #         print(summ)